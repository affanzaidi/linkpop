from django.db import models


# Create your models here.

class User(models.Model):
    id              = models.AutoField(primary_key=True)
    email           = models.CharField(max_length=255)
    username        = models.CharField(max_length=255)
    account_name    = models.CharField(max_length=255)
    mobile_number   = models.CharField(max_length=20)
    password        = models.CharField(max_length=255)
    device_token    = models.CharField(max_length=255)
    device_type     = models.IntegerField()
    created_date    = models.DateTimeField(auto_now_add=True)
    status          = models.IntegerField()
    updated_date    = models.DateTimeField(auto_now=True)
    
    
class Alarm(models.Model):
    alarm_id        = models.IntegerField()
    user_id         = models.IntegerField()
    alarm_time      = models.TimeField
    alarm_days      = models.IntegerField()
    status          = models.IntegerField()
    created_date    = models.DateTimeField(auto_now_add=True)
    updated_date    = models.DateTimeField(auto_now=True)

class Alarm_Device_Details(models.Model):
    alarm_device_details_id     = models.IntegerField()
    user_id                     = models.IntegerField()
    alarm_id                    = models.IntegerField()
    device_id                   = models.IntegerField()
    status                      = models.IntegerField(default=1)

class Device(models.Model):
    server_device_id    = models.AutoField(primary_key=True)
    user_id             = models.IntegerField()
    device_id           = models.CharField(max_length=255)
    hex_device_id       = models.CharField(max_length=255)
    device_name         = models.CharField(max_length=255)
    ble_address         = models.CharField(max_length=255)
    device_type         = models.IntegerField()
    remember_last_color = models.CharField(max_length=255)
    status              = models.IntegerField()
    is_favourite        = models.IntegerField()
    identifier          = models.CharField(max_length=255, null=True,blank=True, default=None)
    mac_address         = models.CharField(max_length=255, null=True,blank=True, default=None)
    socket_status       = models.CharField(max_length=255, null=True,blank=True, default=None)
    wifi_configured     = models.CharField(max_length=255, null=True,blank=True, default=None)
    created_date        = models.DateTimeField(auto_now_add=True)
    updated_date        = models.DateTimeField(auto_now=True)
    
    
class Device_Favourite_Details(models.Model):
    favourite_id    = models.IntegerField()
    device_id       = models.IntegerField()
    user_id         = models.IntegerField()
    is_favourite    = models.IntegerField()
    created_date    = models.DateTimeField(auto_now_add=True)
    
    
class Device_Group(models.Model):
    device_group_id     = models.AutoField(primary_key=True)
    group_name          = models.CharField(max_length=255)
    user_id             = models.ForeignKey(User, on_delete=models.CASCADE,)
    local_group_id      = models.CharField(max_length=255)
    local_group_hex_id  = models.CharField(max_length=255)
    status              = models.IntegerField()
    is_favourite        = models.IntegerField()
    created_date        = models.DateTimeField(auto_now_add=True)
    updated_date        = models.DateTimeField(auto_now=True)
    
    
class Device_group_Details(models.Model):
    device_group_details_id = models.AutoField(primary_key=True)
    device_id               = models.ForeignKey(Device, on_delete=models.CASCADE,blank= True, null=True)
    group_id                = models.ForeignKey(Device_Group, on_delete=models.CASCADE,blank= True, null=True)
    user_id                 = models.ForeignKey(User, on_delete=models.CASCADE,blank= True, null=True)
    status                  = models.IntegerField()
    created_date            = models.DateTimeField(auto_now_add=True)
    
class Device_Socket_Details(models.Model):
    id              = models.IntegerField(primary_key=True)
    device_id       = models.IntegerField()
    socket_id       = models.IntegerField()
    socket_name     = models.CharField(max_length=255)
    image_type      = models.IntegerField()
    created_date    = models.DateTimeField(auto_now_add=True)
    updated_date    = models.DateTimeField(auto_now=True)
    created_by      = models.IntegerField()
    updated_by      = models.IntegerField()
    
    
class Device_Type(models.Model):
    id                  = models.AutoField(primary_key=True)
    device_type_name    = models.CharField(max_length=255)
    device_type_value   = models.CharField(max_length=255)
    status              = models.IntegerField()
    created_date        = models.DateTimeField(auto_now_add=True)
    
    
class Group_Favourite_Details(models.Model):
    favourite_id    = models.IntegerField()
    group_id        = models.IntegerField()
    user_id         = models.IntegerField()
    is_favourite    = models.IntegerField()
    created_date    = models.DateTimeField(auto_now_add=True)
    
class Notification(models.Model):
    id              = models.IntegerField(primary_key=True)
    user_id         = models.IntegerField()
    device_type     = models.IntegerField()
    device_token    = models.TextField()
    response_details = models.TextField()
    msg             = models.TextField()
    
    
class Socket_Strip_Device_Details(models.Model):
    id                  = models.IntegerField(primary_key=True)
    strip_device_id     = models.CharField(max_length=255)
    strip_device_hex_id = models.CharField(max_length=255)
    strp_device_name    = models.CharField(max_length=255)
    user_id             = models.IntegerField()
    service_device_id   = models.IntegerField()
    created_date        = models.DateTimeField(auto_now_add=True)
    
# class User(models.Model):
#     id              = models.AutoField(primary_key=True)
#     email           = models.CharField(max_length=255)
#     username        = models.CharField(max_length=255)
#     account_name    = models.CharField(max_length=255)
#     mobile_number   = models.CharField(max_length=20)
#     password        = models.CharField(max_length=255)
#     device_token    = models.CharField(max_length=255)
#     device_type     = models.IntegerField()
#     created_date    = models.DateTimeField(auto_now_add=True)
#     status          = models.IntegerField()
#     updated_date    = models.DateTimeField(auto_now=True)
    

class User_Device_Token(models.Model):
    id          = models.IntegerField(primary_key=True)
    user_id     = models.IntegerField()
    device_type = models.IntegerField()
    status      = models.IntegerField()
    device_token = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    
class Youtube(models.Model):
    id              = models.AutoField(primary_key=True)
    video_id        = models.CharField(max_length=255)
    title           = models.CharField(max_length=255)
    thumbnail_url   = models.TextField()
    created_date    = models.DateTimeField(auto_now_add=True)
    updated_date    = models.DateTimeField(auto_now=True)
    created_by      = models.IntegerField()
    updated_by      = models.IntegerField()
    
    
        
    
    
    






















# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     bio = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=255)
#     link = models.CharField(max_length=255)


class Links(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    link_belongs_to = models.ForeignKey(User, on_delete=models.CASCADE)


class Socials(models.Model):
    social_media_name = models.CharField(max_length=255)
    profile_link = models.CharField(max_length=255)
    profile_belongs_to = models.ForeignKey(User, on_delete=models.CASCADE)
    
    

