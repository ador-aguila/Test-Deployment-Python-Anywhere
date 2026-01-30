from django.urls import path
from . import views 




urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),

    path('exam', views.exam, name='exam'),
    path('exam-site', views.exam_site, name='exam-site'),
    path('exam-result', views.exam_result, name='exam-result'),

    path('login', views.loginPage, name='loginPage'),
    path('logout', views.logoutUser, name='logout'),
    path('signup', views.signup, name='signup'),

    path('edit-account',views.editAccount,name="edit-account"),

    
]
