#!/usr/bin/env bash

remote_base_url="http://sitcon.org/newsletter"

if [ -z "$1" ]; then
    echo "Usage: $0 target-folder [remote-base-url]" >&2
    exit 1
fi

if [ -n "$2" ]; then
    remote_base_url="$2"
    if [ "${remote_base_url: -1}" = "/" ]; then
        remote_base_url="${remote_base_url:0: -1}"
    fi
fi

target="$1"

if [ "${target: -1}" = "/" ]; then
    target="${target:0: -1}"
fi

if [ "${target:0:1}" = "/" ]; then
    target="${target:1}"
fi

echo "Remote Assets URL = ${remote_base_url}/${target}/"

mkdir build
cp -R ${target}/* build/
./utilities/inline_css.py build/index.html build/index.html
./utilities/remotify_resource.py "${remote_base_url}/${target}/" build/index.html build/index.html -v
mv build/index.out.html build/index.html
