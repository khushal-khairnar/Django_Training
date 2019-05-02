from django.urls import path,include
from .views import home, user_registration, sample

urlpatterns = [
    path('', home, name='home'),
    path('user_registration', user_registration, name='user_registration'),
    #   path('user_profile',user_profile,name='user_profile')
    path('sample/', sample,name='sample'),
]
