from django.contrib.auth import \
    get_user_model  # для юзера, так якщо відразу в queryset модель юзера покласти, то потім будуть помилки
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.serializers import UserSerializer

UserModel = get_user_model()

class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

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

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserUnBanView(GenericAPIView):
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserToAdminView(GenericAPIView):
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AdminToUserView(GenericAPIView):
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)



