from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class Message(BaseModel):
    user_input: str


@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/send_message")
async def send_message(message: Message):
    user_input = message.user_input
    if not user_input:
        raise HTTPException(status_code=400, detail="No message provided")
    # 这里可以插入处理消息的逻辑，例如调用聊天机器人模型。
    bot_response = f"Echo: {user_input}"  # Replace this with actual bot response logic
    return JSONResponse(content={"bot_response": bot_response})


@app.post("/clear_chat")
async def clear_chat():
    # This endpoint could be used for backend cleanup if necessary.
    return JSONResponse(content={"message": "Chat cleared."})
