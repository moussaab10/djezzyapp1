
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/citoyens/', include('greenev.urls.citoyen_urls')),
    path('api/associations/', include('greenev.urls.association_urls')),
    path('api/evenements/', include('greenev.urls.evenement_urls')),
    path('api/alerts/', include('greenev.urls.alert_urls')),
    path('api/notifications/', include('greenev.urls.notification_urls')),
    path('api/users/', include('greenev.urls.user_url')),
    path('api/reviews/', include('greenev.urls.review_urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
