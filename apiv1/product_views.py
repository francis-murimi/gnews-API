from requests import request 
from django.db.models import Prefetch
# no-code imports 
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
# importing models
from product.models import Topic, Service, Blog, Comment
from product.serializers import BlogListSerializer, TopicSerializer, ServiceSerializer, BlogSerializer, CommentSerializer, ServiceBlogSerializer, TopicBlogSerializer
from church.models import ChurchItem, ChurchMembership, ChurchPastorship
from church.serializers import ChurchPastorshipSerializer
from profiles.models import UserProfile,PastorProfile
from profiles.serializers import PastorProfileSerializer


class TopicList(generics.ListCreateAPIView):
    serializer_class = TopicSerializer
    
    def get_queryset(self):
        topics = Topic.objects.all()
        queryset = topics.filter(church = self.kwargs['pk'])
        return queryset
    
    def perform_create(self, serializer):
        user = self.request.user
        church_pastor = ChurchPastorship.objects.filter(pastor_profile__profile_owner = user).count()
        if  church_pastor > 0:
            church = ChurchItem.objects.get(pk = self.kwargs['pk'])
            serializer.save(church= church)
        else:
            raise PermissionDenied("You can not add a topic to this church.")
        return super().perform_create(serializer)

class TopicDetail(generics.RetrieveUpdateAPIView):
    serializer_class = TopicBlogSerializer
    def get_queryset(self):
        queryset = Topic.objects.filter(pk = self.kwargs['pk']).prefetch_related(Prefetch('topic_blogs',queryset=Blog.objects.filter(status=1),to_attr='blogs'))
        return queryset

    def update(self, request, *args, **kwargs):
        topic = Topic.objects.get(pk = self.kwargs['pk'])
        user = self.request.user
        pastorship = ChurchPastorship.objects.filter(church = topic.church, pastor_profile__profile_owner= user).count()
        if pastorship < 1:
            raise PermissionDenied("You can not update this topic.")
        return super().update(request, *args, **kwargs)


class ServiceList(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    
    def get_queryset(self):
        services = Service.objects.all()
        queryset = services.filter(church = self.kwargs['pk'])
        return queryset
    
    def perform_create(self, serializer):
        user = self.request.user
        church_pastor = ChurchPastorship.objects.filter(pastor_profile__profile_owner = user).count()
        if  church_pastor > 0:
            church = ChurchItem.objects.get(pk = self.kwargs['pk'])
            serializer.save(church= church)
        else:
            raise PermissionDenied("You can not add a service to this church.")
        return super().perform_create(serializer)

class ServiceDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ServiceBlogSerializer
    def get_queryset(self):
        queryset = Service.objects.filter(pk = self.kwargs['pk']).prefetch_related(Prefetch('service_blogs',queryset=Blog.objects.filter(status=1),to_attr='blogs'))
        return queryset

    def update(self, request, *args, **kwargs):
        service = Service.objects.get(pk = self.kwargs['pk'])
        user = self.request.user
        pastorship = ChurchPastorship.objects.filter(church = service.church, pastor_profile__profile_owner= user).count()
        if pastorship < 1:
            raise PermissionDenied("You can not update this Service.")
        return super().update(request, *args, **kwargs)

class ChurchPastorList(generics.ListAPIView):
    serializer_class = PastorProfileSerializer
    
    def get_queryset(self):
        pastors = ChurchPastorship.objects.filter(church = self.kwargs['pk']).values_list('pastor_profile', flat=True)
        queryset = PastorProfile.objects.filter(id__in = [pastors])
        return queryset

class ChurchPastorBlogList(generics.ListAPIView):
    serializer_class = BlogListSerializer
    
    def get_queryset(self):
        queryset = Blog.objects.filter(church = self.kwargs['pk'],pastor = self.kwargs['id'],status= 1)
        return queryset

class ChurchBlogList(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    
    def get_queryset(self):
        queryset = Blog.objects.filter(church = self.kwargs['pk'], status = 1)
        return queryset
    
    def perform_create(self, serializer):
        profile = UserProfile.objects.get(profile_owner = self.request.user)
        member = ChurchMembership.objects.filter(user_profile = profile).count()
        if member > 0:
            church = ChurchItem.objects.get(pk = self.kwargs['pk'])
            serializer.save(church= church, created_by=profile)
        else:
            raise PermissionDenied("You can not add a blog to this church.")
        return super().perform_create(serializer)

class BlogDetail(generics.RetrieveUpdateAPIView):
    serializer_class = BlogSerializer
    
    def get_queryset(self):
        queryset = Blog.objects.filter(pk= self.kwargs['pk']).prefetch_related(Prefetch('comments',queryset=Comment.objects.filter(active=True)))
        return queryset
    
    def update(self, request, *args, **kwargs):
        blog = Blog.objects.get(pk=self.kwargs["pk"])
        profile = UserProfile.objects.get(profile_owner = self.request.user)
        if not profile == blog.created_by:
            raise PermissionDenied("You can not update this blog.")
        return super().update(request, *args, **kwargs)

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        queryset = Comment.objects.filter(blog_id = self.kwargs["pk"],active=True)
        return queryset
    
    def perform_create(self, serializer):
        blog_id = self.kwargs["pk"]
        blog = Blog.objects.get(id = blog_id)
        church = blog.church
        profile = UserProfile.objects.get(profile_owner = self.request.user)
        member = ChurchMembership.objects.filter(church = church, user_profile = profile).count()
        
        if member > 0 :
            serializer.save(created_by= profile, blog = Blog.objects.get(pk=self.kwargs["pk"]))
        else:
            raise PermissionDenied("You can not add a comment to this blog.")
        return super().perform_create(serializer)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        queryset = Comment.objects.filter(id=self.kwargs["pk"])
        return queryset
    
    def destroy(self, request, *args, **kwargs):
        comment = Comment.objects.get(pk=self.kwargs["pk"])
        profile = UserProfile.objects.get(profile_owner = self.request.user)
        if not profile == comment.created_by:
            raise PermissionDenied("You can not delete this comment.")
        return super().destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        comment = Comment.objects.get(pk=self.kwargs["pk"])
        profile = UserProfile.objects.get(profile_owner = self.request.user)
        if not profile == comment.created_by:
            raise PermissionDenied("You can not update this comment.")
        return super().update(request, *args, **kwargs)