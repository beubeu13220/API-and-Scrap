from lxml import html
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np 
import googlemaps

path_export = ""
# *****************************************************	
# ********************Google script********************
# *****************************************************
Keyword_search =""
key_google_api =  Token_Gooogle_API

#we launch connexion
gmaps = googlemaps.Client(key=key_google_api)

#We get the paris geocode location for the next step
#also the id location
geo_paris = gmaps.geocode("Paris")
location_id_paris = geo_paris[0].get("place_id")
location_cor_paris = geo_paris[0].get("geometry").get("location")

#with the geocode location we get the first page of paris kebab
#we init a large radius value, this value limit the distance from the original location
page = gmaps.places(Keyword_search,location_cor_paris,radius=10*1000)

#We obtain the first kebab result
#If we want other result we change 0 by other number
#This request has only 20 result, correspond to the first page search
page.get("results")[0]

adress = page.get("results")[0].get("formatted_address")
name = page.get("results")[0].get("name")
rating = page.get("results")[0].get("rating")
#We have only one result page, if we want the next page we need to capture the next token page
next_token = kebab_page.get("next_page_token")
#With the next token, we launch again the request and get the result page 2
test = gmaps.places(Keyword_search,cor,radius=10*1000,page_token=next_tok)

#optim
#create loop for browse all pages and add condition for stop to the end 
#also create a condition to confirm that the location is repected 
#because the radius is large

#example : first page extraction
#loop on first page
data_ = pd.DataFrame(index=np.arange(len(page.get("results"))), columns=["name","adress","rating"])

for i in range(len(page.get("results"))):
	#if we want clean the adrres, we can :
	#data.iloc[i,"adress"] = kebab_page.get("results")[i].get("formatted_address").split(",")[0]
	#data.iloc[i,"city"] = kebab_page.get("results")[i].get("formatted_address").split(",")[1]
	#data.iloc[i,"country"] = kebab_page.get("results")[i].get("formatted_address").split(",")[2]
	data.iloc[i,"adress"] = page.get("results")[i].get("formatted_address")
	data.iloc[i,"name"] = page.get("results")[i].get("name")
	data.iloc[i,"rating"] = page.get("results")[i].get("rating")

#Export en csv 
data.to_csv(path_export+"data.csv")





