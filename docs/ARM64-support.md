# ARM64 (aarch64) 支持说明

本仓库为 MIO-KITCHEN 的 Linux ARM64 专属版。

## 工具链现状

`bin/Linux/aarch64/` 共 19 个工具，全部可用：

| 工具 | 来源 | 说明 |
|---|---|---|
| afptool, delta_generator, dtc, e2fsdroid, extract.erofs, img2simg, imgkit, lpmake, magiskboot, make_ext4fs, mke2fs, mkfs.erofs, brotli, busybox, zstd | 官方仓库自带 | 大多数为 NDK 静态链接 |
| cpio, mkfs.f2fs, sload.f2fs, simg2img | 发行版补入 | 动态链接, 需系统库 (见下) |

上游 aarch64 目录缺失 4 个工具, 本仓库已补齐:
- `cpio` (boot ramdisk 解/打包) — GNU cpio, 仅依赖 libc
- `mkfs.f2fs` / `sload.f2fs` (f2fs 分区打包) — f2fs-tools, 依赖 libuuid/libblkid/libselinux
- `simg2img` (sparse 合并) — 依赖 android libsparse (Debian/Ubuntu 包: android-sdk-libsparse-utils)

> 注: `extract.f2fs` 未补 — f2fs 解包走 `imgkit`, 该二进制运行时不引用。

## 运行时系统依赖 (各发行版自行安装)

Debian/Ubuntu:
```bash
sudo apt install -y python3-tk cpio f2fs-tools python3-pil python3-pycryptodome \
    python3-requests python3-pygments python3-zstandard python3-asn1crypto \
    python3-lxml python3-six python3-httpx python3-cryptography python3-toml \
    python3-lz4 python3-lzo android-sdk-libsparse-utils
```

Python pip 依赖 (apt 没有的):
```bash
pip install -r requirements.txt
```

## 启动

```bash
python3 tool.py          # 需 X11 或 Wayland+XWayland 图形环境
```

构建 deb 包见 `packaging/debian/`。
