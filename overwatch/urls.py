from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('beacon/', include("beacon.urls")),
    path('account/', include("account.urls")),
]
