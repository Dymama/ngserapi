from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import viewsets,generics

from . models import *
from . serializers import *
# Create your views here.
from django.db.models import Q
class prix_de_vente(generics.ListAPIView):
    serializer_class=ClientSerializer
    def get_queryset(self):
        queryset=Client.objects.all()
        client=self.request.query_params.get('query')
        if client:
            resultat=(Q(client__icontains=client))
            queryset=queryset.filter(resultat)
            print(queryset)
        return queryset


class ClientsViewSet(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
    
class AchatsViewSet(viewsets.ModelViewSet):
    queryset=Achat.objects.all()
    serializer_class=AchatSerializer
    
class AchatPlusEleve(viewsets.ModelViewSet):
    queryset=Achat.objects.all()
    serializer_class=AchatSerializer