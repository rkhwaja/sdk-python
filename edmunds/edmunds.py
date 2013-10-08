"""
Edmunds.com API Python wrapper
Edmunds API Documentation: http://developer.edmunds.com/

author: Michael Bock <mbock@edmunds.com>
version: 0.0.1
"""

import requests
from types import StringType

class Edmunds:
	"""
	The Edmunds API wrapper class
	"""
	
	BASE_URL = 'https://api.edmunds.com'
	BASE_MEDIA = 'http://media.ed.edmunds-media.com'

	def __init__(self, key):
		"""
		Constructor for Edmunds class

		:param key: Edmunds API key
		:type key: str
		"""
		if not isinstance(key, StringType):
			raise Exception('key not a StringType; class not instantiated')
		self.parameters = {'api_key' : key, 'fmt': 'json'}

	def make_call(self, endpoint, **kwargs):
		"""
		example calls:
		>>> make_call('/v1/api/vehiclephoto/service/findphotosbystyleid', comparator='simple', styleId='3883')
		>>> make_call('/api/vehicle/v2/lexus/rx350/2011/styles')

		Info about **kwargs: http://stackoverflow.com/questions/1769403/understanding-kwargs-in-python

		:param endpoint: Edmunds API endpoint, e.g. '/v1/api/vehiclephoto/service/findphotosbystyleid' or '/api/vehicle/v2/lexus/rx350/2011/styles'
		:type endpoint: str
		:param kwargs: List of extra parameters to be put into URL query string, e.g. view='full' or comparator='simple', styleId='3883'
		:type kwargs: List of key=value pairs, where the value is a str
		:returns: API response
		:rtype: JSON object
		"""
		# assemble url and queries
		payload = dict(self.parameters.items() + kwargs.items())
		url = self.BASE_URL + endpoint
		# make request
		r = requests.get(url, params=payload)
		return r.json()
