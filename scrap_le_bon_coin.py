from lxml import html
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import json


"""Type de recherche (idtt): numerique (idtt=2)
    Location: 1
    Achat: 2

Localisation (ci): 1 ou plusieurs numerique separé par une virgule (ci=330192,330363)

Type de bien (idtypebien): 1 ou plus numerique separé par une virgule (idtypebien=1,2,3,4,6,7,8,9,11,12,13,14,15)
    Appartement: 1
    Maison / Villa: 2
    Parking / Box: 3
    Terrain: 4
    Boutique: 6
    Local Commercial: 7
    Bureaux: 8
    Loft / Atelier / Surface: 9
    Immeuble: 11
    Betiment: 12
    Chateau: 13
    Hotel particulier: 14
    Programme: 15
 """

regions = [
'Alsace',
'Aquitaine',
'Auvergne',
'Basse_Normandie',
'Bourgogne',
'Bretagne',
'Centre',
'Champagne_Ardenne',
'Corse',
'Franche_Comté',
'Haute Normandie',
'Ile-de-France',
'Languedoc-Roussillon',
'Limousin',
'Lorraine',
'Midi-Pyrénées',
'nord_pas_de_calais',
'pays_de_la_Loire',
'picardie',
'poitou-charentes',
'provence_alpes_cote_d_azur',
'rhone-alpes'
]


#region = ""
#bien = ""
url = "https://www.leboncoin.fr/ventes_immobilieres/offres/nord_pas_de_calais/?th=1&parrot=0"

text_lb = requests.get(url)
soup = BeautifulSoup(text_lb.text,  'html.parser')
	# On identifie la dernieère page
last_page = list(
	    map(lambda x: x['href'], soup.find_all("a", class_='list_item clearfix trackable')))



columns_name = ['region', 'prix', 'piece', 'mcare', 'price_care']
data_zoe = pd.DataFrame(columns=columns_name)

collect = dict()

for n_page in last_page:
	idx_price = None
	idx_piece = None
	idx_surface = None

	print(n_page)
	text_lb = requests.get("https:" + n_page)
	soup = BeautifulSoup(text_lb.text,  'html.parser')

	for i in range(len(soup.find_all(class_='property'))):
		if soup.find_all(class_='property')[i].text == "Prix":
			idx_price = i
		if soup.find_all(class_='property')[i].text =="Pièces":
			idx_piece = i  
		if soup.find_all(class_='property')[i].text =="Surface":
			idx_surface = i
	
		price = soup.find_all(class_='value')[idx_price].text.replace(
	        "\xa0", "").replace("\n", "").replace(" ", "").replace("€","")

		piece = soup.find_all(class_='value')[idx_piece].text.replace(
	        "\xa0", "").replace("\n", "").replace(" ", "")
		mcare = soup.find_all(class_='value')[idx_surface].text.replace(
	        "\xa0", "").replace("\n", "").replace(" ", "").split("m")[0]

		price_care = float(price)/float(mcare)

		
		value_return = {'region':"Nord", 'prix':float(price), 'piece':piece,\
		'mcare':float(mcare), 'price_care':price_care}

		data_zoe.append(value_return,ignore_index=True)