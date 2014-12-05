# Emoji 拼音输入法扩展

Emoji 拼音输入法扩展，可用于 [Google 拼音](http://www.google.com/intl/zh-CN/ime/pinyin/) 或 [ibus-libpinyin](https://github.com/epico/ibus-libpinyin)。

该项目可以使用 OS X 10.10 中的`/usr/share/mecabra/zh/common/emoji.plist`生成 Lua 扩展。

# 使用指南

## 生成扩展

1. 安装 pip3
2. `sudo pip3 install -r requirements.txt`
3. `python3 generator.py /usr/share/mecabra/zh/common/emoji.plist`
