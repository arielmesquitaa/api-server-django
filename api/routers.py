from api.authentication.viewsets import RegisterViewSet, LoginViewSet
from rest_framework import routers
from api.user.viewsets import UserViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'edit', UserViewSet, basename='users')

router.register(r'register', RegisterViewSet, basename='register')

router.register(r'login', LoginViewSet, basename='login')

urlpatterns = [
    *router.urls,
]