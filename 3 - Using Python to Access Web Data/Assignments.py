# # Assignment: Finding Numbers in a Haystack
# import re
# handle = open('regex_sum_907674.txt')
# soma = 0

# for line in handle:
#     line = line.rstrip()
#     strNumbers = re.findall('[0-9]+', line)
#     if len(strNumbers) < 1 : continue
#     fltNumbers = [float(i) for i in strNumbers]
#     #print(fltNumbers)
#     #print(sum(fltNumbers))
#     soma += sum(fltNumbers)

# print(soma)
################################################################################
# # Assignment: Exploring the HyperText Transport Protocol
# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')

# mysock.close()
################################################################################
# # Assignment: Scraping Numbers from HTML using BeautifulSoup
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# #url = input('Enter - ')
# url = 'http://py4e-data.dr-chuck.net/comments_907676.html'
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the span tags
# tags = soup('span')
# soma = list()
# for tag in tags:
#     #print('TAG:', tag)
#     #print('URL:', tag.get('href', None))
#     soma.append(float(tag.contents[0]))
#     #print('Contents:', tag.contents[0])
#     #print('Attrs:', tag.attrs)

# print('Count', len(soma))
# print(sum(soma))
################################################################################
# # Assignment: Following Links in HTML Using BeautifulSoup
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# #url = input('Enter URL: ')
# url = 'http://py4e-data.dr-chuck.net/known_by_Divya.html'
# #url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html' #sample data
# count = int(input('Enter count: '))
# position = int(input('Enter position: '))

# print('Retrieving: ', url)
# for i in range(count):
#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')

#     # Retrieve all of the anchor tags
#     tags = soup('a')
#     url = tags[position-1].get('href', None)
#     # for tag in tags:
#     #     print(tag.get('href', None))
#     print('Retrieving: ', url)
################################################################################
# # Assignment: Extracting Data from XML
# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET
# import ssl

# api_key = False
# # If you have a Google Places API key, enter it here
# # api_key = 'AIzaSy___IDByT70'
# # https://developers.google.com/maps/documentation/geocoding/intro

# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/xml?' 
# else :
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# # address = 'http://py4e-data.dr-chuck.net/comments_907678.xml'
# # address = 'http://py4e-data.dr-chuck.net/comments_42.xml'  #sample data

# while True:
#     soma = 0
#     address = input('Enter location: ')
#     if len(address) < 1: break

#     # parms = dict()
#     # parms['address'] = address
#     # if api_key is not False: parms['key'] = api_key
#     # url = serviceurl + urllib.parse.urlencode(parms)
#     url = address
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)

#     data = uh.read()
#     print('Retrieved', len(data), 'characters')
#     # print(data.decode())
#     tree = ET.fromstring(data)

#     counts = tree.findall('.//count')
#     print('Count: ', len(counts))
#     for item in counts:
#         soma += float(item.text)
#         # print(item.text)
#     print('Sum: ', soma)
#     # results = tree.findall('result')
#     # lat = results[0].find('geometry').find('location').find('lat').text
#     # lng = results[0].find('geometry').find('location').find('lng').text
#     # location = results[0].find('formatted_address').text

#     # print('lat', lat, 'lng', lng)
#     # print(location)
################################################################################
# # Assignment: Extracting Data from JSON
# import urllib.request, urllib.parse, urllib.error
# import ssl
# import json

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter location: ')
# # url = 'http://py4e-data.dr-chuck.net/comments_42.json' #sample data
# # url = 'http://py4e-data.dr-chuck.net/comments_907679.json'

# print('Retrieving', url)
# connection = urllib.request.urlopen(url, context=ctx)
# data = connection.read()
# print('Retrieved', len(data), 'characters')
# data = data.decode()
# # print(data)

# # data = '''
# # [
# #   { "id" : "001",
# #     "x" : "2",
# #     "name" : "Chuck"
# #   } ,
# #   { "id" : "009",
# #     "x" : "7",
# #     "name" : "Brent"
# #   }
# # ]'''

# info = json.loads(data)
# print('User count:', len(info["comments"]))

# soma = 0 
# for item in info["comments"]:
#     # print('Name', item['name'])
#     # print('Id', item['id'])
#     # print('Attribute', item['x'])
#     soma += item['count']

# print('Sum: ', soma)
################################################################################
# Assignment: Using the GeoJSON API
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # print(json.dumps(js, indent=4))

    # lat = js['results'][0]['geometry']['location']['lat']
    # lng = js['results'][0]['geometry']['location']['lng']
    # print('lat', lat, 'lng', lng)
    # location = js['results'][0]['formatted_address']
    # print(location)
    place_id = js['results'][0]['place_id']
    print('Place id', place_id)