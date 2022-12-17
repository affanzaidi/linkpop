from django.urls import path,include
from . import views

urlpatterns = [
    path('users/', views.UserInfo.as_view(), name= "users"),
    path('users/<id>', views.SingleUserInfo.as_view(), name= "users<id>"),
    path('links/', views.LinkInfo.as_view(), name= "links"),
    path('links/<id>', views.SingleUserLinks.as_view(), name= "links<id>"),
    path('socials/', views.SocialInfo.as_view(), name= "socials"),
    path('socials/<id>', views.SingleUserSocials.as_view(), name= "socials<id>"),
    path('get_user_data/<id>', views.GetAllUserinfo.as_view(), name= "get_user_data<id>")
]