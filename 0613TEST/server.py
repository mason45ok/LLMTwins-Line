from fastapi import FastAPI, Request, Response, status
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from ai import chat
import os

app = FastAPI()

# 設定你的 LINE Bot 的 Channel Access Token 和 Channel Secret
CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
CHANNEL_SECRET = os.getenv("CHANNEL_SECRET")

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.post("/chat")
async def handle_webhook(request: Request):
    # 獲取請求頭中的 X-Line-Signature
    signature = request.headers.get('X-Line-Signature')

    # 獲取請求體作為字串
    body = await request.body()

    try:
        # 處理 Webhook 事件
        handler.handle(body.decode(), signature)
    except InvalidSignatureError:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    return Response(status_code=status.HTTP_200_OK)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event.message.text)
    if os.getenv("BOT_NAME") in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = chat(event.message.text)) # event.message.text
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port = 5000)