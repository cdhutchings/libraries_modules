# External Packages

# Must be installed in order to use them
# They can be found on pypi.org etc.
# Looking at the package "Requests"

# Install using pip or your interpreter

import requests

# This package makes http requests

sparta_homepage = requests.get("https://www.spartaglobal.com/")

# This command returns the html of the page in question
#print(sparta_homepage.content)

# And to return headers, for instance
# These are metadata from the site which are not normally shown on the webpage
print(sparta_homepage.headers)