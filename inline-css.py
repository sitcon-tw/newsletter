#!/usr/bin/env python3

import bs4
import sys
import os

def strip_css_comment(style_content):
    while True:
        comment_start = style_content.find('/*')
        comment_end = style_content.find('*/')
        if comment_start == -1 or comment_end == -1:
            break
        style_content = (style_content[:comment_start] +
                         style_content[comment_end+2:])
    return style_content

def apply_inline_css(document, style_content):
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

def process(content):
    document = bs4.BeautifulSoup(content)

    for link in document.select('link'):
        try: filename = link['href']
        except: filename = ''
        if filename.endswith('.css'):
            style_content = open(filename).read()
            apply_inline_css(document, style_content)

    for style in document.select('style'):
        apply_inline_css(document, style.text)
        # remove style element
        style.decompose()

    return document.prettify()

def main(argv):
    if len(argv) < 3:
        print(
            'usage: {script} input.html output.html'.format(script = argv[0]),
            file = sys.stderr
        )
        exit(1)

    _, input_file, output_file, *_ = argv
    content = open(input_file).read()
    cwd = os.getcwd()
    os.chdir(os.path.dirname(input_file))
    result = process(content)
    os.chdir(cwd)
    open(output_file, 'w').write(result)

if __name__ == '__main__':
    main(sys.argv)
