# 构建指南 (Linux ARM64)

## 1. 安装依赖

```bash
# Debian/Ubuntu 系统依赖
sudo apt install -y python3-tk cpio f2fs-tools android-sdk-libsparse-utils \
    python3-pil python3-pycryptodome python3-requests python3-pygments \
    python3-zstandard python3-asn1crypto python3-lxml python3-six python3-httpx \
    python3-cryptography python3-toml python3-lz4 python3-lzo python3-pip

# pip 依赖
pip install --break-system-packages -r requirements.txt

# C 扩展 (CPB 格式解包, 可选)
pip install --break-system-packages src/c_extension/cpb_file
```

> 其他发行版请用对应包管理器安装同名依赖 (Arch: `pacman -S`, Fedora: `dnf install`)。

## 2. 运行

```bash
python3 tool.py
```

## 3. 打包 deb

```bash
bash packaging/debian/build-deb.sh
# 产物: mio-kitchen_4.2.0_arm64.deb
```

## 4. 自检

```bash
python3 -m src.tool_tester
```
