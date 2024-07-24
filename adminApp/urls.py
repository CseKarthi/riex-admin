from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.admin,name="login"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout',views.logout_user,name="logout"),
    path('updateProfile',views.updateProfile,name="updateProfile"),
    path('newInstitution',views.newInstitution,name="newInstitution"),
    path('institution',views.institution,name="institution")
]