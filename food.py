from flask import Flask,render_template,redirect,request
import pandas as pd 
import numpy as np
import requests
from urllib.request import urlopen
import urllib.request as urllib2 
from bs4 import BeautifulSoup  
import matplotlib.pyplot as plt
import random
app=Flask(__name__)
@app.route('/')
def index():
    imageis="https://upload.wikimedia.org/wikipedia/commons/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg"
    return render_template("index.html",imageis=imageis)

@app.route('/',methods=['POST'])
def marks():
    if request.method == 'POST':

        food=str(request.form['food'])
        a=[]   
        def getdata(url):  
            r = requests.get(url)  
            return r.text  
        
        htmldata = getdata("https://www.google.com/search?q="+food+" food"+"&rlz=1C1CHBF_enIN921IN921&sxsrf=ALeKk00MvauCDY4oq4VxU3Jq72l7226XrA:1613817483274&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjJlcrOovjuAhUegUsFHdjdDv4Q_AUoAXoECAcQAw&biw=1536&bih=722")  
        soup = BeautifulSoup(htmldata, 'html.parser')  
        count=0
        for item in soup.find_all('img'): 
            x = item['src']
            a.append(x)
            count=count+1
        #print(count)
        random_number = random.randint(1, count-1)
        random2= random.randint(1, count-1)
        random3= random.randint(1, count-1)

        x = a[random2]
        #print(x)

        y = a[random_number]
        z= a[random3]
        URL = 'https://google.com/search?q='+food+' food details '
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        set1 = soup.find_all('div', {'class': 'BNeawe iBp4i AP7Wnd'})
        set2 = soup.find_all('div', {'class': 'BNeawe s3v9rd AP7Wnd'})
        strings=str(set2[0])
        split_string = strings.split("<sub", 1)
        substring = split_string[0]
        ans = BeautifulSoup(substring, 'html.parser')
        content=ans.text
        URL = 'https://google.com/search?q='+food+' protein content'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        page.content

        set1 = soup.find_all('div', {'class': 'BNeawe iBp4i AP7Wnd'})
        set2 = soup.find_all('div', {'class': 'BNeawe s3v9rd AP7Wnd'})
        c=0

        fatvar=""   
        for i in set1:
            if(i.text.find(' g')!=-1):
                fatvar=i.text
                #print(i.text)
                c=1
                break
            
        if(len(set2)!=0):
            j = set2[0]
            if(c==0):
                for i in set2:
                    if(i.text.find(' g')!=-1 and j.text.find('Protein')!=-1):
                        fatvar=i.text
                        #print(fatvar)
                        break
                    j=i


    return render_template("index.html",imageis=x,content=content,protein=fatvar)
if __name__== '__main__':
    app.run(debug=True)
