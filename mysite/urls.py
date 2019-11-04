from django.contrib import admin
from django.urls import include, path
import polls.views as views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',views.IndexView.as_view()),
]
