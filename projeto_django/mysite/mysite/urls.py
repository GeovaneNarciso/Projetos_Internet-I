"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pools import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('question/<int:question_id>', views.exibir, name='exibir'),
    path('question/<int:question_id>/result/', views.results, name='results'),
    path('question/<int:question_id>/vote/', views.vote, name='vote'),
    path('question/<int:question_id>/manage/', views.manage, name='manage'),
    path('question/<int:question_id>/remove/<int:choice_id>/', views.remove, name='remove'),
    path('question/<int:question_id>/alter_status/', views.alter_status, name='alter_status'),
    path('question/<int:question_id>/add/<int:choice_id>/', views.add, name='add')
]
