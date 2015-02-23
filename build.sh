#!/usr/bin/env bash

if [ -z "$1" ]; then
    echo "Usage: $0 target-folder" >&2
    exit 1
fi

target="$1"

if [ "${target: -1}" = "/" ]; then
    target="${target:0: -1}"
fi

if [ "${target:0:1}" = "/" ]; then
    target="${target:1}"
fi

mkdir build
cp -R ${target}/* build/
./remotify-resoure.py "http://sitcon.org/newsletter/${target}/" build/index.html
./inline-css.py build/index.out.html build/index.html
rm build/index.out.html
