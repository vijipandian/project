import streamlit as st
import pymongo 
import pandas as pd
import snscrape.modules.twitter as sntwitter


server=pymongo.MongoClient("mongodb+srv://viji:1234@cluster0.gwcwspp.mongodb.net")
db=server.dsguvi
mycollection=db.twitter


st.title("Twitter Scrape")
tweets_list1=[]
user_name=st.text_input('USERNAME')
staring_date=st.date_input('STARTING DATA')
ending_date=st.date_input('ENDING DATA')


for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{user_name} since:{staring_date} until:{ending_date}').get_items()):#declear a user name
    if i>10: #number of tweets you want toscrape
        break
    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username]) #declare the attributes to be returned
    

# tweets_list1

data=pd.DataFrame(tweets_list1, columns=['Datatime','Tweet ID','Text','Username'])
# data

Dict=data.to_dict('list')


if st.button("scrape tweets"):
    st.dataframe(tweets_list1)
    mycollection.insert_one(Dict)
    st.success("Data saveed success")
    
    
    

 
    
