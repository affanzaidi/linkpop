from rest_framework import serializers
from django.db.models import Count
import datetime
from .models import *

class Userserializer(serializers.ModelSerializer):
    email = serializers.CharField(allow_null=True)
    username = serializers.CharField(allow_null=True)
    account_name = serializers.CharField(allow_null=True)
    mobile_number = serializers.CharField(allow_null=True)
    password = serializers.CharField(allow_null=True)
    device_token = serializers.CharField(allow_null=True)
    device_type = serializers.IntegerField(allow_null=True)
    status = serializers.IntegerField(allow_null=True)
    print("In user serianlier")
    
    class Meta:
        model = User
        fields = '__all__'


    def create(self, obj):
        print("inside create user serilizer")
        new_user = User.objects.create(
            email = obj["email"],
            username = obj["username"],
            account_name = obj["account_name"],
            mobile_number = obj["mobile_number"],
            password = obj["password"],
            device_token= obj["device_token"],
            device_type= obj["device_type"],
            status= obj["status"]
        )
        return new_user
     
    def to_representation(self, instance):
        return_usersinfo = {
            "id":instance.id,
            "email":instance.email,
            "username":instance.username,
            "account_name": instance.account_name,
            "mobile_number": instance.mobile_number,
            "password": instance.password,
            "device_token": instance.device_token,
            "device_type": instance.device_type,
            "status": instance.status,
            "created_date": instance.created_date,
            "updated_date": instance.updated_date
        }

        return return_usersinfo

    def update(self, instance, obj):
        print("in update user")
        if "email" in obj:
            instance.email = obj["email"]
        if "username" in obj:
            instance.username = obj["username"]
        if "account_name" in obj:
            instance.account_name = obj["account_name"]
        if "password" in obj:
            instance.password = obj["password"]
        if "mobile_number" in obj:
            instance.mobile_number = obj["mobile_number"]
        if "device_token" in obj:
            instance.device_token = obj["device_token"]
        if "device_type" in obj:
            instance.device_type = obj["device_type"]
        if "status" in obj:
            instance.status = obj["status"]
        instance.save()
        return instance





class Deviceserializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(allow_null=True)
    device_id = serializers.CharField(allow_null=True)
    hex_device_id = serializers.CharField(allow_null=True)
    device_name = serializers.CharField(allow_null=True)
    ble_address = serializers.CharField(allow_null=True)
    device_type = serializers.IntegerField(allow_null=True)
    remember_last_color = serializers.CharField(allow_null=True)
    
    status = serializers.IntegerField(allow_null=True)
    is_favourite = serializers.IntegerField(allow_null=True)
    identifier = serializers.CharField(allow_null=True)
    mac_address = serializers.CharField(allow_null=True)
    socket_status = serializers.CharField(allow_null=True)
    wifi_configured = serializers.CharField(allow_null=True)
    # print("In Device serianlier")
    
    class Meta:
        model = Device
        fields = '__all__'


    def create(self, obj):
        new_device = Device.objects.create(
            user_id = obj["user_id"],
            device_id = obj["device_id"],
            hex_device_id = obj["hex_device_id"],
            device_name = obj["device_name"],
            ble_address= obj["ble_address"],
            device_type= obj["device_type"],
            remember_last_color= obj["remember_last_color"],
            status= obj["status"],
            is_favourite = obj["is_favourite"]
        )
        if "identifier" in obj:
            new_device.identifier = obj["identifier"]
        if "mac_address" in obj:
            new_device.mac_address = obj["mac_address"]
        if "socket_status" in obj:
            new_device.socket_status = obj["socket_status"]
        if "wifi_configured" in obj:
            new_device.wifi_configured = obj["wifi_configured"]
        new_device.save()
        return new_device
     
    def to_representation(self, instance):
        return_usersinfo = {
            "device_group_details_id": "",
            "server_device_id":instance.server_device_id,
            "user_id":instance.user_id,
            "device_id": instance.device_id,
            "hex_device_id": instance.hex_device_id,
            "device_name": instance.device_name,
            "ble_address": instance.ble_address,
            "device_type": instance.device_type,
            "remember_last_color": instance.remember_last_color,
            "status": instance.status,
            "is_favourite":instance.is_favourite,
            "identifier":instance.identifier,
            "mac_address": instance.mac_address,
            "socket_status": instance.socket_status,
            "wifi_configured": instance.wifi_configured,
            "created_date": instance.created_date,
            "updated_date": instance.updated_date
        }
        return return_usersinfo

    def update(self, instance, obj):
        print("in update user")
        if "user_id" in obj:
            instance.user_id = obj["user_id"]
        if "device_id" in obj:
            instance.device_id = obj["device_id"]
        if "hex_device_id" in obj:
            instance.hex_device_id = obj["hex_device_id"]
        if "device_name" in obj:
            instance.device_name = obj["device_name"]
        if "ble_address" in obj:
            instance.ble_address = obj["ble_address"]
        if "device_type" in obj:
            instance.device_type = obj["device_type"]
        if "remember_last_color" in obj:
            instance.remember_last_color = obj["remember_last_color"]
        if "status" in obj:
            instance.status = obj["status"]
            
        if "is_favourite" in obj:
            instance.is_favourite = obj["is_favourite"]
        if "identifier" in obj:
            instance.identifier = obj["identifier"]
        if "mac_address" in obj:
            instance.mac_address = obj["mac_address"]
        if "socket_status" in obj:
            instance.socket_status = obj["socket_status"]
        if "wifi_configured" in obj:
            instance.wifi_configured = obj["wifi_configured"]
        instance.save()
        return instance



