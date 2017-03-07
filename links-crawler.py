from bs4 import BeautifulSoup
import urllib, urllib2

link = "http://www.magazineluiza.com.br/"

pages = set()

#Retorna o parsing do BeautifulSoup
def getData(link):
    response = urllib2.urlopen(link).read();
    return BeautifulSoup(response, "html.parser")

#Pega os Links - Com recursão
def getLinks(url):
    global pages

    data = getData(url)

    for link in data.findAll("a"):
        
        try:
            #Evitando links repetidos
            if link["href"] not in pages:
                print link.get_text() + " - " + link["href"]        
                pages.add(link["href"])
                getLinks(link["href"])

        except:
            pass

getLinks(link)

    
