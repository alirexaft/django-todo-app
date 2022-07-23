from django.urls import path
from .views import Login, SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login')
]
