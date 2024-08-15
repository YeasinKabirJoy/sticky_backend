from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()


def crete_jwt_token_pair(user:User):
    refresh = RefreshToken.for_user(user)
    refresh['username'] = user.username

    tokens = {
        "access":str(refresh.access_token),
        "refresh":str(refresh)
    }

    return tokens