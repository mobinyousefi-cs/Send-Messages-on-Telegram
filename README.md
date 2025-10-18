# Telegram Message Sender (Tkinter + Telethon)

Convert your Telegram account into a handy desktop tool to send messages quickly — via a clean Tkinter GUI or a CLI. Built with **Telethon** for Telegram API access and designed with a professional `src/` layout, tests, and CI.

---

## ✨ Features
- ✅ One‑time login flow using Telethon sessions (kept locally)
- 🖥️ GUI app (Tkinter) to send messages to users, groups, channels
- 🧪 Pytest test suite + GitHub Actions CI (Ruff + Black + Pytest)
- ⚙️ Config via `.env` (API keys) and sensible defaults
- 🧰 CLI utilities for login and scripted sending

---

## 🗂️ Project Structure
```
telegram-message-sender/
├─ src/
│  └─ telegram_sender/
│     ├─ __init__.py
│     ├─ config.py
│     ├─ client.py
│     ├─ gui.py
│     └─ main.py
├─ tests/
│  └─ test_config.py
├─ .github/workflows/ci.yml
├─ .editorconfig
├─ .gitignore
├─ LICENSE
├─ pyproject.toml
├─ requirements.txt
└─ README.md
```

---

## 🔐 Prerequisites
1. **Create a Telegram API App** at <https://my.telegram.org/apps> to get `API_ID` and `API_HASH`.
2. **Python 3.10+** installed.

> **Note for Tkinter**: On Linux, install Tkinter via your package manager (e.g. `sudo apt-get install python3-tk`). On Windows/macOS, it usually ships with Python.

---

## 🚀 Setup
```bash
# 1) Clone
git clone https://github.com/mobinyousefi-cs/telegram-message-sender.git
cd telegram-message-sender

# 2) Create & activate a virtual environment (recommended)
python -m venv .venv
# Windows: .venv\Scripts\activate
# Unix/Mac: source .venv/bin/activate

# 3) Install deps
pip install -r requirements.txt

# 4) Create .env
cp .env.example .env
# then edit .env and set API_ID, API_HASH, PHONE (optional)
```

### `.env` Example
```
API_ID=1234567
API_HASH=your_api_hash_here
PHONE=+981234567890
SESSION_NAME=telegram_sender
SESSION_DIR=
```
- `SESSION_DIR` is optional. When empty, a platform‑specific config dir is used.

---

## 🔑 One‑Time Login (creates local session)
Run the login command once to authenticate your account. You’ll receive a code in Telegram, then (if enabled) your 2FA password.

```bash
python -m telegram_sender login
```
This stores a session file (e.g. `telegram_sender.session`) in your config directory. The GUI and CLI can reuse it without asking for the code again.

---

## 🖥️ Start the GUI
```bash
python -m telegram_sender gui
```
- Enter recipient: a **username** (e.g., `@example_user`), or a **phone** (`+123...`), or **Saved Messages** (`me`).
- Type your message and click **Send**.

> If you haven’t logged in yet, you’ll be prompted to run the login command in your terminal.

---

## 🧰 CLI Usage
Send a message without opening the GUI:
```bash
python -m telegram_sender send \
  --to "@example_user" \
  --message "Hello from my Python sender!"
```
**Options**
```
usage: python -m telegram_sender {gui,login,send} [...]

commands:
  gui                 launch Tkinter app
  login               authenticate and create a session
  send                send a single message via CLI

send options:
  --to TEXT           username (@user), phone (+123...), or "me"
  --message TEXT      message to send
```

---

## 🧪 Tests
```bash
pytest -q
```
> Tests are isolated and don’t require real Telegram credentials.

---

## 🧹 Code Quality
- **Ruff**: Linting (fast)
- **Black**: Formatting
- **Pytest**: Unit tests

Run locally:
```bash
ruff check src tests
black --check src tests
pytest
```

---

## 📝 License
This project is licensed under the **MIT License**. See [LICENSE](./LICENSE).

---

## ❓ FAQ
**Q. Where is the session stored?**  
A. By default in a platform‑specific config directory (e.g., `~/.config/telegram_sender/` on Linux). You can override via `.env` → `SESSION_DIR`.

**Q. Can I send to groups/channels?**  
A. Yes — provide the public username (e.g., `@mygroup`). For private entities, ensure your account has access.

**Q. Does the GUI handle first‑time login?**  
A. For a clean UX, perform `python -m telegram_sender login` first. After that, GUI works seamlessly.

---

## 🔧 Troubleshooting
- `ModuleNotFoundError: No module named 'tkinter'` → install Tkinter for your OS.
- `ValueError: API_ID/API_HASH missing` → set them in `.env`.
- Network issues → ensure you can reach Telegram and aren’t behind a blocking firewall.

---

## 🙌 Credits
Author: **Mobin Yousefi** — <https://github.com/mobinyousefi-cs>

