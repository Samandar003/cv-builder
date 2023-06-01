
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import ResumeAPIView
from main.serializers import ResumeSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cv/', ResumeAPIView.as_view())
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
