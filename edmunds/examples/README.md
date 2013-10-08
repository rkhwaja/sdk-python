###THE EDMUNDS API PYTHON WRAPPER IS UNDER DEVELOPMENT!

#Edmunds API Python Wrapper Examples

#Contents
* Media: Photos Example

##Media: Photos

This example has two functions, `get_style_id` which returns a style ID for a given make, model, and year,
and `get_photos` which returns a dict of lists of photo URLs for a given style ID.

####Usage
```python
>>> python media_photos.py
{(u'exterior',
  u'FBDG'): [u'http://media.ed.edmunds-media.com/tesla/model-s/2012/oem/2012_tesla_model-s_sedan_signature_fbdg_oem_2_396.jpg', u'http://media.ed.edmunds-media.com/tesla/model-s/2012/oem/2012_tesla_model-s_sedan_signature_fbdg_oem_2_87.jpg', ..., u'http://media.ed.edmunds-media.com/tesla/model-s/2012/oem/2012_tesla_model-s_sedan_signature_fbdg_oem_2_131.jpg'],
 (u'exterior',
  u'FQ'): [u'http://media.ed.edmunds-media.com/tesla/model-s/2012/oem/2012_tesla_model-s_sedan_signature_fq_oem_17_300.jpg', u'http://media.ed.edmunds-media.com/tesla/model-s/2012/oem/2012_tesla_model-s_sedan_signature_fq_oem_17_175.jpg', ..., u'http://media.ed.edmunds-media.com/tesla/model-s/2012/oem/2012_tesla_model-s_sedan_signature_fq_oem_18_2048.jpg'],
  ...
}
```
Note: '...' indicates more data removed here for clarity.
