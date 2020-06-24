import graphene  
from tweets.models import User as UserModel ,Hashtags_trend as Hashtags_tr , George_s as George_sen    
from mongoengine import connect
from graphene_mongo import MongoengineObjectType

class User(MongoengineObjectType):
    class Meta:
        model = UserModel

class tr_Hashtags(MongoengineObjectType):
    class Meta:
        model = Hashtags_tr

class sen_George(MongoengineObjectType):
    class Meta:
        model = George_sen
"""
class UK_Hashtags(MongoengineObjectType):
    class Meta:
        model = ukHashtags

class FR_Hashtags(MongoengineObjectType):
    class Meta:
        model = frHashtags
"""

class Query(graphene.ObjectType):
    users = graphene.List(User)
    Hashtags = graphene.List(tr_Hashtags)
    GeorgeSen=graphene.List(sen_George)
    #FrHashtags = graphene.List(FR_Hashtags)
    #UkHashtags = graphene.List(UK_Hashtags)

    def resolve_users(self, info):
        return list(UserModel.objects.all())

    def resolve_Hashtags(self, info):
        return list(Hashtags_tr.objects.all())
    
    def resolve_GeorgeSen(self, info):
        return list(George_sen.objects.all())
    
    """
    def resolve_UkHashtags(self, info):
        return list(ukHashtags.objects.all())
    """
         
    
 
