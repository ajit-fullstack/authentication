from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from .serilizers import UserRegestrationSerializer

class UserRegestrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegestrationSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print('dlkjs')
            return Response({"msg": "User has been registered sucessfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

