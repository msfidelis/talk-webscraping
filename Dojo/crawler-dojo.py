import urllib2
from bs4 import BeautifulSoup 

url = "http://cidades.ibge.gov.br/xtras/home.php"

links = set()



def listarhtml(link):
	try:
		html = urllib2.urlopen(link).read()
		a = BeautifulSoup(html, "html.parser")

		for estado in a.findAll("li"):
			try:

				if estado.a["href"] not in links:
					novoEstado = "%s/%s"%(url,estado.a["href"].strip())
					# print novoEstado
					# http://cidades.ibge.gov.br/xtras/uf.php?lang=&coduf=12&search=acre
					# http://cidades.ibge.gov.br/xtras/home.php/../xtras/uf.php?lang=_EN&coduf=17&search=tocantins

					novoEstado = novoEstado.replace("/xtras/home.php/..", "")
					print novoEstado
					links.add(estado.a["href"])
					listarhtml(novoEstado)
				
			except Exception as e:
				pass 

	except Exception as e:
		print e
		pass

listarhtml(url)