class DeviceTypeserializer(serializers.ModelSerializer):
    device_type_name = serializers.CharField(allow_null=True)
    device_type_value = serializers.CharField(allow_null=True)
    status = serializers.IntegerField(allow_null=True)
    # print("In Device Type serianlier")
    
    class Meta:
        model = Device_Type
        fields = '__all__'


    def create(self, obj):
        new_device = Device_Type.objects.create(
            device_type_name = obj["device_type_name"],
            device_type_value = obj["device_type_value"],
            status= obj["status"]
        )
        return new_device
     
    def to_representation(self, instance):
        # print("In Device Type to rep serianlier")
        return_usersinfo = {
            "id":instance.id,
            "device_type_name":instance.device_type_name,
            "device_type_value": instance.device_type_value,
            "status": instance.status,
            "created_date": instance.created_date,
        }
        return return_usersinfo

    def update(self, instance, obj):
        # print("in update user")
        if "device_type_name" in obj:
            instance.device_type_name = obj["device_type_name"]
        if "device_type_value" in obj:
            instance.device_type_value = obj["device_type_value"]
        if "status" in obj:
            instance.status = obj["status"]
        instance.save()
        return instance





class DeviceGroupserializer(serializers.ModelSerializer):
    group_name = serializers.CharField(allow_null=True)
    user_id = serializers.CharField(allow_null=True)
    local_group_id = serializers.CharField(allow_null=True)
    local_group_hex_id = serializers.CharField(allow_null=True)
    status = serializers.IntegerField(allow_null=True)
    is_favourite = serializers.IntegerField(allow_null=True)
    
    # print("In Device serianlier")
    
    class Meta:
        model = Device_Group
        fields = '__all__'


    def create(self, obj):
        new_device = Device_Group.objects.create(
            group_name = obj["group_name"],
            user_id = User.objects.get(id=obj["user_id"]),
            local_group_id = obj["local_group_id"],
            local_group_hex_id= obj["local_group_hex_id"],
            status= obj["status"],
            is_favourite = obj["is_favourite"]
        )
        # user_id = obj["user_id"]
        if 'user_id' in obj:
            print("IN USER ID")
            new_device.user_id = User.objects.get(id=obj["user_id"])
        new_device.save()
        return new_device
     
    def to_representation(self, instance):
        Device_info_data = Device_group_Details.objects.filter(group_id = instance.device_group_id, )
        Devicedata = DeviceGroupDetailSerializer(Device_info_data, many=True)
        devices = Devicedata.data
        device_list = []
        for device in devices:
            device = Device.objects.filter(server_device_id=device['device_id'])
            device_ser = Deviceserializer(device, many=True)
            device_list.append(device_ser.data[0])
        return_usersinfo = {
            "id" : instance.device_group_id,
            "devices": device_list,
            "group_name": instance.group_name,
            "user_id":instance.user_id.id,
            "local_group_id": instance.local_group_id,
            "local_group_hex_id": instance.local_group_hex_id,
            "status": instance.status,
            "is_favourite": instance.is_favourite,
            "created_date": instance.created_date,
            "updated_date": instance.updated_date
        }
        return return_usersinfo

    def update(self, instance, obj):
        print("in update user")
        if "group_name" in obj:
            instance.group_name = obj["group_name"]
        if "user_id" in obj:
            instance.user_id = obj["user_id"]
        if "local_group_id" in obj:
            instance.local_group_id = obj["local_group_id"]
        if "local_group_hex_id" in obj:
            instance.local_group_hex_id = obj["local_group_hex_id"]
        if "status" in obj:
            instance.status = obj["status"]
        if "is_favourite" in obj:
            instance.is_favourite = obj["is_favourite"]
        instance.save()
        return instance





