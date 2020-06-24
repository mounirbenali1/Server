from django.db import models
from mongoengine import Document
from mongoengine.fields import(StringField,ListField,ReferenceField)

class User(Document):
    meta = {'collection': 'US9_trend'}
    full_name = StringField(required=True)
    tweet_text= StringField(required=True)
    no_of_replies = StringField(required=True)
    number_of_likes = StringField(required=True)
    hashtags= StringField(required=True)
    username = StringField(required=True)
    no_of_retweets = StringField(required=True)
    twitter_url= StringField(required=True)
    call_to_action = StringField(required=True)
    no_of_hashtags = StringField(required=True)
    mentions= StringField(required=True)
    tweet_time = StringField(required=True)
    no_of_mentions = StringField(required=True)
    sentiment = StringField(required=True)


class George_s(Document):
    meta = {'collection': 'George'}
    full_name = StringField(required=True)
    tweet_text= StringField(required=True)
    no_of_replies = StringField(required=True)
    number_of_likes = StringField(required=True)
    hashtags= StringField(required=True)
    username = StringField(required=True)
    no_of_retweets = StringField(required=True)
    twitter_url= StringField(required=True)
    call_to_action = StringField(required=True)
    no_of_hashtags = StringField(required=True)
    mentions= StringField(required=True)
    tweet_time = StringField(required=True)
    no_of_mentions = StringField(required=True)
    sentiment = StringField(required=True)

class Hashtags_trend(Document):
    meta = {'collection': 'US_HASHTAGS_TREND_copy'}
    full_name = StringField(required=True)
    tweet_text= StringField(required=True)
    no_of_replies = StringField(required=True)
    number_of_likes = StringField(required=True)
    hashtags= StringField(required=True)
    username = StringField(required=True)
    no_of_retweets = StringField(required=True)
    twitter_url= StringField(required=True)
    call_to_action = StringField(required=True)
    no_of_hashtags = StringField(required=True)
    mentions= StringField(required=True)
    tweet_time = StringField(required=True)
    no_of_mentions = StringField(required=True)
    sentiment = StringField(required=True)
    Country=StringField(required=True)    