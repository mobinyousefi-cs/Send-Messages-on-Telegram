#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Telegram Message Sender
File: test_config.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-18
Updated: 2025-10-18
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
Basic tests for configuration loading. Does not require real Telegram credentials.
"""
from __future__ import annotations

import os
from pathlib import Path

import pytest

from telegram_sender.config import Settings


def test_default_session_dir_is_path():
    p = Settings.default_session_dir()
    assert isinstance(p, Path)


def test_load_from_env(tmp_path, monkeypatch):
    monkeypatch.setenv("API_ID", "12345")
    monkeypatch.setenv("API_HASH", "hash")
    monkeypatch.setenv("SESSION_DIR", str(tmp_path))

    s = Settings.load()
    assert s.api_id == 12345
    assert s.api_hash == "hash"
    assert s.session_dir == tmp_path
    assert s.session_path().name == f"{s.session_name}.session"


def test_missing_keys_raises(monkeypatch):
    for k in ("API_ID", "API_HASH"):
        if k in os.environ:
            monkeypatch.delenv(k, raising=False)
    with pytest.raises(ValueError):
        Settings.load()
