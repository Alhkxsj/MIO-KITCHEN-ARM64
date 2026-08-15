#!/bin/bash
# MIO-KITCHEN ARM64 一键启动脚本
# 用法:
#   ./start.sh           启动 Xvnc(端口5900) + MIO-KITCHEN GUI
#   ./start.sh --novnc   不启动 VNC, 仅在本机显示(需已有 DISPLAY)
cd "$(dirname "$0")"

if [ "$1" != "--novnc" ] && ! pgrep -x Xvnc > /dev/null; then
    if [ ! -f /root/.vncpasswd ]; then
        echo "123456" | vncpasswd -f > /root/.vncpasswd
        chmod 600 /root/.vncpasswd
    fi
    echo "[*] Starting Xvnc on :99, VNC port 5900 (密码: 123456)"
    Xvnc :99 -rfbport 5900 -geometry 1280x800 -depth 24 \
        -SecurityTypes VncAuth -PasswordFile /root/.vncpasswd \
        > /tmp/xvnc.log 2>&1 &
    sleep 2
fi
export DISPLAY=:99
echo "[*] Starting MIO-KITCHEN 4.2.0 (ARM64)..."
exec python3 tool.py
