import ctypes
import os
import shutil
import urllib.request

from slugify import slugify


def between(data, here, there):
    data = str(data)
    needle = data.find(here)
    if needle != -1:
        length = data.find(there, needle + len(here))
        return data[needle + len(here):length]
    else:
        return None


URL = 'https://www.nationalgeographic.com/photography/photo-of-the-day/'
LOCATION = os.environ['USERPROFILE'] + '\\wp-natgeo\\'

# First get data from the picture of the day page which is not the actual image

with urllib.request.urlopen(URL) as response:
    html = str(response.read())

# Scrub the data returned for the location of the actual image
pic_url = between(html, '<meta property="og:image" content="', '"')

if pic_url is not None:
    # Picture exists
    title = between(html, '<meta property="og:title" content="', '"')

    # Get the title for the filename and to see if we have downloaded it before
    filename = LOCATION + slugify(title) + '.jpg'
    if not os.path.exists(filename):

        # Make directories if they are not there
        if not os.path.exists(LOCATION):
            os.makedirs(LOCATION)

        # Download and save picture
        with urllib.request.urlopen(pic_url) as response:
            with open(filename, 'wb') as file:
                shutil.copyfileobj(response, file)

    cs = ctypes.c_wchar_p(filename)
    ret = ctypes.windll.user32.SystemParametersInfoW(0x0014, 0, cs, 0)
