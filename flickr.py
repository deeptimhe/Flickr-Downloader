import flickrapi
import urllib2
import os


"""
Author: Tim He
Date: 2017-09-26
Usage:
1. Install flickrapi, urllib2: e.g., sudo pip install flickrapi urllib2 (linux)
2. Sign up and log in: www.flickr.com
3. Create an app: https://www.flickr.com/services/apps/create/noncommercial/?
   Make up app name and building, submit, get api_key and api_secret
4. Set params

Note:
1. If you cannot open flickr.com, please download and install lantern first: https://github.com/getlantern/forum/issues/833
   Open lantern, then close it, and open: www.flickr.com
2. This program will make a directory with the name same as 'tag' param, then download pictures into this directory.
3. Please record your tag and taken_date.
"""

# ---------------------------------------------------
# Params
api_key = u'xxxxx'
api_secret = u'xxx'
tag = ''  # example: people
min_taken_date = ''  # example: 2017-09-24
max_taken_date = ''  # example: 2017-09-25
# ---------------------------------------------------


save_dir = tag + '_' + min_taken_date + '_' + max_taken_date
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
flickr = flickrapi.FlickrAPI(api_key, api_secret)
extras = 'url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
for photo in flickr.walk(
        tag_mode='all',
        tags=tag,
        min_taken_date=min_taken_date,
        max_taken_date=max_taken_date,
        extras=extras):
    url_o = photo.get('url_o')
    if url_o is not None:
        pic = urllib2.urlopen(url_o).read()
        img_file = open(os.path.join(save_dir, url_o.split('/')[-1]), 'wb')
        img_file.write(pic)
        img_file.close()
