import os
print("kamc-gui package installer")
print("Hangi dağıtımı kullanıyorsunuz?")
print("ARCH : 1")
print("OPENSUSE : 2")
print("Debian & Ubuntu : 3")
print("Fedora : 4")
dagitim = input("")

if dagitim == "1":
    os.system("pacman -Syy")
    os.system("pacman -S net-tools-deprecated")
    os.system("pacman -S macchanger")
    os.system("pacman -S python3-pip")
    os.system("pacman -S xterm")
    os.system("pip install pyqt5")
    print("İşlem tamamlandi!")

if dagitim == "2":
    os.system("zypper refresh")
    os.system("zypper install net-tools-deprecated")
    os.system("zypper install macchanger")
    os.system("zypper install python3-pip")
    os.system("pip install pyqt5")
    os.system("zypper install xterm")
    print("İşlem tamamlandi!")

if dagitim == "3":
    os.system("apt update")
    os.system("apt install net-tools -y")
    os.system("apt install macchanger -y")
    os.system("apt install python3-pip")
    os.system("pip install pyqt5")
    os.system("apt install xterm -y")
    print("İşlem tamamlandi!")
if dagitim == "4":
    os.system("dnf upgrade --refresh")
    os.system("dnf install net-tools")
    os.system("dnf install net-tools-deprecated")
    os.system("dnf install macchanger")
    os.system("dnf install python3-pip")
    os.system("pip install pyqt5")
    os.system("apt install xterm -y")
    print("İşlem tamamlandi!")
