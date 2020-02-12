from django.conf.urls import url,include

app_name = "accounts"

from .views import login_page,password_reset    , RegisterView, guest_register_view,logout_user,activate

urlpatterns = [
    # /service/ homepage with no extra information

    url(r'^login_user/$', login_page , name='login_user'),
    url(r'^logout/$', logout_user , name='logout_user'),
#    path(        'change-password/',   auth_views.PasswordChangeView.as_view(template_name='accounts/change-password.html'), ),

    url(r'^register/$', RegisterView, name='register'),
    url(r'^subscribe_us/$', guest_register_view, name='guest_register'),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),

]