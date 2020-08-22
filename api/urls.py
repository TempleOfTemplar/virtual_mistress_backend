"""sexadvices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
from . import views

app_name = "api"

router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'users', views.UserViewSet.as_view({'get': 'list'}))
# router.register(r'users/<pk>/', views.UserViewSet.as_view({'get': 'retrieve'}))
router.register(r'suggestions', views.SuggestionViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'categories', views.DeviationViewSet)

urlpatterns = [
    # path('users', views.UserList.as_view()),
    path('users/current', views.CurrentUserView.as_view()),
    # path('users/<pk>', views.UserDetails.as_view()),
    url(r'^', include(router.urls)),
]
