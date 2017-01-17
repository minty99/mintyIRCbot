from irc import *
import os
import random
import time

channel = "#botworld"
server = "irc.uriirc.org"
port = 16664
nickname = "mintybot"
 
irc = IRC()
irc.connect(server, channel, port, nickname)

gcc_flag = False

while 1:
    text = irc.get_text()
    print("GET: " + text)
    text = text[1:]
    msg = text[(text.find(":")+1):-1]
    if "PRIVMSG" in text and channel in text:

        if gcc_flag and "**fin" not in text and text[:(text.find("!"))] == commander:
            codefile.write(msg)

        if "**자기소개" in text:
            irc.send(channel, "파릇파릇한 새내기 minty99님이 만들어주신 봇이에요 ><")

        if "민티봇 나가" in text:
            irc.send_cmd(channel, "QUIT")
            exit()

        if "**C언어" in text:
            irc.send(channel, "지금부터 코드를 입력받겠습니다. 입력 종료 시, **fin 을 입력해주세요.")
            gcc_flag = True
            commander = text[:(text.find("!"))]
            print("MASTER: " + commander)
            codefile = open('code.c', 'w')

        if "**fin" in text:
            codefile.close()
            os.system("gcc \"" + os.getcwd() + "/code.c\" &> gcc_output.txt")
            os.system("\"" + os.getcwd() + "\/a.out\" > program_output.txt")
            time.sleep(2)
            os.system('pkill ' + 'a.out')

            gccout = open('gcc_output.txt', 'r')
            prgout = open('program_output.txt', 'r')
            gcclines = gccout.readlines()
            prglines = prgout.readlines()

            if len(gcclines) > 0:
                irc.send(channel, "이하는 GCC의 출력입니다.")
                for l in gcclines:
                    irc.send(channel, l)
            else:
                irc.send(channel, "이하는 컴파일된 프로그램의 출력입니다.")
                for l in prglines:
                    irc.send(channel, l)

            gccout.close()
            prgout.close()
            prglines = []
            gcclines = []
            gcc_flag = False