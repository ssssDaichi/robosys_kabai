#!/usr/bin/python3

# SPDX-FileCopyrightText: 2024 Daichi Hirose
# SPDX-License-Identifier: MIT

import subprocess

def test_square_number():
    # echoコマンドで5を出力し、それをスクリプトに渡す
    result = subprocess.run(["python3", "square_number.py"], input="5", capture_output=True, text=True)
    # 出力結果を確認
    assert result.stdout.strip() == "25.0"  # 期待される出力が"25.0"であることを確認

