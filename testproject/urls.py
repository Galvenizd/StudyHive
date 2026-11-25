from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from testApp.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    # Built-in login / logout pages (uses templates/registration/login.html)
    path('accounts/signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
