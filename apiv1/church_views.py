from requests import request 
from django.db.models import Prefetch
# no-code imports 
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
# model imports
from church.models import ChurchDenomination, ChurchItem, ChurchMembership, ChurchPastorship, DenominationLeadership
from church.serializers import ChurchDenominationSerializer, ChurchItemSerializer, ChurchMembershipSerializer, ChurchSerializer, AddMembershipSerializer
# profile models
from profiles.models import UserProfile

class DenominationList(generics.ListAPIView):
    serializer_class = ChurchDenominationSerializer

    def get_queryset(self):
        queryset = ChurchDenomination.objects.all().prefetch_related(Prefetch('churches',
                        queryset=ChurchItem.objects.all(),to_attr='denomination_churches')) 
        return queryset

class ChurchList(generics.ListAPIView):
    serializer_class = ChurchSerializer
    def get_queryset(self):
        queryset = ChurchItem.objects.all()
        return queryset

class ChurchDetail(generics.RetrieveAPIView):
    serializer_class = ChurchItemSerializer
    def get_queryset(self):
        churches = ChurchItem.objects.all()
        queryset = churches.filter(pk = self.kwargs['pk'])
        return queryset

class ChurchMembershipList(generics.ListAPIView):
    serializer_class = ChurchMembershipSerializer
    
    def get_queryset(self):
        user = self.request.user
        profile = UserProfile.objects.get(profile_owner=user)
        queryset = ChurchMembership.objects.filter(user_profile=profile)
        return queryset

class ChurchMembershipDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChurchMembershipSerializer
    
    def get_queryset(self):
        user = self.request.user
        profile = UserProfile.objects.get(profile_owner=user)
        queryset = ChurchMembership.objects.filter(user_profile=profile)
        return queryset
    
    def destroy(self, request, *args, **kwargs):
        membership = ChurchMembership.objects.get(pk=self.kwargs["pk"])
        if not request.user == membership.user_profile.profile_owner:
            raise PermissionDenied("You can not delete this membership.")
        return super().destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        membership = ChurchMembership.objects.get(pk=self.kwargs["pk"])
        if not request.user == membership.user_profile.profile_owner:
            raise PermissionDenied("You can not update this Pastor profile.")
        return super().update(request, *args, **kwargs)

class AddChurchMembership(generics.CreateAPIView):
    serializer_class = AddMembershipSerializer
    def get_queryset(self):
        queryset = ChurchMembership.objects.all()
        return queryset
    
    def perform_create(self, serializer):
        user = self.request.user
        profile = UserProfile.objects.get(profile_owner=user)
        church = ChurchItem.objects.get(pk = self.kwargs['pk'])
        serializer.save(user_profile= profile, church= church)
        return super().perform_create(serializer)