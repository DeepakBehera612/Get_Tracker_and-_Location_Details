"""api_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from api_tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),



    # tracker
    path('', views.show_tracker_data_from_db),

    path(r'^$', views.tracker_button),

    path('^insert_tracker_data_todb',
         views.insert_tracker_data_todb, name='script'),

    path('location/<int:id>', views.show_tracker_data_from_db,
         name='show_tracker_data_from_db'),





    # location
    path('', views.show_location_data_from_db),
    path(r'^$', views.location_button),

    path('^insert_locations_data_todb',
        views.insert_locations_data_todb, name='location_script'),

    path('location/<int:id>/', views.show_location_data_from_db),
]
