<p align="center">
  <samp>
    <big><big><big>🍝 This code is 100% AI generated · Zero human 🍝</big></big></big><br>
    <small>(maybe a little bit of human)</small><br>
    <i>Code written by AI. Bugs retained by human.</i><br>
    <small>5 min coding, 2h compile errors, missed a semicolon.</small>
  </samp>
</p>

# MIO-KITCHEN-ARM64 #
> [!CAUTION]
> # [Your phone is about to stop being yours. ](https://keepandroidopen.org/)

![Banner](https://raw.githubusercontent.com/Alhkxsj/MIO-KITCHEN-ARM64/main/splash.png)
#### A Rom Tool Written in Python
##### The Best Free And Open Source Rom Tool For You
> [!CAUTION]
> Unauthorized commercial use prohibited
***

## Linux ARM64 Only!
> [!IMPORTANT]
> This is a fork of [MIO-KITCHEN-SOURCE](https://github.com/ColdWindScholar/MIO-KITCHEN-SOURCE)
> dedicated to **Linux ARM64 (aarch64)** only. We only maintain this platform.
> **Windows / macOS / x86_64 / loongarch64 are NOT supported here.**
> Use the [upstream](https://github.com/ColdWindScholar/MIO-KITCHEN-SOURCE) for those platforms.
>
> The full aarch64 toolchain is included: boot / super / ext4 / erofs / f2fs / payload
> unpack & repack all work out of the box.
> 19 native tools, including **MagiskBoot**, **delta_generator**,
> **mkfs.f2fs** / **sload.f2fs** / **cpio** / **simg2img** (complete vs upstream aarch64).

***
<details><summary><h2>Used Projects</h2></summary>

|         Name         | Used for                                      | Link                                                                                               |       Developer |
|:--------------------:|-----------------------------------------------|----------------------------------------------------------------------------------------------------|----------------:|
|       unpac_py       | unpack sprd pac file                          | [Click](https://github.com/affggh/unpac_py)                                                        |          Affggh |
|       fspatch        | patch file_config before unpack               | [Click](https://github.com/affggh/fspatch)                                                         |          Affggh |
|     Logo_dumper      | Unpack and Repack Xiaomi lOGO.IMG             | [Click](https://github.com/affggh/logo_dumper)                                                     |          Affggh |
| mtk-garbage-porttool | Support repack old android folder to img file | [Click](https://github.com/ColdWindScholar/mtk-garbage-porttool)                                   |          Affggh |
|   context_pacther    | Patch file_context before repacking           | [Click](https://github.com/ColdWindScholar/context_patch)                                          | ColdWindScholar |
|       lpunpack       | Unpack and parse Android Super Image          | [Click](https://github.com/unix3dgforce/lpunpack)                                                  |    unix3dgforce |
|    android-tools     | Repack Ext4 Image, Sparse Convertion, lpmake  | [Click](https://github.com/nmeum/android-tools)                                                    |           nmeum |
|       cpio_py        | unpack cpio and repack                        | [Click](https://github.com/ColdWindScholar/cpio_py)                                                | ColdWindScholar |
|     erofs-utils      | Unpack and repack Erofs Images                | [Click](https://github.com/sekaiacg/erofs-utils)                                                   |        sekaiacg |
|     make_ext4fs      | repack ext4 images for old devices            | [Click](https://github.com/anpaza/make_ext4fs)                                                     |          anpaza |
|         ext4         | parse and unpack Ext4 images                  | [Click](https://github.com/cubinator/ext4)                                                         |       cubinator |
|     Busybox_w64      | plugin support                                | [Click](https://frippery.org/busybox/)                                                             |     Ron Yorston |
|       Busybox        | Plugin Support                                | [Click](http://busybox.net/)                                                                       |   Erik Andersen |
|        brotli        | Unpack and repack .br files                   | [Click](https://github.com/google/brotli)                                                          |          Google |
|       sdat2img       | Convert dat to img                            | [Click](https://github.com/xpirt/sdat2img)                                                         |           xpirt |
|       img2sdat       | Convert img to sparse dat                     | [Click](https://github.com/xpirt/img2sdat)                                                         |           xpirt |
|       kdztools       | Unpack kdz and dz files                       | [Click](https://github.com/ehem/kdztools)                                                          |            ehem |
|         dtc          | Decompile and compile device trer files       | [Click](https://android.googlesource.com/platform/external/dtc/)                                   |    David Gibson |
|     oppo_decrypt     | Decrypt ozip and ofp                          | [Click](https://github.com/bkerler/oppo_decrypt)                                                   |         bkerler |
|      splituapp       | Parse and unpack UPDATE.APP file              | [Click](https://github.com/superr/splituapp)                                                       |          Superr |
|       libufdt        | Parse \ Unpack \ Repack Dtbo image            | [click](https://android.googlesource.com/platform/system/libufdt/)                                 |          Google |
|     ROMFS_PARSER     | Unpack Romfs files                            | [Click](https://github.com/ddddhm1234/ROMFS_PARSER/tree/main)                                      |       ddddhm123 |
|     Nh4RomTools      | Codes for disable vb                          | [Click](https://github.com/affggh/NH4RomTool)                                                      |          Affggh |
|         zstd         | Unpack and repack zstd files                  | [Click](https://github.com/facebook/zstd)                                                          |        facebook |
|       rsceutil       | Unpack and repack Rk resource images          | Inspired by [Rsce-go](https://github.com/Evsio0n/rsce-go)                                          | ColdWindScholar |
|      apftool-rs      | Unpack and repack RKFW and RKAF images        | [Click](https://github.com/suyulin/apftool-rs)                                                     |         suyulin |
|      aml_image       | Unpack Amlogic V2 images                      | [View Code](https://github.com/ColdWindScholar/MIO-KITCHEN-SOURCE/blob/main/src/core/aml_image.py) | ColdWindScholar |
* And other projects! Huge shout out to the developers! 
</details>

***

## Features
* Unpack `boot, dtbo, ext4, erofs, payload, logo` and so on
* Pack `boot, dtbo, ext4, erofs, logo` and so on
***
## Advantages
* Automatic fs_config and fs_context patch
* GUI graphical interface
* A graphical plugin manager, plus an editor for plugin script editing. Support plugin installing and exporting
* Quick updates, secure, stable and fast
* Unique MSH interpreter that supports running MSH scripts
* Provide backward compatibility with Android 8 and lower and create .img for these versions
* Use mkc file choose api on Linux, making it easier to use
***
## Supported Os

|   Os    | Arch    |
|:-------:|---------|
|  Linux  | arm64   |
## Supported Image Types
| Supported Image Types     |
|---------------------------|
| Android Boot Image        |
| Android Recovery Image    |
| Android Vendor_boot Image |
| Erofs                     |
| Ext4                      |
| F2fs(Linux Version)       |
| Romfs                     |
| Amlogic v2 image          |
| RockChip resource image   |
| Payload                   |
## Supported File Types
| Supported File Types |
|----------------------|
| Zip                  |
| Sprd PAC             |
| ops                  |
| Ozip                 |
| tar.md5              |
| kdz/dz               |
| ofp                  |
| tar.gz               |
## The MIO-KITCHEN Manager
>[!NOTE]
>Its a utils to manage MIO-KITCHEN tool.
<details><summary>Update Prebulit Binary</summary>

```` shell
python3 config upbin
````

</details>

<details><summary>Check If Supported My Machine</summary>

```` shell
python3 config chksupd
````

</details>


## Start To Use
> [!NOTE]
> Currently Only Support Python 3.8 and Newer!
### Prerequisites
<details><summary>Linux</summary>

```` shell
python3 -m pip install -U --force-reinstall pip
pip install -r requirements.txt
sudo apt update -y && sudo apt install -y python3-tk cpio f2fs-tools \
    python3-pil python3-pycryptodome python3-requests python3-pygments \
    python3-zstandard python3-asn1crypto python3-lxml python3-six python3-httpx \
    python3-cryptography python3-toml python3-lz4 python3-lzo python3-protobuf
pip install -r requirements.txt
````

If using NixOS

```` shell
nix-shell
````

</details>

### Get started
```` shell
python tool.py
# To create a binary distribution, you could:
python build.py
````
***
# Contact Us
***
### Developer's Email: 3590361911@qq.com
### QQ Group: 683828484
### Telegram Group: [Mio Android Kitchen Chat](https://t.me/mio_android_kitchen_group)
### Telegram Channel: [Mio Android Kitchen Updates](https://t.me/mio_android_kitchen)
***
# Contributors:
***
### [![contributors](https://contrib.rocks/image?repo=ColdWindScholar/MIO-KITCHEN-SOURCE&max=999&column=20)](https://github.com/ColdWindScholar/MIO-KITCHEN-SOURCE/graphs/contributors)
### Thanks to people like you for helping out!
***
# About
***
### MIO-KITCHEN
```
Always free, users first
Quality Tools, presented here!
Brought you by the MIO-KITCHEN-TEAM
```
#### ColdWindScholar (3590361911@qq.com) All Rights Reserved. ####
