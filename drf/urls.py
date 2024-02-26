from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 



router = DefaultRouter()

router.register("blogs", views.BlogModelViewSet)

urlpatterns = [
   path("", include(router.urls))
]

201505
215343
215817
220438