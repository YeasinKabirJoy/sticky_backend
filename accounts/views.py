from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from .tokens import crete_jwt_token_pair


class SignUp(APIView):
    serializer_class = UserSerializer

    def post(self,request:Request):
        data = request.data
        print(data)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message':'user created',
                'data': serializer.data
            }
            return Response(data=response,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):

    def post(self,request:Request):

        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email,password=password)
        if user is not None:
            tokens = crete_jwt_token_pair(user)
            response = {
                "message": "Login Successful",
                "tokens":tokens
            }
            return Response(data=response,status=status.HTTP_200_OK)
        return Response(data={"message":"Wrong Password or Email"},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):

        data = {
            "user": str(request.user),
            "auth": str(request.auth)
        }

        return Response(data=data,status=status.HTTP_200_OK)


class Logout(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        try:
            token = request.data.get('refresh_token')
            if not token:
                return Response(data={"message": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

            token_obj = RefreshToken(token)
            token_obj.blacklist()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
