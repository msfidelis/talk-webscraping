from bs4 import BeautifulSoup
import urllib, urllib2

link = "http://www.magazineluiza.com.br/"

response = urllib2.urlopen(link).read()

soup = BeautifulSoup(response, "html.parser");

pages = set()
emails = set()

def getLinks(url):
    global pages

    response = urllib2.urlopen(url).read();
    soup = BeautifulSoup(response, "html.parser")
    
    for link in soup.findAll("a"):
        
        try:
            #Evitando links repetidos
            if link["href"] not in pages:
                print link.get_text() + " - " + link["href"]        
                pages.add(link["href"])

        except:
            pass

def crawler(inicial):
    global pages 
    pages.add(inicial)

    for page in pages:
        getLinks(page)


crawler(link)

    