class DeviceGroupDetailSerializer(serializers.ModelSerializer):
    device_id = serializers.IntegerField(allow_null=True)
    group_id = serializers.IntegerField(allow_null=True)
    user_id = serializers.IntegerField(allow_null=True)
    status = serializers.IntegerField(allow_null=True)
    
    print("In Device serianlier")
    
    class Meta:
        model = Device_group_Details
        fields = '__all__'


    def create(self, obj):
        new_device = Device_group_Details.objects.create(
            device_id = Device.objects.get(server_device_id=obj["device_id"]),
            group_id = Device_Group.objects.get(device_group_id=obj["group_id"]),
            # user_id = User.objects.get(id=obj["user_id"]),
            status= obj["status"],
        )
        # user_id = obj["user_id"]
        if 'user_id' in obj:
            print("IN USER ID")
            new_device.user_id = User.objects.get(id=obj["user_id"])
        new_device.save()
        return new_device
     
    def to_representation(self, instance):
        return_usersinfo = {
            "id" : instance.device_group_details_id,
            "device_id": instance.device_id.server_device_id,
            "group_id": instance.group_id.device_group_id,
            "user_id":instance.user_id.id,
            "status": instance.status,
            "created_date": instance.created_date,
        }
        return return_usersinfo

    def update(self, instance, obj):
        print("in update user")
        if "device_id" in obj:
            instance.device_id = obj["device_id"]
        if "user_id" in obj:
            instance.user_id = obj["user_id"]
        if "group_id" in obj:
            instance.group_id = obj["group_id"]
        if "status" in obj:
            instance.status = obj["status"]
        instance.save()
        return instance



class Videoserializer(serializers.ModelSerializer):
    video_id = serializers.CharField(allow_null=True)
    title = serializers.CharField(allow_null=True)
    thumbnail_url = serializers.CharField(allow_null=True)
    created_by = serializers.IntegerField(allow_null=True)
    updated_by = serializers.IntegerField(allow_null=True)
    print("In Video serianlier")
    
    class Meta:
        model = Youtube
        fields = '__all__'


    def create(self, obj):
        print("inside create Youtube serilizer")
        new_youtube = Youtube.objects.create(
            video_id = obj["video_id"],
            title = obj["title"],
            thumbnail_url = obj["thumbnail_url"],
            created_by = obj["created_by"],
            updated_by = obj["updated_by"]
        )
        return new_youtube
     
    def to_representation(self, instance):
        return_usersinfo = {
            "youtube_url": "https://www.youtube.com/watch?v=",
            "id":instance.id,
            "video_id":instance.video_id,
            "title":instance.title,
            "thumbnail_url": instance.thumbnail_url,
            "created_by": instance.created_by,
            "updated_by": instance.updated_by,
            "created_date": instance.created_date,
            "updated_date": instance.updated_date
        }

        return return_usersinfo

    def update(self, instance, obj):
        print("in update user")
        if "video_id" in obj:
            instance.video_id = obj["video_id"]
        if "title" in obj:
            instance.title = obj["title"]
        if "thumbnail_url" in obj:
            instance.thumbnail_url = obj["thumbnail_url"]
        if "created_by" in obj:
            instance.created_by = obj["created_by"]
        if "updated_by" in obj:
            instance.updated_by = obj["updated_by"]
        if "device_token" in obj:
            instance.device_token = obj["device_token"]
        if "device_type" in obj:
            instance.device_type = obj["device_type"]
        if "status" in obj:
            instance.status = obj["status"]
        instance.save()
        return instance









