"""invid19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
import diskusi.urls as diskusi

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("users.urls")),
    path("login", user_views.loginUser, name="login"),
    path("logout", user_views.logoutUser, name="logout"),
    path("signup", user_views.signupUser, name="signup"),
    path(
        "activate/<uidb64>/<token>/",
        user_views.activate,
        name="activate",
    ),
    path("", include("main.urls")),
    path("diskusi/", include(diskusi)),
    path("artikel/",include("artikel.urls")),
    path("data-covid/", include("dataCovid.urls")),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
