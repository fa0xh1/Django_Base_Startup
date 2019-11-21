from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('accounts/',include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
