#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:15:08 2019

@author: adityabhat
"""

import schedule
import praw
import pandas as pd
import time
from datetime import datetime
#Function to scrape article elements at certain times

def job():
    
   #Authenticating with reddit servers with the access tokens
    reddit = praw.Reddit(client_id='',
                             client_secret='',
                             password='',
                             user_agent='',
                             username='')
    
    #Creating an instance of reddit object specifying the subreddit to scrape from
    subreddits=reddit.subreddit('news')
    subs=reddit.subreddit('news').subscribers
    #Extracting top 15 hot posts from the hot section of reddit
    hot_news=subreddits.hot(limit=10)
    
    number = subreddits.active_user_count
     #getting date time 
    now=datetime.now()
    
    #Creating a dictionary to append the values extracted from the api 
    topics_dict={
             "ActiveUsers":[],\
             "Subs":[],\
             "Datetime":[]
             }
    
    #Looping through the elements and appeding them to the dictionary    
    for submission in hot_news:
      
      topics_dict['ActiveUsers'].append(number)
      topics_dict['Subs'].append(subs)
      topics_dict['Datetime'].append(now)
      
    df = pd.DataFrame(topics_dict)
    with open('auc.csv', 'a') as f:
         df.to_csv(f, header=True)
     
    
#Scheduling 
schedule.every().hour.at(":00").do(job)


while True:
    schedule.run_pending()
    time.sleep(60)
    
    
    
    
    
