from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/send_message")
async def send_message(user_input: str):
    # 这里可以插入处理消息的逻辑，例如调用聊天机器人模型。
    # 下面是一个简单的回复例子。
    bot_response = f"你好，你刚才说了: {user_input}"
    return JSONResponse(content={"bot_response": bot_response})


@app.post("/clear_chat")
async def clear_chat():
    # 清除聊天的端点可能不需要在后端实现，
    # 因为这可以通过前端的JavaScript来处理。
    # 但是，如果需要的话，可以在这里添加逻辑。
    return JSONResponse(content={"message": "Chat cleared."})
