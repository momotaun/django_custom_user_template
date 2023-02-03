from dj_rest_auth.views import LoginView
from .serializer import UserLoginSerializer

class APILoginVIew(LoginView):
    # permission_classes = ['AllowAny']
     def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user', None)
        self.login(request, user)
        return super().post(request, format=None)