class Linkserializer(serializers.ModelSerializer):
    title = serializers.CharField(allow_null = True)
    url = serializers.CharField(allow_null = True)
    link_belongs_to = serializers.CharField(allow_null = True)
    class Meta:
        model = Links
        fields = '__all__'

    def create(self, obj):
        print("inside create link serilizer")

        new_link = Links.objects.create(
            title = obj["title"],
            url = obj["url"],
            link_belongs_to = User.objects.get(id = obj["link_belongs_to"])
        )
        return new_link

    def to_representation(self, instance):
        print("in get links")
        link_belongs_to = None
        if link_belongs_to is not None:
            link_belongs_to = instance.link_belongs_to.id

        return_linksinfo = {
            "id":instance.id,
            "title": instance.title,
            "url": instance.url,
            "created_on":instance.created_on,
            "updated_on":instance.updated_on,
            "link_belongs_to":instance.link_belongs_to.id
        }
        return return_linksinfo

    def update(self, instance, obj):
        print("in update link")
        if "title" in obj:
            instance.title = obj["title"]
        if "url" in obj:
            instance.url = obj["url"]
        if "created_on" in obj:
            instance.created_on = obj["created_on"]
        if "updated_on" in obj:
            instance.updated_on = obj["updated_on"]
        print("validation done")
        if "link_belongs_to" in obj:
            instance.link_belongs_to = obj["link_belongs_to"]
        instance.save()
        return instance

class ProfileSerializerlinks(serializers.ModelSerializer):
    def to_representation(self, instance):
        link_belongs_to = None
        if link_belongs_to is not None:
            link_belongs_to= instance.link_belong_to.id

        return_socialsinfo= {
            "title": instance.title,
            "url": instance.url,
        }
        return return_socialsinfo

        



class Socialserializer(serializers.ModelSerializer):
    profile_belongs_to = serializers.CharField(allow_null = True)
    class Meta:
        model = Socials
        fields = '__all__'

    def create(self, obj):
        print("inside create Socials serializer")

        new_social = Socials.objects.create(
            social_media_name = obj["social_media_name"],
            profile_link = obj["profile_link"],
            profile_belongs_to =User.objects.get(id = obj["profile_belongs_to"])
        )
        return new_social

    def to_representation(self, instance):
        print("in get socials.")
        profile_belongs_to = None
        if profile_belongs_to is not None:
            profile_belongs_to= instance.profile_belong_to.id

        return_socialsinfo= {
            "id":instance.id,
            "social_media_name":instance.social_media_name,
            "profile_link":instance.profile_link,
            "profile_belongs_to":instance.profile_belongs_to.id
        }
        return return_socialsinfo

class ProfileSerializerSocials(serializers.ModelSerializer):
    def to_representation(self, instance):
        profile_belongs_to = None
        if profile_belongs_to is not None:
            profile_belongs_to= instance.profile_belong_to.id

        return_socialsinfo= {
            "social_media_name":instance.social_media_name,
            "profile_link":instance.profile_link,
        }
        return return_socialsinfo

        



class UserProfileSerializer(serializers.Serializer):
    first_name = serializers.CharField(allow_null=True)
    last_name = serializers.CharField(allow_null=True)
    bio = serializers.CharField(allow_null=True)
    link = serializers.CharField(allow_null=True)
    # links = serializers.SerializerMethodField()
    # socials = serializers.Serializer

    class Meta:
        model = User
        fields = {
            "first_name",
            "last-name",
            "bio",
            "link"
        }
    def to_representation(self, instance):
        print("in get_links")
        links = Links.objects.filter(link_belongs_to_id= instance.id)
        links_data = ProfileSerializerlinks(links, many=True)
        socials = Socials.objects.filter(profile_belongs_to_id= instance.id)
        socials_data = ProfileSerializerSocials(socials, many=True)
        return_user_info={
            "first_name":instance.first_name,
            "last-name":instance.last_name,
            "bio":instance.bio,
            "link":instance.link,
            "links_to share": links_data.data,
            "Socials": socials_data.data
        }
        return return_user_info


