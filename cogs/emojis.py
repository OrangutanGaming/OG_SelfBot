lenny = "( ͡° ͜ʖ ͡°)"
fight = "(ง⚆ᨎ⚆)ง"
"(ง⚆ᗜ⚆)ง"
approve = "ಠ_ಠ"
cool = "(⌐■_■)"

dir = dir()
rEmojis = []
for emoji in dir:
    if not emoji.startswith("__"):
        rEmojis.append(emoji.title())
emojis = "`{}`".format("`, `".join(rEmojis))
