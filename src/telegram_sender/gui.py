#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Telegram Message Sender
File: gui.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-18
Updated: 2025-10-18
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
Tkinter GUI for sending Telegram messages using an existing Telethon session.

Usage:
python -m telegram_sender gui
"""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass

from .config import Settings
from .client import send_message


@dataclass
class GUIState:
    to: tk.StringVar
    message: tk.StringVar


class TelegramSenderApp(ttk.Frame):
    def __init__(self, master: tk.Tk, settings: Settings) -> None:
        super().__init__(master, padding=16)
        self.settings = settings
        self.state = GUIState(to=tk.StringVar(value="@"), message=tk.StringVar())
        self._build_ui()

    def _build_ui(self) -> None:
        self.master.title("Telegram Message Sender")
        self.master.geometry("520x280")
        self.grid(sticky="nsew")

        for i in range(3):
            self.columnconfigure(i, weight=1)
        self.rowconfigure(3, weight=1)

        ttk.Label(self, text="Recipient (username / +phone / me):").grid(row=0, column=0, sticky="w")
        entry_to = ttk.Entry(self, textvariable=self.state.to)
        entry_to.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0, 8))

        ttk.Label(self, text="Message:").grid(row=2, column=0, sticky="w")
        txt = ttk.Entry(self, textvariable=self.state.message)
        txt.grid(row=3, column=0, columnspan=3, sticky="ewns")

        btn_send = ttk.Button(self, text="Send", command=self.on_send)
        btn_send.grid(row=4, column=2, sticky="e", pady=(12, 0))

        self.master.bind("<Return>", lambda _e: self.on_send())

    def on_send(self) -> None:
        to = self.state.to.get().strip()
        msg = self.state.message.get().strip()

        if not to:
            messagebox.showwarning("Validation", "Please enter a recipient (e.g., @user, +123, or 'me').")
            return
        if not msg:
            messagebox.showwarning("Validation", "Please enter a message.")
            return

        try:
            send_message(self.settings, to=to, message=msg)
        except Exception as exc:  # pragma: no cover - GUI runtime errors
            messagebox.showerror(
                "Error",
                f"Failed to send message.\n\n{exc}\n\nIf this is a new setup, run:\npython -m telegram_sender login",
            )
            return

        messagebox.showinfo("Success", "Message sent ✔")
        self.state.message.set("")


def run_gui(settings: Settings) -> None:
    root = tk.Tk()
    # Optional: use themed widgets
    try:
        root.call("tk", "scaling", 1.2)
    except Exception:
        pass

    app = TelegramSenderApp(root, settings)
    root.mainloop()
