from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users
from .serializers import UserRegistrationSerializers
from django.contrib.auth import authenticate
from drf_yasg2.utils import swagger_auto_schema




class UserRegistrationAPIView(APIView):
    @swagger_auto_schema(request_body=UserRegistrationSerializers)
    def post(self,request):
        serializer=UserRegistrationSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"phone_namber": user["phone_namber"],"token":user["token"]})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





