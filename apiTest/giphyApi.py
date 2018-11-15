
import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
try:
    from apiTest.authorizationkey import *
except:
    from authorizationkey import *

api_instance = giphy_client.DefaultApi()


def searchGif(term):
    try:
        api_response = api_instance.gifs_translate_get(giphy_api_key, term)
        return(api_response.data.images.downsized.url)
    except ApiException as e:
        print("Can't find....")


if __name__ == '__main__':
    print(searchGif('兔 跳舞'))
