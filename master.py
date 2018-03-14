from irc import *

channel = "#minty99"
server = "moe.uriirc.org"
port = 16664
nickname = "master"

irc = IRC()
irc.connect(server, channel, port, nickname)

while True:
    text = irc.get_text()
    print("GET: " + text)
    text = text[1:]
    msg = text[(text.find(":")+1):-1]
    user = text[:(text.find("!"))]
    
    if "JOIN" in text and channel in text:
        irc.give_op(channel, user)

    if "PRIVMSG" in text and channel in text and user == "minty99":
        if "마스터 안녕" in text:
            irc.send(channel, "나는 이 채널의 마스터! 옵을 뿌리지!")
