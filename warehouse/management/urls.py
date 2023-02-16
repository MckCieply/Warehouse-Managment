from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup_request, name="signup"),
    path('login', views.login_request, name="login"),
    path('logout', LogoutView.as_view(template_name='registration/logout.html') , name="logout"),
    path('<str:city>', views.state, name="city"),
    path('<str:city>/<int:id>', views.update, name="update"),
]