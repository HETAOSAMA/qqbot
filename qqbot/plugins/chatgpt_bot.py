from nonebot import on_command
from nonebot.rule import Rule
from revChatGPT.revChatGPT import Chatbot
from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment
from nonebot.params import T_State
from nonebot.log import logger
import json

config = {
        "session_token": ""
}
chatbot = Chatbot(config, conversation_id=None)
ChatGptBot = on_command('chatgpt', priority=5)
@ChatGptBot.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    event = event.get_plaintext()
    response = chatbot.get_chat_response(event, output="text")
    message = response["message"]
    logger.info("响应消息"+str(message))
    # data = json.loads(str(response))
    
    await ChatGptBot.send(message)