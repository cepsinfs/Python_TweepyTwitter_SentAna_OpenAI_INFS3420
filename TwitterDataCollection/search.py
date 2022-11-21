import tweepy
import streamlit as st
import pandas as pd
import config

client = tweepy.Client(bearer_token=config.bearer)

qry = "covid lang:en -is:retweet"

response = client.search_all_tweets(
                query=qry, 
                max_results=500, 
                tweet_fields=['author_id', 'created_at', 'public_metrics'], 
                user_fields=['public_metrics'], 
                expansions="author_id"
                
                
                )

user_dict = {}
results = []

for user in response.includes['users']:
    user_dict[user.id] ={

        'name': user.name, 
        'handler': user.username,
        'followers': user.public_metrics['followers_count'],
        'following': user.public_metrics['following_count']

    }


for tweet in response.data:

    auth_info = user_dict[tweet.author_id]

    results.append({

        "tweetID": tweet.id,
        "text": tweet.text,
        "posted_on": tweet.created_at,
        "likes": tweet.public_metrics['like_count'],
        "retweets": tweet.public_metrics['retweet_count'],
        "replies": tweet.public_metrics['reply_count'],
        'name': auth_info['name'],
        'handler': auth_info['handler'],
        'followers': auth_info['followers'],
        'following': auth_info['following']


    })


dataset = pd.DataFrame(results)
st.write(dataset)
# dataset.to_csv("collectedData.csv")
# dataset.to_excel("dataset.xlsx")

st.download_button(label="Export to CSV", data=dataset.to_csv(), mime="text/csv", file_name="COVID.csv" )


   

    









# for tweet in response.data:
#     st.info(f" Tweet Text: {tweet.text}  Tweet ID: {tweet.id} Author: {tweet.author_id} {tweet.created_at} {tweet.public_metrics}")


   

