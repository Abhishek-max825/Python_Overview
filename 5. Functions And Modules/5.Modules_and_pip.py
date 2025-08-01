# Two types of modules in python
# --> Built in modules
# --> User defined modules
# List of all the modules in python :- https://docs.python.org/3/py-modindex.html
import math
import os
import Userdefined_Function as udf
import requests

print(math.sqrt(16))
udf.hello()# User defined module usage
r = requests.get(url="https://www.google.com") # it will fetch the html code of google.com
print(r.text)

