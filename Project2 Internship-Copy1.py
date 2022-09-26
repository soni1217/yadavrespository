#!/usr/bin/env python
# coding: utf-8

# In[82]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[83]:


from bs4 import BeautifulSoup
import requests


# In[84]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[78]:


page


# In[5]:


soup = BeautifulSoup(page.content)
soup


# In[6]:


heading_tags = ['h1','h2','h3']
for tags in soup.find_all(heading_tags):
    print(tags.name + '->' + tags.text.strip())


# In[7]:


#Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
#and make data frame


# In[8]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[9]:


page = requests.get('http://www.imdb.com/chart/top')


# In[10]:


page


# In[11]:


soup = BeautifulSoup(page.content,"html.parser")
print(soup.prettify())


# In[12]:


#scrap movie name
scraped_movies=soup.find_all('td',class_='titleColumn')
scraped_movies


# In[13]:


#parse movie name with realsing dates
movies=[]
for movie in scraped_movies:
    movie=movie.get_text().replace('\n',"")
    movie=movie.strip("")
    movies.append(movie)
movies


# In[14]:


#scrap rating for movies
scraped_ratings=soup.find_all('td',class_='ratingColumn imdbRating')
scraped_ratings


# In[15]:


#parse ratings
ratings=[]
for rating in scraped_ratings:
    rating=rating.get_text().replace('\n',"")
    rating=rating.strip("")
    ratings.append(rating)
ratings


# In[16]:


#store the scraped data
data=pd.DataFrame()
data['Movie Names','Year']=movies
data['Ratings']=ratings
data.head()


# In[ ]:





# In[17]:


#Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of
#release) and make data frame


# In[18]:


page = requests.get('https://www.imdb.com/india/top-rated-indian-movies/')


# In[19]:


page


# In[20]:


soup = BeautifulSoup(page.content,"html.parser")
print(soup.prettify())


# In[21]:


#scrap movie name
scraped_movies=soup.find_all('td',class_='titleColumn')
scraped_movies


# In[22]:


#parse movie name with realsing dates
movies=[]
for movie in scraped_movies:
    movie=movie.get_text().replace('\n',"")
    movie=movie.strip("")
    movies.append(movie)
movies


# In[23]:


#parse ratings
ratings=[]
for rating in scraped_ratings:
    rating=rating.get_text().replace('\n',"")
    rating=rating.strip("")
    ratings.append(rating)
ratings


# In[24]:


data=pd.DataFrame()
data['Movie Names','Year']=movies
data['Ratings']=ratings
data.head()


# In[ ]:





# In[25]:


#Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) 
#from https://presidentofindia.nic.in/former-presidents.ht


# In[26]:


page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')


# In[27]:


page


# In[28]:


soup = BeautifulSoup(page.content,"html.parser")
print(soup.prettify())


# In[29]:


#scrap former president  name
scraped_names=soup.find_all('div',class_='presidentListing')
scraped_names


# In[30]:


#parse former president  name with tenor year with term of office
names=[]
for name in scraped_names:
    name=name.get_text().replace('\n',"",)
    name=name.strip("")
    names.append(name)
names


# In[ ]:





# In[31]:


#Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape


# In[32]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')

page


# In[ ]:





# In[33]:


#Top 10 ODI teams in men’s cricket along with the records for matches, points and rating


# # teams

# In[34]:


soup = BeautifulSoup(page.content)
soup


# In[35]:


first_team = soup.find('span',class_ = "u-hide-phablet")
first_team


# In[36]:


first_team.text


# In[37]:


match = soup.find('td',class_ = 'rankings-block__banner--matches')


# In[38]:


match.text


# In[39]:


point = soup.find('td',class_ = "rankings-block__banner--points")

point


# In[40]:


point.text


# In[41]:


rating = soup.find('td',class_ = "rankings-block__banner--rating u-text-right")

rating


# In[42]:


rating.text


# In[43]:


teams = []

for i in soup.find_all('span',class_ = "u-hide-phablet"):
    teams.append(i.text)
    
teams 


# In[44]:


matches = []

for i in soup.find_all('td',class_ = "table-body__cell u-center-text"):
    matches.append(i.text)
    
matches  


# In[45]:


ratings=[]

for i in soup.find_all('td',class_ = "table-body__cell u-text-right rating"):
    ratings.append(i.text)
    
ratings    


# # mens batsman

# In[46]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')
page


# In[47]:


soup = BeautifulSoup(page.content)
soup


# In[48]:


first_player = soup.find('div',class_ = "rankings-block__banner--name")
first_player


# In[49]:


first_player.text


# In[50]:


country = soup.find('div',class_ = "rankings-block__banner--nationality")
country


# In[51]:


country.text


# In[52]:


rating = soup.find('div',class_= "rankings-block__banner--rating")
rating


# In[53]:


rating.text


# In[54]:


players = []

for i in soup.find_all('td',class_ = "table-body__cell name"):
    players.append(i.text)
    
players    


# In[55]:


countries = []

for i in soup.find_all('span',class_= "table-body__logo-text"):
    countries.append(i.text)
    
countries


# In[56]:


ratings=[]

for i in soup.find_all('td',class_= "table-body__cell u-text-right rating"):
    ratings.append(i.text)
    
ratings 


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # 9) Write a python program to scrape mentioned details from dineout.co.in :

# In[60]:


page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[61]:


page


# In[62]:


soup = BeautifulSoup(page.content)


# In[63]:


soup


# In[64]:


first_title = soup.find('div', class_ = "restnt-info cursor")
first_title


# In[65]:


first_title.text


# In[66]:


loc = soup.find('div',class_ = "restnt-loc ellipsis")
loc.text


# In[67]:


sta = soup.find('span',class_ = "double-line-ellipsis")
sta.text


# In[68]:


titles = []

for i in soup.find_all('div',class_ ="restnt-info cursor"):
    titles.append(i.text)
    
titles 


# In[69]:


location = []

for i in soup.find_all('div',class_ = "restnt-loc ellipsis"):
    location.append(i.text)
    
location   


# In[70]:


price = []

for i in soup.find_all('span',class_ = "double-line-ellipsis"):
    price.append(i.text)
    
price   


# In[71]:


images = []

for i in soup.find_all("img", class_ = "no-img"):
    images.append(i['data-src'])
    
images   


# In[72]:


import pandas as pd
df = pd.DataFrame(['Titles',titles,'Location',location,'Price',price,'Images_url',images])
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




