import json
import requests
import shutil
import os

if not os.path.exists('imagenes'):
	os.mkdir('imagenes')

URL = 'http://es.wikieducator.org/api.php?action=query&list=allimages&aiuser=Deleyva&aisort=timestamp&ailimit=500&format=json'

r = requests.get(URL)

imagenes = json.loads(r.text)

for im in imagenes['query']['allimages']:
	url = im.get('url')
	nombre = im.get('name')
	response = requests.get(url, stream=True)
	with open('imagenes/' + nombre, 'wb') as out_file:
	    shutil.copyfileobj(response.raw, out_file)
	del response
