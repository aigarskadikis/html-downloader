import sys
from mechanize import Browser
br = Browser()

br.set_handle_robots( False )
br.addheaders = [('User-agent', 'Firefox')]

url = str(sys.argv[1])
filename = str(sys.argv[2])

f = br.retrieve(url,filename)[0]

