from rest_framework import serializers 
from blogapp.models import Blog 



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'user', 'title', 'slug', 'body', 'thumbnail', 'created',
                  'updated', 'category']