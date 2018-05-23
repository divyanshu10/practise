from django.urls import path
from login import views
app_name='login'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
   
]
