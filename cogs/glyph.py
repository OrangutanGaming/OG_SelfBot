from discord.ext import commands
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Glyph():
    def __init__(self, bot):
        self.bot = bot

    def enterCode(self, code):
        try:
            driver = webdriver.Firefox()
            driver.get(f"https://www.warframe.com/promocode?code={code}")
            elem = driver.find_element_by_name("code")
            elem.send_keys(Keys.RETURN)
            assert "already been redeemed" not in driver.page_source
            assert "please try again" not in driver.page_source
            # Check if page is now success page (https://www.warframe.com/redeem_success?item={})
            driver.close()
            return True
        except AssertionError:
            return False

    async def on_message(self, message):
        content = message.content
        try: x = re.findall(r"([A-Z0-9]{4})-([A-Z0-9]{4})-([A-Z0-9]{4})-([A-Z0-9]{4})", content)
        except IndexError:
            return
        fullCode=[]
        for code in x:
            for fragment in code:
                fullCode.append(fragment)
            final = final + "-".join(fullCode)
        for code in x:
            if self.enterCode(code):
                await self.bot.get_channel(315579438563852289)\
                    .send(f"{self.bot.user.mention} Success! Used code `{code}`!")

def setup(bot):
    bot.add_cog(Glyph(bot))