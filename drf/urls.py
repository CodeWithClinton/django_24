from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_nested.routers import NestedDefaultRouter
from . import views 


router = routers.DefaultRouter()
router.register("blogs", views.BlogModelViewSet, basename="blogs")


blog_router = NestedDefaultRouter(router, "blogs", lookup="blog")
blog_router.register("comments", views.CommentModelViewSet, basename='blog-comments')

urlpatterns = [
   path("", include(router.urls)),
   path("", include(blog_router.urls))
]

