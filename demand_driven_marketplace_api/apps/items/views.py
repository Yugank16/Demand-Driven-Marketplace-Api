from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from django_filters import rest_framework as filters

from rest_framework import viewsets, mixins, status
from rest_framework import filters as filter

from apps.items.models import Item
from apps.items.serializers import ItemListSerializer, ItemSerializer
from apps.items.permissions import *


class ItemFilter(filters.FilterSet):
    """
    Item Filter for searching item based on name
    """
    name = filters.CharFilter(name='name', lookup_expr='icontains')

    class Meta(object):
        model = Item
        fields = ['name', 'item_status']


class ItemViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    ItemViewset Provides List Of All Item Request Made By Other Users ,
    Allows To Post A New Item Request and Get Details Of Particular Item Request
    """
    filter_backends = (filters.DjangoFilterBackend, filter.OrderingFilter)
    filter_class = ItemFilter
    ordering_fields = ('max_price', 'date_time')

    def get_serializer_class(self):

        if self.action == 'list':
            return ItemListSerializer
        return ItemSerializer
        
    def get_queryset(self):
        if self.action == 'list':
            return Item.objects.exclude(requester=self.request.user).exclude(Q(item_status=3) | Q(item_status=4))
        return Item.objects.all()
    
    def get_serializer_context(self):
        return {'user': self.request.user}
    
    def get_permissions(self):

        if self.action == 'retrieve':
            self.permission_classes = [RequestRetrievePermission, IsAuthenticated]  
        elif self.action == 'list':
            self.permission_classes = [ListAllRequestsPermission, IsAuthenticated]
        elif self.request.method == 'POST':
            self.permission_classes = [ItemRequestPermission, IsAuthenticated]

        return super(BidViewSet, self).get_permissions()


class SelfItemRequest(mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    SelfItemRequest Provides List of Item Request Made by The User ,Allows To Delete the Request
    """

    filter_backends = (filters.DjangoFilterBackend, filter.OrderingFilter)
    filter_class = ItemFilter
    ordering_fields = ('max_price', 'date_time')

    def get_serializer_class(self):
        if self.action == 'list':
            return ItemListSerializer
        return ItemSerializer
    
    def get_queryset(self):
        if self.action == 'list':
            return Item.objects.filter(requester=self.request.user)
        return Item.objects.all()
    
    def get_permissions(self):

        if self.action == 'retrieve':
            self.permission_classes = [ItemRequestPermission, IsAuthenticated]  
        elif self.action == 'destroy':
            self.permission_classes = [RequestDeletePermission, IsAuthenticated]

        return super(BidViewSet, self).get_permissions()


