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
aheui_flag = False

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

        if "**C언어" in text and gcc_flag is not True:
            irc.send(channel, "지금부터 코드를 입력받겠습니다. 입력 종료 시, **fin 을 입력해주세요.")
            gcc_flag = True
            commander = text[:(text.find("!"))]
            print("MASTER: " + commander)
            codefile = open('code.c', 'w')

        if "**fin" in text and gcc_flag is True and aheui_flag is False and text[:(text.find("!"))] == commander:
            codefile.close()
            os.system("gcc code.c &> gcc_output.txt")
            os.system("(sleep 2; pkill a.out) & ./a.out &> program_output.txt")

            try:
                gccout = open('gcc_output.txt', 'r')
                prgout = open('program_output.txt', 'r')
                if os.path.getsize('program_output.txt') < 10000 and os.path.getsize('gcc_output.txt') < 10000:
                    gcclines = gccout.readlines()
                    prglines = prgout.readlines()

                    if len(gcclines) > 0 and len(gcclines) <= 50:
                        irc.send(channel, "GCC Output")
                        for l in gcclines:
                            irc.send(channel, l)
                    elif len(gcclines) > 50: irc.send(channel, "GCC 출력이 너무 깁니다.")

                    else:
                        if len(prglines) > 50 : irc.send(channel, "프로그램 출력이 너무 깁니다.")
                        else:
                            irc.send(channel, "Program Output")
                            for l in prglines:
                                time.sleep(0.4)
                                irc.send(channel, l)

                else: irc.send(channel, "프로그램 출력 또는 GCC 출력이 너무 깁니다.")

                gccout.close()
                prgout.close()
           
            except: irc.send(channel, "오류가 발생했습니다.")

            prglines = []
            gcclines = []
            gcc_flag = False


        if "**아희" in text and aheui_flag is False and gcc_flag is False:
            irc.send(channel, "지금부터 아희 코드를 입력받겠습니다. 입력 종료 시, **힣 을 입력해주세요.")
            aheui_flag = True
            aheui_commander = text[:(text.find("!"))]
            print("AHEUIDOL MASTER: " + aheui_commander)
            aheuifile = open('aheuitemp', 'w')

        if aheui_flag and "**힣" not in text and text[:(text.find("!"))] == aheui_commander:
            aheuifile.write(msg)
            
        if "**힣" in text and aheui_flag is True and  text[:(text.find("!"))] == aheui_commander:
            aheuifile.close()
            cwd = os.getcwd()
            os.system(cwd + "/aheui " + cwd + "aheuitemp > aheui_output.txt")
            time.sleep(2)
            os.system('pkill ' + 'aheui')

            aheuiout = open('aheui_output.txt', 'r')
            aheuilines = aheuiout.readlines()

            if len(aheuilines) > 0:
                irc.send(channel, "이하는 caheui의 출력입니다.")
                for l in aheuilines:
                    irc.send(channel, l)

            aheuiout.close()
            aheuilines = []
            aheui_flag = False
