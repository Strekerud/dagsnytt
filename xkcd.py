import requests
import cStringIO
from PIL import Image
from xml.etree import ElementTree

def retrieve_image_for_today():
    api_url = "https://www.xkcd.com/rss.xml"
    response = requests.get(api_url)

    #print response.content

    tree = ElementTree.fromstring(response.content)

    content = [(item.find('description').text.encode('utf-8')) for item in tree.findall('./channel/item')][0]

    return content.split("\"")[1]

def show_image(url):
    response = requests.get(url)
    file = cStringIO.StringIO(response.content)
    img = Image.open(file)
    img.show()

def show_todays_xkcd():
    show_image(retrieve_image_for_today())
