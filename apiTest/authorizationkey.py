import os
import urllib.parse as urlparse

try:
    from apiTest.envvarrr import *
except:
    try:
        from envvarrr import *
    except:
        dburl = urlparse.urlparse(os.environ['DATABASE_URL'])
        # == for LineBotApi ==
        LineBotApiKey = os.environ['LineBotApiKey']
        LineBothandler = os.environ['LineBothandler']
        # == for weatherkey ==
        weatherKey = os.environ['weatherKey']
        # giphy api
        giphy_api_key = os.environ['giphy_api_key']  # str | Giphy API Key.
        # TRA api key
        TRAapp_id = os.environ['TRAapp_id']
        TRAapp_key = os.environ['TRAapp_key']
