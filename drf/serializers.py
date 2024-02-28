from rest_framework import serializers
from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model
from blogapp.models import Blog, Comment

class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'username', 'address', 'phone', "role", 'bio', 'profile_pic']
        

class SimpleBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'body', 'thumbnail', 'created',
                  'updated']

class BlogSerializer(serializers.ModelSerializer):
    user = MainUserSerializer(read_only=True)
    related_blog = serializers.SerializerMethodField(method_name="related_blogs")
    class Meta:
        model = Blog
        fields = ['id', 'user', 'title', 'slug', 'body', 'thumbnail', 'created',
                  'updated', 'category', 'related_blog']
        
    
    
    def related_blogs(self, blog):
        category = blog.category
        blogs = Blog.objects.filter(category=category).exclude(id=blog.id)
        serializer = SimpleBlogSerializer(blogs, many=True)
        return serializer.data
        
    
    def create(self, validated_data):
        user = self.context['user']
        blog = Blog.objects.create(user=user, **validated_data)
        return blog
        


        


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = get_user_model()
        fields = ['id', 'email', 'username', 'address', 'phone', "role", 'bio', 'profile_pic']




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment 
        fields = ['id', 'body']
        
    
    
    def create(self, validated_data):
        user = self.context["user"]
        blog = self.context["blog"]
        comment = Comment.objects.create(blog=blog, user=user, **validated_data)
        return comment