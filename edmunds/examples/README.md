###THE EDMUNDS API PYTHON WRAPPER IS UNDER DEVELOPMENT!

#Edmunds API Python Wrapper Examples

#Contents
1. Media: Photos Example

##1. Media: Photos

This example has two functions, `get_style_id` which returns a style ID for a given make, model, and year,
and `get_photos` which returns a dict of lists of photo URLs for a given style ID. 
The main function is an example of getting photos for the 2013 Tesla Model S.
The endpoints used in this example are [Get Style Details For a Car Make/Model/Year](http://developer.edmunds.com/api-documentation/vehicle/spec_model_year/v2/02_year_details/api-description.html) and 
[Media: Photos](http://developer.edmunds.com/api-documentation/vehicle/media_photos/v1/index.html).

####Usage
```python
>>> python media_photos.py
{(u'exterior', u'FBDG'): 
  [u'http://media.ed.edmunds-media.com/tesla/model-s/2012/oem/2012_tesla_model-s_sedan_signature_fbdg_oem_2_396.jpg', u'http://media.ed.edmunds-media.com/tesla/model-s/2012/oem/2012_tesla_model-s_sedan_signature_fbdg_oem_2_87.jpg', ..., u'http://media.ed.edmunds-media.com/tesla/model-s/2012/oem/2012_tesla_model-s_sedan_signature_fbdg_oem_2_131.jpg'],
 (u'exterior', u'FQ'): 
  [u'http://media.ed.edmunds-media.com/tesla/model-s/2012/oem/2012_tesla_model-s_sedan_signature_fq_oem_17_300.jpg', u'http://media.ed.edmunds-media.com/tesla/model-s/2012/oem/2012_tesla_model-s_sedan_signature_fq_oem_17_175.jpg', ..., u'http://media.ed.edmunds-media.com/tesla/model-s/2012/oem/2012_tesla_model-s_sedan_signature_fq_oem_18_2048.jpg'],
 ...
}
```
Note: '...' indicates more data removed here for clarity.
