lenny = "( ͡° ͜ʖ ͡°)"
fight = "(ง º  ͜ʖ º )ง"
fight2 = "(ง⚆ᗜ⚆)ง"
fight3 = "(ง⚆ᨎ⚆)ง"
approve = "ಠ_ಠ"
cool = "(⌐■_■)"
happy = "^‿^"
mouse = "ʢ◉ᴥ◉ʡ"
arrow = "⤜(ʘ_ʘ)⤏"
hug = "(づ◔ ͜ʖ◔)づ"
hug2 = "(づ｡◕‿‿◕｡)づ"
dog = "(⚆ᴥ⚆)"
fireworks = "(∩*ヮ*)⊃━☆ﾟ.*"
smile = "◕ ◡ ◕"
embarrassed = "⊙﹏⊙"
surprised = "( ﾟoﾟ)"
ballin = "ヘ(◕。◕ヘ)"
stare = "◉_◉"
stare2 = "๏_๏"
stop = "╚(•⌂•)╝"
oo="•ﺑ•"
oo2="‹•.•›"
fyou = "ಠ︵ಠ凸"
potter = "ϟ"
needle = "┣▇▇▇═───────────"
injured = "(///_ಥ)"
pucker = "(ﾟ＊ﾟ)"
blush = "(｡･_･｡)"
happy2 = "(ﾟヮﾟ)"
ha = "(´▽`)"
silly = ":^Þ"

dir = dir()
rEmojis = []
for emoji in dir:
    if not emoji.startswith("__"):
        rEmojis.append(emoji.title())
rEmojis = "`{}`".format("`, `".join(rEmojis))

emojis = []
for emoji in dir:
    if not emoji.startswith("__"):
        emojis.append(emoji)
emojis = "`{}`".format("`, `".join(emojis))