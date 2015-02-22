#!/usr/bin/env python3

import re
import sys

def process(file_name, output_file, remote_base_url):
    def replace_processor_url(match):
        url = match.group(1)
        if not url.startswith("http"):
            url = remote_base_url + url
        return "url('%s')" % url
    def replace_processor_src(match):
        url = match.group(1)
        if not url.startswith("http"):
            url = remote_base_url + url
        return 'src="%s"' % url

    content = open(file_name).read()
    content = re.sub('url\(\'([^\']*)\'\)', replace_processor_url, content)
    content = re.sub('src="([^"]*)"', replace_processor_src, content)
    open(output_file, 'w').write(content)
    return True

def main(argv):
    if len(argv) < 3:
        print(
            'Usage: {} remote_base_url file1 [file2] ...'.format(argv[0]),
            file = sys.stderr
        )
        exit(1)

    _, remote_base_url, *files = argv
    if remote_base_url[-1] != '/':
        remote_base_url += '/'
    for f in files:
        *p, ext = f.split('.')
        out = '.'.join(p) + '.out.' + ext
        result = process(f, out, remote_base_url)
        print('File {filename} ... {status}'.format(
            filename = f,
            status = 'OK' if result else 'Failed'
            ))

if __name__ == '__main__':
    main(sys.argv)
