#!/usr/bin/env python3

import bs4
import sys

def process(content):
    document = bs4.BeautifulSoup(content)

    for style in document.select('style'):
        # split by lines
        lines = [ l.strip() for l in style.text.split('\n') ]
        # remove empty lines
        lines = [ l for l in lines if l ]
        # remove style element
        style.decompose()

        for l in lines:
            if l[-1] == '{': # start
                selector = l[:-1].strip()
                body = []
            elif l[-1] == '}': # end
                l = l[:-1].strip()
                if l: body.append(l)
                body = ' '.join(body)

                for elem in document.select(selector):
                    try: origin = elem['style'] + ' '
                    except: origin = ''
                    elem['style'] = origin + body
            else:
                body.append(l)

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
    result = process(content)
    open(output_file, 'w').write(result)

if __name__ == '__main__':
    main(sys.argv)
