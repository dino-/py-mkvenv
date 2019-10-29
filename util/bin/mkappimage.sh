#! /bin/bash

set -e

cp --recursive util/resources/AppDir .
pyinstaller --noconfirm py-mkvenv.spec
cp --recursive dist/py-mkvenv AppDir/usr/share
linuxdeploy-x86_64.AppImage --appdir=AppDir --output=appimage
