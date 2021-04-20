from django.urls import path
from . import views

urlpatterns=[
    
    path('login/',views.loginPage,name='login'),
    path('login/as_user/',views.as_user,name='as_user'),
    # path('login/as_librarian/',views.as_librarian,name='as_librarian'),
    path('signup/',views.signup,name='signup'),
    path('library/',views.index,name='index'),
    path('logout/',views.logoutUser,name='logout'),
    path('library/details/',views.details,name='details'),
]