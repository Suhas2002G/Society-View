from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home),
    # path('login', views.user_login),
    # path('register', views.register),
    # path('logout', views.user_logout),
    
    



]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)