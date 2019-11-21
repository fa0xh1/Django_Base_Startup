from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('login/', LoginView.as_view(template_name='auth/login.html'),name="login_url"),
    path('logout/', LogoutView.as_view(next_page='login'),name="logout"),
    path('users/list', views.index, name="users_list"),
    path('users/add', views.AddUser, name="add_user"),
    path('users/update/<int:id>', views.UpdateUser, name="update_user"),
    path('users/delete/<int:id>', views.DeleteUser, name="delete_user"),  
]
