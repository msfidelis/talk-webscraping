from bs4 import BeautifulSoup
import urllib2

link = "https://br.udacity.com/courses/all/"

request_headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "http://thewebsite.com",
    "Connection": "keep-alive" 
}

request = urllib2.Request(link, headers=request_headers)
html = urllib2.urlopen(request).read()

print html
