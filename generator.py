# -*- coding: utf-8 -*-
import sys
import plistlib
from pypinyin import lazy_pinyin
from jinja2 import Environment, FileSystemLoader


def get_readings(word, data):
    if 'readings' in data:
        return ''.join(i for i in data['readings'] if not i.isdigit())
    else:
        return ''.join(lazy_pinyin(word))


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        emoji = plistlib.readPlist(path)
        words = {}
        template_name = 'template.lua'
        env = Environment(loader=FileSystemLoader("./"), trim_blocks=True)
        template = env.get_template(template_name)

        for word, data in emoji.items():
            reading = get_readings(word, data)
            if reading not in words:
                words[reading] = set()
            words[reading] = words[reading] | set(data['emoji'])

        with open('emoji.lua', 'w') as f:
            f.write(template.render(words=words))
    else:
        print('Please input path to emoji plist.')

if __name__ == '__main__':
    main()
