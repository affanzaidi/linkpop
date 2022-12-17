from django.shortcuts import render ,get_object_or_404
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import Userserializer, Linkserializer, Socialserializer, UserProfileSerializer
from .models import User, Links, Socials

# Create your views here.

class UserInfo(APIView):
    def post(self, request, *args, **kwargs):
        userinfo_data = JSONParser().parse(request)
        userdata = Userserializer(data=userinfo_data)
        if userdata.is_valid():
            userdata.save()
            return Response(userdata.data, status=status.HTTP_201_CREATED)
        
        return Response(userdata.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user_info_data = User.objects.all()
        userdata = Userserializer(user_info_data, many=True)
        return Response( userdata.data)
    

class SingleUserInfo(APIView):
    def get(self, request, id):
        user = User.objects.filter(id=id)
        userdata = Userserializer(user, many=True)
        return Response(userdata.data)
 
    def delete(self, request, id):
        user = get_object_or_404(User, pk = id)
        user.delete()
        return Response({"Success":"True"},status=status.HTTP_200_OK)

    def put(self,request, id):
        data = JSONParser().parse(request)
        print("data parsed")
        update = get_object_or_404(User, pk=id)
        print(data["first_name"])
        update_details = Userserializer(
            update, data = data)
        # print(update_details.first_name)
        if update_details.is_valid():
            print(":valid data")
            update_details.save()
            return Response(update_details.data, status=status.HTTP_200_OK)
        return Response(update_details.errors, status=status.HTTP_400_BAD_REQUEST)




class LinkInfo(APIView):
    def post(self, request, *args, **kwargs):
        linkinfo_data = JSONParser().parse(request)
        linkdata = Linkserializer(data=linkinfo_data)
        if linkdata.is_valid():
            linkdata.save()
            return Response(linkdata.data, status=status.HTTP_201_CREATED)
        
        return Response(linkdata.data, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        link_info_data = Links.objects.all()
        linkdata = Linkserializer(link_info_data, many=True)
        return Response(linkdata.data)

class SingleUserLinks(APIView):

    def get(self, request, id):
        links = Links.objects.filter(link_belongs_to_id=id)
        linksdata = Linkserializer(links, many=True)
        return Response(linksdata.data)
    
    def delete(self, request, id):
        link = get_object_or_404(Links, pk = id)
        link.delete()
        return Response({"Success":"True"},status=status.HTTP_200_OK)

    def put(self,request, id):
        data = JSONParser().parse(request)
        update = get_object_or_404(Links, pk=id)
        update_details = Linkserializer(
            update, data = data)
        if update_details.is_valid():
            print(":valid data")
            update_details.save()
            return Response(update_details.data, status=status.HTTP_200_OK)
        return Response(update_details.errors, status=status.HTTP_400_BAD_REQUEST)



class SocialInfo(APIView):
    def post(self, request, *args, **kwargs):
        socialinfo_data = JSONParser().parse(request)
        socialdata = Socialserializer(data=socialinfo_data)
        if socialdata.is_valid():
            socialdata.save()
            return Response(socialdata.data, status=status.HTTP_201_CREATED)
        
        return Response(socialdata.data, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        social_info_data = Socials.objects.all()
        socialdata = Socialserializer(social_info_data, many=True)
        return Response(socialdata.data)

class SingleUserSocials(APIView):
    def get(self, request, id):
        socials = Socials.objects.filter(profile_belongs_to_id=id)
        socialdata = Socialserializer(socials, many=True)
        return Response(socialdata.data)

    def delete(self, request, id):
        socials = get_object_or_404(Socials, pk = id)
        socials.delete()
        return Response({"Success":"True"},status=status.HTTP_200_OK)


class GetAllUserinfo(APIView):
    def get(self, request, id):
        print("Inside all user info")

        try:
            user = User.objects.get(pk=id)
            serilizer = UserProfileSerializer(user)
            print("in try block")
            return Response(serilizer.data)
        except:
            return Response({"stutus":"fail"})


 
        
        