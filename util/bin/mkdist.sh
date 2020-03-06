#! /bin/bash

set -e

version=$(./py-mkvenv --version | awk '{print $2}')
pyinstaller py-mkvenv.spec
mv ./dist/py-mkvenv ./dist/py-mkvenv-${version}
