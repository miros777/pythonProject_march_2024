from django.contrib.auth import \
    get_user_model  # для юзера, так якщо відразу в queryset модель юзера покласти, то потім будуть помилки

from rest_framework import serializers, status
from rest_framework.decorators import permission_classes
from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema

from core.services.email_service import EmailService

from apps.auth.serializers import EmailSerializer
from apps.users.serializers import UserSerializer

UserModel = get_user_model()

class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes=(AllowAny,)

class UserMeView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request):
       user =  self.request.user
       serializer = UserSerializer(user)
       return Response(serializer.data, status=status.HTTP_200_OK)

class UserBanView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    @swagger_auto_schema(request_body=Serializer)
    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserUnBanView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    @swagger_auto_schema(request_body=Serializer)
    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserToAdminView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    @swagger_auto_schema(request_body=Serializer)
    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AdminToUserView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    @swagger_auto_schema(request_body=Serializer)
    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ErrorSerializer(serializers.Serializer):
    details = serializers.CharField()

class TestEmailView(GenericAPIView):
    permission_classes = (AllowAny, )

    def get_serializer_class(self):
        pass

    @swagger_auto_schema(responses={status.HTTP_200_OK:EmailSerializer, status.HTTP_400_BAD_REQUEST:ErrorSerializer})
    def get(self, *args, **kwargs):
        EmailService.send_test()
        return Response(status=status.HTTP_200_OK)


