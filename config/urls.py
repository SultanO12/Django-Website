from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _
from api.views import RegisterUserView

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    re_path(r'^rosetta/', include('rosetta.urls')),
    path(_('auth/'), include('authentication.urls')),
    path(_('api/'), include('api.urls')),
    path('api-auth', include('rest_framework.urls')),
    path('api-auth/register/', RegisterUserView.as_view(), name="register-api"),
    path('', include('main.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
