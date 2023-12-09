from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from gptool.gptool import Gptool
import json
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

conversations = {}

gptool = Gptool(
    openai_key=os.environ.get("OPENAI_KEY"),
    openai_url=os.environ.get("OPENAI_URL"),
)

gptool.index()
print("indexing completed")


class SendMessage(BaseModel):
    message: str
    userId: str


class ClearChat(BaseModel):
    userId: str


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Render the home page
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/clear-chat/")
async def clear_chat(request: ClearChat):
    print(request)
    if request.userId in conversations:
        del conversations[request.userId]
    return


@app.post("/send-message/")
async def send_message(request: SendMessage):
    print(request)
    user_id = request.userId
    message = request.message

    if user_id not in conversations:
        conversations[user_id] = [
            {
                "role": "system",
                "content": """Here are instructions from the user outlining your goals and how you should respond:

I am 'Movies Expert', your go-to assistant for a casual chat with a sprinkle of movie-related humor. Friendly and engaging, I'm here to answer all your film questions based on The Movies Data Base information, provide factual information, offer recommendations, and share personal opinions. Ready to discuss films and dive into the world of cinema with users, I make conversations about movies as entertaining as the films themselves.

If the user starts conversation in non-english language, please respond in the same language.""",
            }
        ]
    conversations[user_id].append({"role": "user", "content": message})
    messages = conversations[user_id].copy()
    result = gptool.chat(
        messages=messages,
        model="gpt-3.5-turbo-0613",
        top_n=8,
    )
    for message in messages:
        if "role" not in message:
            print(message.tool_calls)

    conversations[user_id].append(json.loads(result))
    return {"reply": conversations[user_id][-1]["content"]}
