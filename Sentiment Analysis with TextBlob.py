#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install textblob


# In[1]:


from textblob import TextBlob


# In[2]:


import numpy


# In[5]:


reviews = [
    "I absolutely loved this movie! The storyline was gripping and the characters were well developed.",
    "This was the worst movie I have ever seen. The plot was predictable and the acting was terrible.",
    "An average film with some good moments, but overall it didn't live up to the hype.",
    "Fantastic direction and brilliant performances. A must-watch for everyone!",
    "I did not enjoy this movie. It was boring and too long.",
    "I know they worked hard but it's not my type."
]


# In[8]:


for review in reviews:
    blob = TextBlob(review)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        sentiment_label = "Positive"
    elif sentiment < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    print(f"Review: {review}\nSentiment: {sentiment_label}\n")


# In[ ]:




