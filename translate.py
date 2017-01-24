#!/usr/bin/env python3

import os
import requests
import sys

config_file = '.ya_token'

access_token = os.getenv('YANDEX_TRANSLATE_API_TOKEN')
if not access_token or len(access_token) == 0:
	try:
		f = open(config_file, 'r')
	except FileNotFoundError:
		home = os.path.expanduser("~")
		f = open(
			os.path.join(
				home,
				config_file
			),
			'r'
		)
	access_token = f.readline().strip()
detect_language_url = 'https://translate.yandex.net/api/v1.5/tr.json/detect?key={}'.format(
	access_token
)
translate_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key={}'.format(
	access_token
)
to_lang = sys.argv[1]
text = sys.argv[2]
detected_response = requests.get(detect_language_url+'&text='+text)
detected_lang = detected_response.json()['lang']
	
translation_response = requests.get(
	translate_url+'&text='+text+
	'&lang='+detected_lang+'-'+to_lang
)
for translated in translation_response.json()['text']:
	print(translated)

