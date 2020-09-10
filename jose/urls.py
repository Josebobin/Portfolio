from django.contrib import admin
from django.urls import include, path
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url
import os
from django.views.static import serve as staticserve

 

 
urlpatterns = [
    path('admin/', admin.site.urls),     
    url( r'^login/$',auth_views.LoginView.as_view(template_name="main/registration/login.html"), name="login"),
     
    url(r'^logout/$', auth_views.LogoutView, {'template_name': 'logged_out.html'}, name='logout'),
    #url(r'^signup/', views.SignupPage.as_view(), name='sign_up'),
    path('accounts/',include('django.contrib.auth.urls')),
     
    path('', include('website.urls')),
    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'), name='password_reset_complete'), 
     
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'website.views.error_404_view' 