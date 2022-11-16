#### tamilgram ####
import re
import os
from shortzy import shortzy

##

SHORTENER_WEBSITE_API = os.environ.get("SHORTENER_WEBSITE_API")
SHORTENER_WEBSITE = os.environ.get("SHORTENER_WEBSITE")

##
async def get_shortlink(url):
    if SHORTENER_WEBSITE_API and SHORTENER_WEBSITE:
        shortzy = Shortzy(SHORTENER_WEBSITE_API, SHORTENER_WEBSITE)
        return await shortzy.convert(url)
