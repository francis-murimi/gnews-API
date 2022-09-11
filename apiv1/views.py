from django.contrib.auth import authenticate # for authentication token
from requests import request 
# no-code imports 
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
# model serializers import 
from apiv1.serializers import UserSerializer
from profiles.models import UserProfile, PastorProfile,LeaderProfile
from profiles.serializers import UserProfileSerializer,PastorProfileSerializer, LeaderProfileSerializer



# authentication and log in block
class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

# end of authentication and log in block


# user profile views
class UserProfileList(generics.ListCreateAPIView): #list and create
    serializer_class = UserProfileSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = UserProfile.objects.filter(profile_owner=user)
        return queryset
    def perform_create(self, serializer):
        serializer.save(profile_owner= self.request.user)
        return super().perform_create(serializer)


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView): # details, delete, update a single user profile
    serializer_class = UserProfileSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = UserProfile.objects.filter(profile_owner=user)
        return queryset
    def destroy(self, request, *args, **kwargs):
        profile = UserProfile.objects.get(pk=self.kwargs["pk"])
        if not request.user == profile.profile_owner:
            raise PermissionDenied("You can not delete this profile.")
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        profile = UserProfile.objects.get(pk=self.kwargs["pk"])
        if not request.user == profile.profile_owner:
            raise PermissionDenied("You can not update this profile.")
        return super().update(request, *args, **kwargs)
# end of user profile views


# pastor profile views
class PastorProfileList(generics.ListCreateAPIView): #list and create
    serializer_class = PastorProfileSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = PastorProfile.objects.filter(profile_owner=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(profile_owner= self.request.user)
        return super().perform_create(serializer)


class PastorProfileDetail(generics.RetrieveUpdateDestroyAPIView): # details, delete, update a single pastor profile
    serializer_class = PastorProfileSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = PastorProfile.objects.filter(profile_owner=user)
        return queryset
    def destroy(self, request, *args, **kwargs):
        profile = PastorProfile.objects.get(pk=self.kwargs["pk"])
        if not request.user == profile.profile_owner:
            raise PermissionDenied("You can not delete this Pastor profile.")
        return super().destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        profile = PastorProfile.objects.get(pk=self.kwargs["pk"])
        if not request.user == profile.profile_owner:
            raise PermissionDenied("You can not update this Pastor profile.")
        return super().update(request, *args, **kwargs)
# end of pastor profile views


# leader profile views
class LeaderProfileList(generics.ListCreateAPIView): #list and create
    serializer_class = LeaderProfileSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = LeaderProfile.objects.filter(profile_owner=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(profile_owner= self.request.user)
        return super().perform_create(serializer)


class LeaderProfileDetail(generics.RetrieveUpdateDestroyAPIView): # details, delete, update a single leader profile
    serializer_class = LeaderProfileSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = LeaderProfile.objects.filter(profile_owner=user)
        return queryset
    def destroy(self, request, *args, **kwargs):
        profile = LeaderProfile.objects.get(pk=self.kwargs["pk"])
        if not request.user == profile.profile_owner:
            raise PermissionDenied("You can not delete this Leader profile.")
        return super().destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        profile = LeaderProfile.objects.get(pk=self.kwargs["pk"])
        if not request.user == profile.profile_owner:
            raise PermissionDenied("You can not update this Leader profile.")
        return super().update(request, *args, **kwargs)
# end of leader profile views

