#!/bin/env python3

import bs4
import time
import json
import random
import string
import os, sys
import requests
import collections
import urllib.request
from bs4 import BeautifulSoup

raw_tags = []
tag_lis = []

useragent = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7']

	
class extra():

	def tiny_url(url):
		apiurl = "http://tinyurl.com/api-create.php?url="
		tinyurl = requests.get(apiurl + url)
		return tinyurl.text

	def write(in_text):
		for char in in_text:
			time.sleep(0.1)
			sys.stdout.write(char)
			sys.stdout.flush()

	def extract_hash_tags(stri): 
		return list(part[1:] for part in stri.split() if part.startswith('#'))


class main1():

	def __init__(self, user):
		self.user = user
		self.get_profile()

	def get_profile(self):
		if bs4.__version__ == '4.6.0':
			pass
		else:
			print(f"\n[!] currunt verion of bs4 module isn't supported \n[+] Downgrading beautifulsoup")
			os.system("python3 -m pip install beautifulsoup4==4.6.0")
			os.execv('main.py', sys.argv)
			
		extra.write(f"\ngetting profile ...")
		profile = requests.get(f"https://www.instagram.com/{self.user}", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'})
		soup = BeautifulSoup(profile.text, 'html.parser')
		more_data = soup.find_all('script', attrs={'type': 'text/javascript'})
		self.data = json.loads(more_data[3].get_text()[21:].strip(';'))
		self.p_data = self.data['entry_data']['ProfilePage'][0]['graphql']['user']
		self.output = {
			"username": str(self.p_data['username']),
			"name": str(self.p_data['full_name']),
			"url": str(f"instagram.com/{self.p_data['username']}"),
			"followers": str(self.p_data['edge_followed_by']['count']),
			"following": str(self.p_data['edge_follow']['count']),
			"posts": str(self.p_data['edge_owner_to_timeline_media']['count']),
			"bio": str(self.p_data['biography'].replace('\n', ', ')),
			"external url": str(self.p_data['external_url']),
			"private": str(self.p_data['is_private']),
			"verified": str(self.p_data['is_verified']),
			"profile pic url": extra.tiny_url(str(self.p_data['profile_pic_url_hd'])),
			"business account": str(self.p_data['is_business_account']),
			"connected to fb": str(self.p_data['connected_fb_page']),
			"joined recently": str(self.p_data['is_joined_recently']),
		
		}

		if str(self.output['private']).lower() == 'true':
			print(f"[!] private profile can't scrap data !\n")
			return 1
		else:
			for index, post in enumerate(self.p_data['edge_owner_to_timeline_media']['edges']):
				try:
					raw_tags.append(extra.extract_hash_tags(post['node']['edge_media_to_caption']['edges'][0]['node']['text']))
				except IndexError:
					pass
			x = len(raw_tags)
			for i in range(x):
				tag_lis.extend(raw_tags[i])
			self.tags = dict(collections.Counter(tag_lis))

		return self.tags
		return self.output

	

	def print_data(self):
		for key, value in self.output.items():
			print(f"{key+(17-len(key))*' '} : {value}")	


