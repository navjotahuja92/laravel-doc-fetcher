from bs4 import BeautifulSoup
import urllib2

f = open('urls.txt','w+')

response = urllib2.urlopen('http://laravel.com/docs/5.0')
soup = BeautifulSoup(response.read())

UrlsHTML = soup.find("section",{ 'class' : 'sidebar'})
 
uls = UrlsHTML.select('a')

f.write('http://laravel.com/docs/5.0' + '\n')
for item in uls:
	f.write('http://laravel.com' + item.get('href') + '\n')

f.close() 