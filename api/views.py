from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def LoginApi(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},

                        status=HTTP_400_BAD_REQUEST,

                        )
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND,

                        )
    token, _ = Token.objects.get_or_create(user=user)

    return Response(
        {'msg':"Successfully Logged in",
            'token': token.key
        },
        status=HTTP_200_OK,
    )


@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAdminUser,))
def UserListApi(request):
    user=User.objects.all().values()

    return Response(
        user,
        status=HTTP_200_OK,
    )


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def UserDetailsApi(request):
    if request.user.is_superuser:
        user = User.objects.all().values()
    else:
        user=User.objects.filter(id=request.user.id).values()

    if not user:
        return Response({'error': 'No Users Found'},
                        status=HTTP_404_NOT_FOUND,

                        )
    return Response(
        user,
        status=HTTP_200_OK,
    )
