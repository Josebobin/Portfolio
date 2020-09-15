from django.urls import path
from . import views

#app_name = "main" 

urlpatterns = [
    #path('', views.homepage, name="homepage"),
    path('', views.home, name="home"),
    path("password_reset",  views.password_reset_request, name="password_reset"),
    path('print/', views.portfolioprintview, name="print"),
    path('thank-you', views.contact, name="thank-you"),
    path('sign_up/',views.sign_up,name="sign-up"),
    path('filter/',views.filter,name="filter"),
     

     
    #path('article', ArticleDetailView.as_view(), name="article-detail"),
    #path('lifting/', views.test, name="lifting"),    
    #path('brand/', views.brand, name="brand"),
 
]
 