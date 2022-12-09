# qqbot
# 对你有用的话点个star呗
## 已对接chatgpt 使用/chatgpt 加上你要提问等问题
## go-cqhttp用的v1.0.0-rc3
配置时选用反向ws
config反向ws配置为
```
universal: ws//127.0.0.1:8765/onebot/v11/ws/
```
如果遇到服务器部署go-cqhttp登陆问题的话先本地部署一个，用扫码登陆，然后将里面的session.token，device.json还有data文件夹替换进去
```
我的python版本为3.10.6(3.8.X应该都可以)
依赖版本
nb-cli                     0.6.8
nonebot-adapter-cqhttp     2.0.0a16
nonebot-adapter-onebot     2.1.5
nonebot-plugin-apscheduler 0.2.0
nonebot-plugin-guild-patch 0.2.1
nonebot2                   2.0.0rc1
revChatGPT                 0.0.32.1
缺啥pip install 就好了
chatgpt的配置在plugins chatgpt_bot.py里
想用其他的如账号密码的话看revChatGPT wiki(里面有怎样获取session_token方法)
https://github.com/acheong08/ChatGPT/wiki
```
配置完成直接python bot.py就可以
## How to start

1. generate project using `nb create` .
2. create your plugin using `nb plugin create` .
3. writing your plugins under `qqbot/plugins` folder.
4. run your bot using `nb run` .

## Documentation

See [Docs](https://v2.nonebot.dev/)
