from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("prijavnice/", views.prijavnice, name="prijavnice"),
    path("prijavnica/", views.prijavnica, name="prijavnica"),
    path("kpi", views.kpi, name="kpi"),
    path('edit_prijavnica/<int:prijavnica_id>', views.edit_prijavnica, name='edit_prijavnica'),
    path("user_prijavnice/", views.user_prijavnice, name="user_prijavnice"),
    path("prijavnica/edit/<int:pk>/", views.user_edit_prijavnica, name="user_edit_prijavnica"),
]
 