###THE EDMUNDS API PYTHON WRAPPER IS UNDER DEVELOPMENT!

#Edmunds API Python Wrapper

This is an awesome Python wrapper for the [Edmunds.com API](http://developer.edmunds.com/api-documentation/overview/index.html).
The Edmunds.com API provides automative data including [vehicle specs](http://developer.edmunds.com/api-documentation/vehicle/), 
[pricing](http://developer.edmunds.com/api-documentation/vehicle/price_tmv/v1/), [media](http://developer.edmunds.com/api-documentation/vehicle/media_photos/v1/), 
[reviews](http://developer.edmunds.com/api-documentation/vehicle/content_ratings_and_reviews/v2/), and more. 
There are also Edmunds API endpoints for [dealership information](http://developer.edmunds.com/api-documentation/dealer/) 
and [Edmunds editorial content](http://developer.edmunds.com/api-documentation/editorial/).

##Usage
Enter your [Edmunds API key](http://edmunds.mashery.com/member/register/):
```python
from edmunds import Edmunds
api = Edmunds('YOUR API KEY')
```

Make API calls to any endpoint, get a JSON object returned.
For example, get the [style details](http://developer.edmunds.com/api-documentation/vehicle/spec_style/v2/01_by_mmy/api-description.html) 
for the 2011 Lexus RX 350:
```python
>>> response = api.make_call('/api/vehicle/v2/lexus/rx350/2011/styles')
>>> response
{u'styles': [{u'id': 101353967,
   u'make': {u'id': 200001623, u'name': u'Lexus', u'niceName': u'lexus'},
   u'model': {u'id': u'Lexus_RX_350',
    u'name': u'RX 350',
    u'niceName': u'rx-350'},
   u'name': u'4dr SUV (3.5L 6cyl 6A)',
   u'submodel': {u'body': u'SUV', u'modelName': u'RX 350 SUV'},
   u'trim': u'Base',
   u'year': {u'id': 100533091, u'year': 2011}},
  {u'id': 101353968,
   u'make': {u'id': 200001623, u'name': u'Lexus', u'niceName': u'lexus'},
   u'model': {u'id': u'Lexus_RX_350',
    u'name': u'RX 350',
    u'niceName': u'rx-350'},
   u'name': u'4dr SUV AWD (3.5L 6cyl 6A)',
   u'submodel': {u'body': u'SUV', u'modelName': u'RX 350 SUV'},
   u'trim': u'Base',
   u'year': {u'id': 100533091, u'year': 2011}}],
 u'stylesCount': 2}
```

Get [photos](http://developer.edmunds.com/api-documentation/vehicle/media_photos/v1/) 
for the style ID 3883 (1990 Honda Civic 2dr Hatchback):
```python
>>> response = api.make_call('/v1/api/vehiclephoto/service/findphotosbystyleid', comparator='simple', styleId='3883')
>>> response
[{u'authorNames': [u'American Honda Motor Company, Inc.'],
  u'captionTranscript': u'1991 Honda Civic 2 Dr Si Hatchback',
  u'photoSrcs': [u'/honda/civic/1991/oem/1991_honda_civic_2dr-hatchback_si_fq_oem_1_131.jpg',
   u'/honda/civic/1991/oem/1991_honda_civic_2dr-hatchback_si_fq_oem_1_396.jpg',
   u'/honda/civic/1991/oem/1991_honda_civic_2dr-hatchback_si_fq_oem_1_300.jpg',
   u'/honda/civic/1991/oem/1991_honda_civic_2dr-hatchback_si_fq_oem_1_400.jpg',
   u'/honda/civic/1991/oem/1991_honda_civic_2dr-hatchback_si_fq_oem_1_500.jpg',
   u'/honda/civic/1991/oem/1991_honda_civic_2dr-hatchback_si_fq_oem_1_185.jpg',
   u'/honda/civic/1991/oem/1991_honda_civic_2dr-hatchback_si_fq_oem_1_175.jpg',
   u'/honda/civic/1991/oem/1991_honda_civic_2dr-hatchback_si_fq_oem_1_196.jpg',
   u'/honda/civic/1991/oem/1991_honda_civic_2dr-hatchback_si_fq_oem_1_423.jpg',
   u'/honda/civic/1991/oem/1991_honda_civic_2dr-hatchback_si_fq_oem_1_276.jpg',
   u'/honda/civic/1991/oem/1991_honda_civic_2dr-hatchback_si_fq_oem_1_87.jpg',
   u'/honda/civic/1991/oem/1991_honda_civic_2dr-hatchback_si_fq_oem_1_150.jpg',
   u'/honda/civic/1991/oem/1991_honda_civic_2dr-hatchback_si_fq_oem_1_98.jpg'],
  u'shotTypeAbbreviation': u'FQ',
  u'subType': u'exterior',
  u'type': u'PHOTOS'}]
```

##Requirements

The Edmunds API Python wrapper requires the amazing [requests library](http://docs.python-requests.org/en/latest/).
Here are the [installation instructions](http://docs.python-requests.org/en/latest/user/install/#install) and the
[source code](https://github.com/kennethreitz/requests/).

##Issues

Please submit any problems, requests, and comments [here](https://github.com/EdmundsAPI/sdk-python/issues).

##License
TBD
