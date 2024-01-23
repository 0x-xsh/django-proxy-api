
import debug_toolbar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("news.urls")),
     path('__debug__/', include(debug_toolbar.urls)),
]
