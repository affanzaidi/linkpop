from django.shortcuts import render ,get_object_or_404
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import * #Userserializer, Linkserializer, Socialserializer, UserProfileSerializer
from .models import *

# Create your views here.

class UserInfo(APIView):
    def post(self, request, *args, **kwargs):
        userinfo_data = JSONParser().parse(request)
        userdata = Userserializer(data=userinfo_data)
        if userdata.is_valid():
            userdata.save()
            return_data = {
                "data": userdata.data,
                 "message": "Signup successfully",   
                 "response": "true" 
            }
            return Response(return_data, status=status.HTTP_201_CREATED)
        
        return Response(userdata.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user_info_data = User.objects.all()
        userdata = Userserializer(user_info_data, many=True)
        return Response( userdata.data)


class Login(APIView):
    def post(self, request, *args, **kwargs):
        loginInfo = JSONParser().parse(request)
        mobile_number = loginInfo['mobile_number']
        password = loginInfo['password']
        
        user = User.objects.filter(mobile_number=mobile_number, password=password)
        userdata = Userserializer(user, many=True)
        print(userdata.data)
        if userdata.data:
            return_data = {
                    "data": userdata.data,
                    "message": "Login Successfully",   
                    "response": "true" 
                }
            return Response(return_data, status=status.HTTP_201_CREATED)
        return_data = {
            "message":"Mobile not registered with us / password is incorrect",
            "response":"false"
            } 
        return Response(return_data, status=status.HTTP_400_BAD_REQUEST)
    
    
class Check_mobile_exists(APIView):
    def post(self, request, *args, **kwargs):
        loginInfo = JSONParser().parse(request)
        mobile_number = loginInfo['mobile_number']
        
        user = User.objects.filter(mobile_number=mobile_number)
        userdata = Userserializer(user, many=True)
        print(userdata.data)
        if userdata.data:
            return_data = {
                    "data": userdata.data,
                    "message": "Mobile no is registered with us.",   
                    "response": "true" 
                }
            return Response(return_data, status=status.HTTP_201_CREATED)
        return_data = {
            "message":"Mobile not registered with us.",
            "response":"false"
            } 
        return Response(return_data, status=status.HTTP_400_BAD_REQUEST)


   
class Check_user_details(APIView):
    def post(self, request, *args, **kwargs):
        loginInfo = JSONParser().parse(request)
        password = loginInfo['password']
        user_id = loginInfo['user_id']
        
        user = User.objects.filter(password=password, id = user_id)
        userdata = Userserializer(user, many=True)
        print(userdata.data)
        if userdata.data:
            return_data = {
                "message":"Password matching with database.",
                "response":"true"
                }
            return Response(return_data, status=status.HTTP_201_CREATED)
        return_data = {
            "message":"Password not matching with database.",
            "response":"false"
            } 
        return Response(return_data, status=status.HTTP_400_BAD_REQUEST)


class Reset_password(APIView):
    def post(self, request, *args, **kwargs):
        loginInfo = JSONParser().parse(request)
        password = loginInfo['old_password']
        user_id = loginInfo['user_id']
        new_passowrd = loginInfo['new_password']
        user = get_object_or_404(User,  id = user_id, password=password)
        user.password = new_passowrd
        user.save()
        return_data = {
                "message":"Password changed successfully.",
                "response":"true"
                }
        return Response(return_data, status=status.HTTP_201_CREATED)



class DeviceInfo(APIView):
    def post(self, request, *args, **kwargs):
        userinfo_data = JSONParser().parse(request)
        userdata = Deviceserializer(data=userinfo_data, partial = True)
        if userdata.is_valid():
            userdata.save()
            return_data = {
                "data": userdata.data,
                 "message": "Device saved successfully",   
                 "response": "true" 
            }
            return Response(return_data, status=status.HTTP_201_CREATED)
        
        return Response(userdata.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        Device_info_data = Device.objects.all()
        Devicedata = Deviceserializer(Device_info_data, many=True)
        return Response( Devicedata.data)




class UserDevice(APIView):
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        user_id = data['user_id']
        print(user_id)
        all_device = Device.objects.filter(user_id = user_id)
        userdata = Deviceserializer(all_device, many = True)
        print(userdata.data)
        if userdata.data:
            return_data = {
                    "data": userdata.data,
                    "message": "Device saved successfully",   
                    "response": "true" 
                }
            return Response(return_data, status=status.HTTP_201_CREATED)
        return_data = {"data":[],"response":"false"} 
        return Response(return_data, status=status.HTTP_400_BAD_REQUEST)




class UserDeviceType(APIView):
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        user_id = data['user_id']
        device_type_list  = [] 
        all_device = Device.objects.filter(user_id = user_id)
        userdata = Deviceserializer(all_device, many = True)
        if userdata.data:
            for data in userdata.data:
                device_type = Device_Type.objects.filter(pk=int(data['device_type']))
                device_type_data = DeviceTypeserializer(device_type, many = True)
                device_type_list.append(device_type_data.data)
            
                return_data = {
                        "data": device_type_list,
                        "message": "Device type found",   
                        "response": "true" 
                    }
                return Response(return_data, status=status.HTTP_201_CREATED)
        return_data = {"data":[],"response":"false"} 
        return Response(return_data, status=status.HTTP_400_BAD_REQUEST)


class SingleDeviceInfo(APIView):
    def get(self, request, id):
        device = Device.objects.filter(server_device_id=id)
        devicedata = Deviceserializer(device, many=True)
        return Response(devicedata.data)
 
    def delete(self, request, id):
        Device = get_object_or_404(Device, pk = id)
        Device.delete()
        return Response({"Success":"True"},status=status.HTTP_200_OK)

    def put(self,request, id):
        data = JSONParser().parse(request)
        print("data parsed")
        update = get_object_or_404(Device, pk=id)
        print(data["first_name"])
        update_details = Deviceserializer(
            update, data = data)
        # print(update_details.first_name)
        if update_details.is_valid():
            print(":valid data")
            update_details.save()
            return Response(update_details.data, status=status.HTTP_200_OK)
        return Response(update_details.errors, status=status.HTTP_400_BAD_REQUEST)



class DeviceTypeInfo(APIView):
    def post(self, request, *args, **kwargs):
        userinfo_data = JSONParser().parse(request)
        userdata = DeviceTypeserializer(data=userinfo_data, partial = True)
        if userdata.is_valid():
            userdata.save()
            return_data = {
                "data": userdata.data,
                 "message": "Device saved successfully",   
                 "response": "true" 
            }
            return Response(return_data, status=status.HTTP_201_CREATED)
        
        return Response(userdata.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        Device_info_data = Device_Type.objects.all()
        Devicedata = DeviceTypeserializer(Device_info_data, many=True)
        return Response( Devicedata.data)



class SingleDeviceTypeInfo(APIView):
    def get(self, request, id):
        device = Device_Type.objects.filter(pk=id)
        devicedata = DeviceTypeserializer(device, many=True)
        print(devicedata.data)
        return Response(devicedata.data)
 
    def delete(self, request, id):
        device = get_object_or_404(Device_Type, pk = id)
        device.delete()
        return Response({"Success":"True"},status=status.HTTP_200_OK)

    def put(self,request, id):
        data = JSONParser().parse(request)
        print("data parsed")
        update = get_object_or_404(Device_Type, pk=id)
        print(data["first_name"])
        update_details = DeviceTypeserializer(
            update, data = data)
        # print(update_details.first_name)
        if update_details.is_valid():
            print(":valid data")
            update_details.save()
            return Response(update_details.data, status=status.HTTP_200_OK)
        return Response(update_details.errors, status=status.HTTP_400_BAD_REQUEST)


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


class VideoInfo(APIView):
    def post(self, request, *args, **kwargs):
        Videoinfo_data = JSONParser().parse(request)
        Videodata = Videoserializer(data=Videoinfo_data)
        if Videodata.is_valid():
            Videodata.save()
            return Response(Videodata.data, status=status.HTTP_201_CREATED)
        
        return Response(Videodata.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        Video_info_data = Youtube.objects.all()
        Videodata = Videoserializer(Video_info_data, many=True)
        return Response( Videodata.data)
    
class SingleYoutubeInfo(APIView):
    def get(self, request, id):
        video = Youtube.objects.filter(id=id)
        videodata = Videoserializer(video, many=True)
        return Response(videodata.data)
 
    def delete(self, request, id):
        video = get_object_or_404(Youtube, pk = id)
        video.delete()
        return Response({"Success":"True"},status=status.HTTP_200_OK)

    def put(self,request, id):
        data = JSONParser().parse(request)
        print("data parsed")
        update = get_object_or_404(Youtube, pk=id)
        update_details = Videoserializer(update, data = data)
        if update_details.is_valid():
            update_details.save()
            return Response(update_details.data, status=status.HTTP_200_OK)
        return Response(update_details.errors, status=status.HTTP_400_BAD_REQUEST)




class SingleDeviceInfo(APIView):
    def get(self, request, id):
        device = Device.objects.filter(server_device_id=id)
        devicedata = Deviceserializer(device, many=True)
        return Response(devicedata.data)
 
    def delete(self, request, id):
        Device = get_object_or_404(Device, pk = id)
        Device.delete()
        return Response({"Success":"True"},status=status.HTTP_200_OK)

    def put(self,request, id):
        data = JSONParser().parse(request)
        print("data parsed")
        update = get_object_or_404(Device, pk=id)
        print(data["first_name"])
        update_details = Deviceserializer(
            update, data = data)
        # print(update_details.first_name)
        if update_details.is_valid():
            print(":valid data")
            update_details.save()
            return Response(update_details.data, status=status.HTTP_200_OK)
        return Response(update_details.errors, status=status.HTTP_400_BAD_REQUEST)



class GroupInfo(APIView):
    def post(self, request, *args, **kwargs):
        userinfo_data = JSONParser().parse(request)
        userdata = DeviceGroupserializer(data=userinfo_data, partial = True)
        if userdata.is_valid():
            userdata.save()
            return_data = {
                "data": userdata.data,
                 "message": "Device saved successfully",   
                 "response": "true" 
            }
            return Response(return_data, status=status.HTTP_201_CREATED)
        
        return Response(userdata.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        Device_info_data = Device_Group.objects.all()
        Devicedata = DeviceGroupserializer(Device_info_data, many=True)
        return Response( Devicedata.data)


class GroupDetailsInfo(APIView):
    def post(self, request, *args, **kwargs):
        userinfo_data = JSONParser().parse(request)
        userdata = DeviceGroupDetailSerializer(data=userinfo_data, partial = True)
        if userdata.is_valid():
            userdata.save()
            return_data = {
                "data": userdata.data,
                 "message": "Device saved successfully",   
                 "response": "true" 
            }
            return Response(return_data, status=status.HTTP_201_CREATED)
        
        return Response(userdata.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        Device_info_data = Device_group_Details.objects.all()
        Devicedata = DeviceGroupDetailSerializer(Device_info_data, many=True)
        return Response( Devicedata.data)



class SaveGroup(APIView):
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request) 
        is_update = data["is_update"]
        device_data = []
        if is_update == "0":
            print("in create")
            devicedata = DeviceGroupserializer(data=data, partial = True)
            if devicedata.is_valid():
                devicedata.save()
                group_id = devicedata.data["id"]
                devices = data["devices"]
                u_id = data["user_id"]
                sts = data['status']
                devices = devices.split(",")
                for device in devices:
                    post_data = {
                        "device_id": device,
                        "group_id": group_id,
                        "user_id": u_id,
                        "status": sts,
                    }
                    group_device_data = DeviceGroupDetailSerializer(data=post_data, partial = True)
                    if group_device_data.is_valid():
                        group_device_data.save()
                        print(group_device_data.data)
                    data = Device.objects.get(pk = device)
                    device_serializer = Deviceserializer(data)
                    device_data.append(device_serializer.data)
                    print(device_serializer.data)
                data = devicedata.data
                data["devices"] = device_data
                return_data = {
                    "data":data,
                        
                    "message": "Group Created successfully",   
                    "response": "true"
                }   
                
            return Response(return_data, status=status.HTTP_201_CREATED)
        
        return Response("userdata.errors", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        Device_info_data = Device_Group.objects.all()
        Devicedata = DeviceGroupserializer(Device_info_data, many=True)
        return Response( Devicedata.data)
    
class UserGroups(APIView):
   def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request) 
        user_id = data["user_id"]
        Device_info_data = Device_Group.objects.filter(user_id= user_id)
        Devicedata = DeviceGroupserializer(Device_info_data, many=True)
        if Devicedata.data:
            return_data = {
                "group": Devicedata.data,
                "message": "device group list",   
                "response": "true"
            }
            return Response(return_data)   
        return_data =  {"message":"device group not found","response":"false"}
        return Response(return_data)

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


 
        
        