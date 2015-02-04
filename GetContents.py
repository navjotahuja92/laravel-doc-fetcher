from bs4 import BeautifulSoup
import urllib2

# Create a logger object.
import logging
logger = logging.getLogger('your-module')

# Initialize coloredlogs.
import coloredlogs
coloredlogs.install(level=logging.DEBUG)

f = open('urls.txt','r+')
outFile = open('output.html','w+')

url_list = f.read().splitlines()
outFile.write('<html><head></title> laravel Documentation</title>')
outFile.write('<link rel="stylesheet" href="style.css" /> </head>')
outFile.write('<body style="margin:15%; width:70%; ">')
for url in url_list:
	logging.warn('Reading : ' + url)
	response = urllib2.urlopen(url)
	soup = BeautifulSoup(response.read())
	content_html = soup.find("div",{ 'id' : 'docs-content'})
	# print(content_html)
	outFile.write(content_html.encode("utf-8"))
	# Correct Links content_html.replace('="/docs"','http://laravel.com/docs')
	logging.debug('Writing Done :-) ')
outFile.write('</body>')
outFile.write('</html>')