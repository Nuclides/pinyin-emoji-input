# Pinyin Emoji Input

Emoji input extension for [Google Pinyin](http://www.google.com/intl/zh-CN/ime/pinyin/) / [ibus-libpinyin](https://github.com/epico/ibus-libpinyin).

On OS X 10.10, there is a emoji data file located at `/usr/share/mecabra/zh/common/emoji.plist`, you can generate the extension from that file. The file is copyrighted by Apple, use at your own risk.

# Usage

1. Install pip3
2. `sudo pip3 install -r requirements.txt`
3. `python3 generator.py /usr/share/mecabra/zh/common/emoji.plist`
