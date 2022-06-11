from django.urls import path
from work import views

urlpatterns=[

    path('wrk',views.w),
    path('w',views.wrk,name='work')
]