from django.urls import path
from user import views

urlpatterns = [

    path('fun',views.fun),
    path('fun1',views.fun1),
    path('u',views.us, name='uuu'),
    path('user',views.user, name='aaaa'),
]