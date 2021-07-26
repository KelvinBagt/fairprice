#urls.py is used for for storing all the urls to access various paths
from django.contrib import admin
from django.urls import path
from journals import views 

urlpatterns = [
    path('admin/', admin.site.urls), #admin path
    path('journals/', views.journal, name='journals'), #view all journals path
    path('journals/<int:journal_id>/', views.journal_detail, name='journal_detail') #display specific journal 
]
