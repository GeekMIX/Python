# use pip

# downloading a package is very easy.
# open the command line interface and tell pip to download the package you want.
# > pip install camelcase 


# using a package you have installed
# import the "camelcase" package into your project

import camelcase

c = camelcase.CamelCase()

txt = "sfsello 11World"

print(c.hump(txt))




