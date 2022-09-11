from rest_framework import serializers
# importing models
from product.models import Topic, Service, Blog, Comment


class CommentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Comment
        fields = ['id','created_on','content']


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Blog
        fields = ['id','category','pastor','church','service','title','content','created','comments'] # 'category','created_by','title','content','created',

class BlogListSerializer(serializers.ModelSerializer): # to use with service serializer, topic serializer, pastor list
    class Meta:
        model = Blog
        fields = ['id','title','created']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','title','service_day','start_time','end_time','description']

class ServiceBlogSerializer(serializers.ModelSerializer):
    blogs = BlogListSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Service
        fields = ['id','title','service_day','start_time','end_time','description','blogs']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id','title','description'] 

class TopicBlogSerializer(serializers.ModelSerializer):
    blogs = BlogListSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Topic
        fields = ['id','title','description','blogs'] 
