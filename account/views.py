from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from .serilizers import UserRegestrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from account.renderer import UserRenderer

class UserRegestrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegestrationSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print('dlkjs')
            return Response({"msg": "User has been registered sucessfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response({"msg": "User has been loged in sucessfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"errors": {'non_field_errors': ["Email or Password is not valid"]}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

