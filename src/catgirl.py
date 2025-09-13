import requests
import urllib.parse as rp
import json

class CatgirlDownloaderAPI:
	def __init__(self):
		self.endpoint = "https://derpibooru.org/api/v1/json/search/images"
		self.query = "cute, score.gte:200, -changeling, -irl, pony, -animated, -screencap, -text, -comic, -meme, -dialogue, -3d, -monochrome, -sketch, -human, -*anthro, -interspecies, -oc"
		self.per_page = 1
		self.sort = "random"

	def get_page(self, nsfw = False):
		try:
			if nsfw:
				filter_id = 56027
			else:
				filter_id = 209452

			params = rp.urlencode({"q":self.query, "filter_id":filter_id, "per_page":self.per_page, "sf":self.sort})
			r = requests.get(self.endpoint + "?" + params, timeout=10)
			if r.status_code == 200:
				return r.text
			else:
				return None
		except Exception as e:
			print(e)
			return None

	def get_page_url(self, response):
		data = json.loads(response)
		self.info = data
		return data['images'][0]['representations']['full']

	def get_neko(self, nsfw=False):
		return self.get_page_url(self.get_page(nsfw))

	def get_image(self, url):
		r = requests.get(url, timeout=20)
		return r.content
