from rest_framework.generics import ListCreateAPIView

from django.contrib.auth import get_user_model # для юзера, так якщо відразу в queryset модель юзера покласти, то потім будуть помилки

from apps.users.serializers import UserSerializer

UserModel = get_user_model()

class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
