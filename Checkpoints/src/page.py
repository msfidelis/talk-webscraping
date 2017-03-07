# -*- coding: UTF-8 -*-


class Page(object):
    
    def __init__(self, link):
        self._link = link

    def get_data(self):
        from bs4 import BeautifulSoup
        import urllib2
        
        response = urllib2.urlopen(self._link).read();
        return BeautifulSoup(response, "html.parser")

    def parser(self):
        self._soup = get_data()       

    @property
    def links(self):
        return self._links

    @property
    def emails(self):
        return self._emails
