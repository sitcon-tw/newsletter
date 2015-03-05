#!/usr/bin/env python3

import bs4
import sys
import os

__all__ = [
    'strip_css_comment',
    'apply_inline_css',
    'process_html_content',
    'inline_html_file'
]

def strip_css_comment(style_content):
    'strip comment in css'
    while True:
        comment_start = style_content.find('/*')
        comment_end = style_content.find('*/')
        if comment_start == -1 or comment_end == -1:
            break
        style_content = (style_content[:comment_start] +
                         style_content[comment_end+2:])
    return style_content

def apply_inline_css(document, style_content):
    'spread css to every element'
    style_content = strip_css_comment(style_content)
    # split by lines
    lines = [ l.strip() for l in style_content.split('\n') ]
    # remove empty lines
    lines = [ l for l in lines if l ]

    for l in lines:
        if l[-1] == '{': # start
            selectors = [ s.strip() for s in l[:-1].split(',') ]
            body = []
        elif l[-1] == '}': # end
            l = l[:-1].strip()
            if l: body.append(l)
            body = ' '.join(body)

            for selector in selectors:
                for elem in document.select(selector):
                    # try append to exists style
                    try: origin = elem['style'] + ' '
                    except: origin = ''
                    elem['style'] = origin + body
        else:
            body.append(l) # css content

def process_html_content(content):
    '''
    try to parse html content and do `apply_inline_css`

    *make sure that your current work directory is same as content*
    '''
    document = bs4.BeautifulSoup(content, 'html5')

    for link in document.select('link'):
        if link.get('rel') == 'stylesheet':
            filename = link.get('href', '')
            if filename.endswith('.css'):
                style_content = open(filename).read()
                apply_inline_css(document, style_content)
            link.decompose()

    for style in document.select('style'):
        apply_inline_css(document, style.text)
        # remove style element
        style.decompose()

    return str(document)

def inline_html_file(input_file, output_file):
    '''
    same as `process_html_content`, it deals with work directory automatically.
    '''
    content = open(input_file).read()
    cwd = os.getcwd()
    os.chdir(os.path.dirname(input_file))
    result = process_html_content(content)
    os.chdir(cwd)
    with open(output_file, 'w') as f:
        f.write(result)

def main(argv):
    if len(argv) < 3:
        print(
            'usage: {script} input.html output.html'.format(script = argv[0]),
            file = sys.stderr
        )
        exit(1)

    _, input_file, output_file, *_ = argv
    inline_html_file(input_file, output_file)

if __name__ == '__main__':
    main(sys.argv)
