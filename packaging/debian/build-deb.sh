#!/bin/bash
# 从本仓库构建 mio-kitchen deb 包 (Linux ARM64)
set -e
cd "$(dirname "$0")/../.."
ROOT="$(pwd)"
PKG=/tmp/mio-kitchen-pkg
rm -rf "$PKG" && mkdir -p "$PKG/opt" "$PKG/DEBIAN" "$PKG/usr/bin" \
    "$PKG/usr/share/applications" "$PKG/usr/share/icons/hicolor/256x256/apps"

# 源码 + 工具链 (排除 .git / 无头残留)
cp -a "$ROOT" "$PKG/opt/mio-kitchen"
rm -rf "$PKG/opt/mio-kitchen/.git" "$PKG/opt/mio-kitchen/docs" "$PKG/opt/mio-kitchen/packaging"
find "$PKG/opt/mio-kitchen" -name __pycache__ -type d -exec rm -rf {} + 2>/dev/null

# C 扩展 (如已编译)
if [ -f /usr/local/lib/python3*/dist-packages/cpb_file*.so ]; then
    cp /usr/local/lib/python3*/dist-packages/cpb_file*.so "$PKG/opt/mio-kitchen/"
fi

# 启动器
cat > "$PKG/usr/bin/mio-kitchen" <<SH
#!/bin/bash
cd /opt/mio-kitchen
python3 -c "import sv_ttk, chlorophyll, future" 2>/dev/null || \
    python3 -m pip install --break-system-packages --quiet sv-ttk chlorophyll future "protobuf>=7" 2>/dev/null
[ -n "\$DISPLAY" ] || { echo "[错误] 需要 X11 或 Wayland+XWayland 图形环境 (DISPLAY 为空)"; exit 1; }
exec python3 tool.py
SH
chmod 755 "$PKG/usr/bin/mio-kitchen"

# 桌面入口 + 图标
cp "$PKG/opt/mio-kitchen/bin/kemiaojiang.png" "$PKG/usr/share/icons/hicolor/256x256/apps/mio-kitchen.png"
cat > "$PKG/usr/share/applications/mio-kitchen.desktop" <<DESK
[Desktop Entry]
Type=Application
Name=MIO-KITCHEN
Comment=Android ROM image unpack/repack kitchen
Exec=/usr/bin/mio-kitchen
Icon=mio-kitchen
Terminal=false
Categories=Utility;
DESK

# control
VERSION=$(grep "^version" "$PKG/opt/mio-kitchen/bin/setting.ini" | cut -d= -f2 | tr -d " ")
cat > "$PKG/DEBIAN/control" <<CTRL
Package: mio-kitchen
Version: $VERSION
Section: utils
Priority: optional
Architecture: arm64
Maintainer: MIO-KITCHEN-ARM64 Project
Depends: cpio, f2fs-tools, python3 (>= 3.8), python3-tk, python3-pil, python3-lz4,
 python3-cryptography, python3-lxml, python3-requests, python3-zstandard,
 python3-toml, python3-pygments, python3-pycryptodome, python3-httpx,
 python3-asn1crypto, python3-six, python3-lzo, python3-pip
Description: MIO-KITCHEN ARM64 - Android image unpack/repack tool
 GUI kitchen for unpacking/repacking Android boot/super/ext4/erofs/f2fs
 images. Requires X11 or Wayland with XWayland.
CTRL
cat > "$PKG/DEBIAN/postinst" <<POST
#!/bin/bash
set -e
python3 -m pip install --break-system-packages --quiet \
    sv-ttk chlorophyll future "protobuf>=7" 2>/dev/null || true
chmod -R a+rX /opt/mio-kitchen 2>/dev/null || true
exit 0
POST
chmod 755 "$PKG/DEBIAN/postinst"

dpkg-deb --build --root-owner-group "$PKG" "$(dirname "$0")/mio-kitchen_${VERSION}_arm64.deb"
echo "构建完成: packaging/debian/mio-kitchen_${VERSION}_arm64.deb"
