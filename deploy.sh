#/usr/bin/env bash

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

echo "Pack files..."
tar -C build -zcvf "/tmp/${target}.build.tar.gz" .

echo "Switch branch..."
git checkout gh-pages

echo "Unpack files..."
tar -C "${target}" -zxvf "/tmp/${target}.build.tar.gz"

echo "Commit files..."
git add "${target}"
git commit -m "Update ${target}"

echo "Done! Please check files and you can push now..."
