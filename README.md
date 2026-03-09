<p align="center">
	<img src="https://github.com/user-attachments/assets/b91f259f-baa6-4907-9a9d-bf6ed89f1131">
</p>

# 🔥 Overview
**ClipTyper** — Paste anywhere, even when clipboard sharing is disabled.\
A lightweight utility that simulates keyboard strokes to paste clipboard content into applications where standard copy-paste functionality is restricted.


## 📖 Description

ClipTyper is a simple GUI application designed to bypass clipboard restrictions in remote or restricted environments. Instead of relying on the system clipboard, it reads your local clipboard content and simulates real-time keystrokes (typing) into the active window.

This makes it ideal for scenarios where:
*   Clipboard redirection is disabled.
*   You are managing a server console without GUI access.

## ✨ Features

*   **Clipboard Simulation:** Reads your local clipboard and types character-by-character.
*   **Visual Feedback:** A countdown timer shows progress while typing.
*   **Error Handling:** Checks for empty clipboards or excessively long text (max 100k chars).
*   **Lightweight GUI:** Built with `wxPython`, delivering a native look and feel without the overhead of an Electron app.
*   **Cross-Platform:** Works on Windows, Linux, and macOS also should work.

## 🛠️ Use Cases

ClipTyper is particularly useful in environments where clipboard synchronization is disabled or unavailable:

| Environment | Scenario | Benefit |
| :--- | :--- | :--- |
| **KVM Consoles** | noVNC, Proxmox, IPMI/iDRAC | Type commands directly into the console. |
| **Remote Desktop** | RDP / VNC (No Clipboard Sync) | Paste data without needing clipboard forwarding. |
| **Virtual Machines** | VirtualBox / VMware (Guest isolation) | Bypass VM guest OS restrictions. |
| **CLI Interfaces** | PuTTY, Tera Term, Serial Console | Simulate input for command-line tools. |
| **Legacy Apps** | Old Windows/DOS applications | Works where modern clipboard APIs fail. |
| **Security Kiosks** | Secure terminals / Restricted PCs | Bypass security policies blocking paste. |

## 📦 Installation

### Prerequisites
* Python 3.9 or higher is recommended.
* On Linux: `xclip` package is required.

### Dependencies
You can install the required libraries using:

```bash
pip install -r requirements.txt
```

### Running the Application
Simply run the script in your terminal:

```bash
python ClipTyper.py
```

## 🚀 Usage

1.  **Open ClipTyper:** Run the application.
2.  **Prepare Clipboard:** Copy the text you wish to paste (Ctrl+C).
3.  **Click Button:** Click **"Paste by typing."** in the window.
4.  **Wait:** After pressing the button, a timer will appear. This will wait 3 seconds before pasting the clipboard content.
5.  **Done:** Once finished, the button re-enables for future use.

If you want to stop the program even when it's writing, just close it.

## ⚙️ Configuration & Limitations

*   **Text Length Limit:** Currently limited to **100,000 characters**. Attempting to paste more will trigger an error dialog.
*   **Display Server:** On Linux/Mac, ensure you have the correct display server running as `wxPython` requires one.

## 🛠️ Troubleshooting

| Issue | Solution |
| :--- | :--- |
| **"Error accessing clipboard"** | Ensure no other application is locking the clipboard. |
| **Window doesn't appear** | On Linux, ensure `DISPLAY` environment variable is set correctly (e.g., `export DISPLAY=:0`). |
| **Antivirus blocks execution** | Some AVs flag `pyautogui` and `nuitka`. Add an exception or whitelist the program folder. |
