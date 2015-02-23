#!/usr/bin/env python3

import re
import sys

VERBOSE = False

__all__ = [
    'remotify_resource_file',
    'replace_processor_url',
    'replace_processor_src'
]

def remotify_resource_file(remote_base_url, file_name, output_file):
    '''read file and change assets url'''
    def replace_processor_url(match):
        url = match.group(1)
        if VERBOSE: print('url::Origin: ' + url)
        if not url.startswith("http"):
            url = remote_base_url + url
        if VERBOSE: print('url::Remote: ' + url)
        return "url('%s')" % url
    def replace_processor_src(match):
        url = match.group(1)
        if VERBOSE: print('src::Origin: ' + url)
        if not url.startswith("http"):
            url = remote_base_url + url
        if VERBOSE: print('src::Remote: ' + url)
        return 'src="%s"' % url

    content = open(file_name).read()
    content = re.sub('url\([\'"]([^\']*)[\'"]\)', replace_processor_url, content)
    content = re.sub('src="([^"]*)"', replace_processor_src, content)
    open(output_file, 'w').write(content)
    return True

def main(argv):
    global VERBOSE

    if len(argv) < 4:
        print('''\
Usage: {} remote_base_url file-in file-out [options...]

    options:
        -v, --verbose   Output more message
'''.format(argv[0]), file = sys.stderr
        )
        exit(1)

    _, remote_base_url, file_in, file_out, *args = argv

    if remote_base_url[-1] != '/':
        remote_base_url += '/'

    if '-v' in args or '--verbose' in args:
        VERBOSE = True
        print('VERBOSE: ON')

    remotify_resource_file(remote_base_url, file_in, file_out)

if __name__ == '__main__':
    main(sys.argv)
