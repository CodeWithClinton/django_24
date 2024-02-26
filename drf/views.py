from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .serializers import BlogSerializer 
from blogapp.models import Blog


# Create your views here.

class BlogModelViewSet(ModelViewSet):
    serializer_class = BlogSerializer 
    queryset = Blog.objects.all()


# class BlogListAPIView(APIView):
#     def get(self, request):
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)
    
    
#     def post(self, request):
#         serializer  = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BlogDetailAPIView(APIView):
#     def get(self, request, pk):
#         blog = get_object_or_404(Blog, pk=pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data) 
    
#     def put(self, request, pk):
#         blog = get_object_or_404(Blog, pk=pk)
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data) 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
#     def delete(self, request, pk):
#         blog = get_object_or_404(Blog, pk=pk) 
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        

# @api_view(['GET', 'POST'])
# def blog_list(request):
#     if request.method == 'GET':
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def blog_detail(request, pk):
#     blog = get_object_or_404(Blog, pk=pk)
#     if request.method == 'GET':
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    
#     elif request.method == 'DELETE':
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
