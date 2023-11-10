from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/', views.UserInfo.as_view(), name= "signup-api"),
    path('login', views.Login.as_view(), name= "login-api"),
    path('check_mobile_number', views.Check_mobile_exists.as_view(), name= "check-mobile-exists"),
    path('check_user_details', views.Check_user_details.as_view(), name= "check-user-details"),
    path('set_reset_password', views.Reset_password.as_view(), name= "check-user-details"),
    path('save_device', views.DeviceInfo.as_view(), name= "save-new device"),
    path('get_all_device', views.UserDevice.as_view(), name= "get-user-devices"),
    
    path('users/', views.UserInfo.as_view(), name= "users"),
    path('users/<id>', views.SingleUserInfo.as_view(), name= "users<id>"),
    path('device/', views.DeviceInfo.as_view(), name= "device"),
    path('device/<id>', views.SingleUserInfo.as_view(), name= "users<id>"),
    # path('links/', views.LinkInfo.as_view(), name= "links"),
    # path('links/<id>', views.SingleUserLinks.as_view(), name= "links<id>"),
    # path('socials/', views.SocialInfo.as_view(), name= "socials"),
    # path('socials/<id>', views.SingleUserSocials.as_view(), name= "socials<id>"),
    # path('get_user_data/<id>', views.GetAllUserinfo.as_view(), name= "get_user_data<id>"),
    path('video', views.VideoInfo.as_view(), name="Youtube demo Videos"),
    path('video/<id>', views.SingleYoutubeInfo.as_view(), name="single Youtube demo Videos")
]