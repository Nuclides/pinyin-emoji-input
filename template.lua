-- encoding: UTF-8

------------------------------------------------------------------------------
-- Emoji 输入法
-- 作者: LIU Dongyuan <liu.dongyuan@gmail.com>, CAO Shan <c.svenjax@gmail.com>
------------------------------------------------------------------------------

local PINYIN_EMOJI = {
{% for word in words %}
  ["{{ word }}"] = {{ words[word] }},
{% endfor %}
}

function emojiInput(arg)
  return PINYIN_EMOJI[arg]
end

------------

ime.register_command("em", "emojiInput", "Emoji", "none", "请输入 Emoji 描述")

