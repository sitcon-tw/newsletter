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
    def replace_processor_href(match):
        url = match.group(1)
        if VERBOSE: print('href::Origin: ' + url)
        if not url.startswith("http") and not url.startswith('mailto:'):
            url = remote_base_url + url
        if VERBOSE: print('href::Remote: ' + url)
        return 'href="%s"' % url
    def meta_tag(match):
        url = match.group(1)
        if VERBOSE: print('meta::Origin: ' + url)
        if not url.startswith("http"):
            url = remote_base_url + url
        if VERBOSE: print('meta::Remote: ' + url)
        return '<meta content="%s" property="og:url" />' % url
    def replace_background(match):
        url = match.group(1)
        if url and url[0] != '#':
            if VERBOSE: print('meta::Origin: ' + url)
            if not url.startswith("http"):
                url = remote_base_url + url
            if VERBOSE: print('meta::Remote: ' + url)
        return 'background="%s"' % url

    content = open(file_name).read()
    content = re.sub('url\([\'"]([^\']*)[\'"]\)', replace_processor_url, content)
    content = re.sub('src="([^"]*)"', replace_processor_src, content)
    content = re.sub('href="([^"]*)"', replace_processor_href, content)
    content = re.sub('<meta\s+content="([^"]*)"\s+property="og:url"\s*/?>', meta_tag, content)
    content = re.sub('<meta\s+property="og:url"\s+content="([^"]*)"\s*/?>', meta_tag, content)
    content = re.sub('background="([^"]+)"', replace_background, content)
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
