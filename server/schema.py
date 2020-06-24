import graphene
from tweets.schema import Query as tweets_query



class Query(tweets_query):
    pass


schema=graphene.Schema(query=Query)