# *****************************************************	
# *****************Page Jaune Script*******************
# *****************************************************

#For the pages one, we can change, we can get the max pages on the first pages
#and create a loop
#the script get the informations on the first element on the first page
#create a loop to get the others 
pages_number = 1
url = "http://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=kebab&ou=paris&proximite=0&page="\
		+str(pages_number)

#We launch the html parser to get the soup
page_kebab = requests.get(url)
soup = BeautifulSoup(page_kebab.text, 'html.parser') 


#we get the name information with two class web
name = soup.find_all(class_="visible-phone mob-zone-pro pj-lb pj-link")[0]\
			.find_all(class_="not-visible")[0].text.replace("\n","").split(" ")

#we clean the name information, delete white space and the number ranking
idx = [name[i] for i in range(len(name)) if name[i].isdigit()==False and name[i]!=""]
name = (" ").join(idx)

#We get the information adress
adress = soup.find_all(class_="adresse-container")[0].text.replace("\n","").split(" ")
#Clean the information 
res = [adress[i]   for i in range(len(adress)) if adress[i]!=""]
adress = (" ").join(res)