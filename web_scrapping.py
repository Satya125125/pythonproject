# importing modules
import requests
from bs4 import BeautifulSoup
import csv
import pandas as p
#scrapping the data
url="https://www.flipkart.com/search?q=mobiles"
r=requests.get(url)

soup=BeautifulSoup(r.content,"html.parser")

title=soup.find_all("div",class_="_4rR01T")
ratings=soup.find_all("div",class_="_3LWZlK")
reviews=soup.find_all("span",class_="_2_R_DZ")
prices=soup.find_all("div",class_="_30jeq3 _1_WHN1")

mt=[]
mr=[]
mre=[]
mp=[]

for title,rating,rev,pri in zip(title,ratings,reviews,prices):
    mt.append(title.text)
    mr.append(rating.text)
    mre.append(rev.text)
    mp.append(pri.text)
    
#sving data
d={"mt":mt,"mr":mr,"mre":mre,"mp":mp}
model=p.DataFrame(data=d)

model.to_csv("mobiles_data.csv")



