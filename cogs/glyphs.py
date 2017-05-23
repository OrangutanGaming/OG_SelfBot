from imgurpython import ImgurClient
import SelfIDs
import re

album = "http://imgur.com/a/emJbN"
albumID = re.findall(r"imgur.com/a/(\w+)", album)[0]

client = ImgurClient(SelfIDs.imgur_clientID, SelfIDs.imgur_Secret)

albumObj = client.get_album(albumID)
albumPics = client.get_album_images(albumID)

glyphs = {}

for pic in albumPics:
    glyphs[pic.description] = pic.link