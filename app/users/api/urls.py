from django.urls import path, include, re_path
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView
from .views import APILoginVIew

urlpatterns = [
    # Third party Urls
    # path('login/', APILoginVIew.as_view(), name='api_login'),
    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),

    # path('register/', RegisterView.as_view(), name='rest_register'),
    # path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view()),
    path('verify-email', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),

    # Custom Urls
    # path('users/api/', include('users.api.urls')),
]