from irc import *
import os
import random
import time

channel = "#minty99"
server = "moe.uriirc.org"
port = 16664
nickname = "mintybot"
 
irc = IRC()
irc.connect(server, channel, port, nickname)

while True:
    text = irc.get_text()
    print("GET: " + text)
    text = text[1:]
    msg = text[(text.find(":")+1):-1]
    user = text[:(text.find("!"))]
    if "PRIVMSG" in text and channel in text:

        if "민티봇 안녕" in text:
            irc.send(channel, "헌 새내기 minty99님이 만들어주신 봇이에요 ><")

        elif "민티봇 나가" in text:
            irc.send(channel, "으앙 싫어 안 나갈거야ㅠㅠㅠ")

        elif "민티봇 꺼져" in text and user == "minty99":
            if user == "minty99":
                exit()
            
            else:
                irc.send(channel, "나는 나보다 약한 자의 말은 듣지 않는다.")
    
    elif "JOIN" in text and channel in text and user == "master":
        irc.give_op(channel, "master")
