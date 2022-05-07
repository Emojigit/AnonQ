"""AnonQ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/q/list/', m_api_q_list),
    path('api/q/stat/<int:id>/', m_api_q_stat),
    path('api/a/stat/<int:id>/', m_api_a_stat),
    path('ask.post/', m_gui_ask_post),
    path('ask/', m_gui_ask),
    path('question/<int:id>', m_gui_question),
    path('answer/<int:id>', m_gui_answer),
    path('',m_gui_list)
]
