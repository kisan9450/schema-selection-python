from django.contrib import admin
from django.urls import path
from .views import nl_to_sql_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/nl-to-sql/', nl_to_sql_api, name='nl_to_sql_api'),
]
