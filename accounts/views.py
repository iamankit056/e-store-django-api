from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import (
    ProfileSerializer,
    TokenSerializer,
    UserSerializer
)
from .models import (
    Profile,
    Address
)

def GetTokensForUser(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def GetProfile(user):
    try:
        return Profile.objects.get(user=user)
    except:
        return None


# Create your views here.
class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            response = {
                'error': 'Invalid Username and Password' 
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)        
        userProfile = GetProfile(user=user)
        serializeProfile = ProfileSerializer(userProfile)
        token = GetTokensForUser(user=user)
        serializeToken = TokenSerializer(token)
        response = {
            'user': serializeProfile.data,
            'token': serializeToken.data,
            'success': 'Login successesfully'
        }
        return Response(response, status=status.HTTP_200_OK)


class SignUp(APIView):
    def post(self, request):
        serializeUser = UserSerializer(data=request.data)
        if serializeUser.is_valid():
            user = serializeUser.save()            
            address = Address.objects.create()
            profile = Profile.objects.create(user=user, address=address)
            serializeProfile = ProfileSerializer(profile)
            token = GetTokensForUser(user)
            serializeToken = TokenSerializer(token)
            response = {
                'user': serializeProfile.data,
                'token': serializeToken.data,
                'success': 'Account created sucessesfully'
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'error': serializeUser.error_messages
        }
        return Response(response)