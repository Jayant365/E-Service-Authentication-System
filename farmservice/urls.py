
from django.contrib import admin
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

from accounts.views import login_page,password_reset,password_reset_done, RegisterView, guest_register_view,logout_user


urlpatterns = [
    # path('admin/', admin.site.urls),
    url('^admin/', admin.site.urls),
    url(r"^service/", include('service.urls', namespace='service')),
    url(r"^accounts/", include('accounts.urls', namespace='accounts')),

    url(r"^orders/", include('orders.urls', namespace='orders')),
    url(r'^$', views.main, name='main'),
    url('^', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
   urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
   urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

''' url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete')'''