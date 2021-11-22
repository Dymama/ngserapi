from rest_framework import serializers
from . models import *


#On serealise les données puis on les affiches sous forme JSON
class AchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achat
        fields = ('produit','prix',)       
        
class ClientSerializer(serializers.ModelSerializer):
    #liaison à la table achats
    achats=AchatSerializer(many=True, read_only=True)
    class Meta:
        model = Client
        fields = ('id', 'client', 'achats')


        
class ClientAchatEleveSerializer(serializers.ModelSerializer):
    #achats = serializers.PrimaryKeyRelatedField(queryset=Achat.objects.all(), many=True)
    achats=AchatSerializer(many=True, read_only=True)
    

    class Meta:
        model = Client
        fields = ('id', 'client', 'achats')