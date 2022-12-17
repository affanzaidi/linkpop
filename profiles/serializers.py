from rest_framework import serializers
from django.db.models import Count
import datetime
from .models import User, Socials, Links

class Userserializer(serializers.ModelSerializer):
    first_name = serializers.CharField(allow_null=True)
    last_name = serializers.CharField(allow_null=True)
    bio = serializers.CharField(allow_null=True)
    # email = serializers.EmailField(allow_null=True)
    phone = serializers.CharField(allow_null=True)
    link = serializers.CharField(allow_null=True)
    print("In user serianlier")
    
    class Meta:
        model = User
        fields = '__all__'


    def create(self, obj):
        print("inside create user serilizer")
        new_user = User.objects.create(
            first_name = obj["first_name"],
            last_name = obj["last_name"],
            bio = obj["bio"],
            email = obj["email"],
            phone = obj["phone"],
            link= obj["link"]
        )
        return new_user
     
    def to_representation(self, instance):
        return_usersinfo = {
            "id":instance.id,
            "first_name":instance.first_name,
            "last_name":instance.last_name,
            "bio": instance.bio,
            "email": instance.email,
            "phone": instance.phone,
            "link": instance.link
        }

        return return_usersinfo

    def update(self, instance, obj):
        print("in update user")
        if "first_name" in obj:
            instance.first_name = obj["first_name"]
        if "last_name" in obj:
            instance.last_name = obj["last_name"]
        if "bio" in obj:
            instance.bio = obj["bio"]
        if "phone" in obj:
            instance.phone = obj["phone"]

        print("validation done")
        if "email" in obj:
            instance.email = obj["email"]
        if "link" in obj:
            instance.link = obj["link"]
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


