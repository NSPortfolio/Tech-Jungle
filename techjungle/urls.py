from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib import admin
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('deletepost/<name_of_product>', views.deletepost, name='deletepost'),
    path('editpost/<name_of_product>', views.editpost, name='editpost'),
    path('saveitem/<name_of_product>', views.saveitem, name='saveitem'),
    path('removeitem/<name_of_product>', views.removeitem, name='removeitem'),
    path('admin/', admin.site.urls),
    path('saveditems/', views.SavedItems),
    path('log-in/', auth_views.LoginView.as_view(template_name="log_in.html")),
    path('sign-out/', auth_views.LogoutView.as_view(next_page="/")),
    path('sign-up/', views.sign_up),
    path('profile/', views.profile),
    path('buy/', views.buy),
    path('buy/computers/', views.computer),
    path('buy/cameras/', views.camera),
    path('buy/tablets/', views.tablet),
    path('buy/watches/', views.watch),
    path('buy/phones/', views.phone),
    path('buy/e-readers/', views.ereader),
    path('buy/storagedevices/', views.storagedevice),
    path('buy/projectors/', views.projector),
    path('buy/speakers/', views.speaker),
    path('buy/headphones-earbuds/', views.headphoneearbud),
    path('buy/printers/', views.printer),
    path('buy/microphones/', views.microphone),
    path('buy/mice/', views.mice),
    path('buy/keyboards/', views.keyboard),
    path('buy/appliances/', views.appliances),
    path('sell/', views.sell),
    path('contactseller/', views.email),
    path('home/', views.home),
    path('', views.firstpage),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)