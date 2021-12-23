from dataCovid.views import add_krisan, add_krisan_flutter
from django.urls.conf import path



urlpatterns = [

    path('', add_krisan, name = "data-covid19"),
    # path('covid19-provinsi', info_provinsi, name="data-covid19-provinsi"),

    path('/flutter', add_krisan_flutter),
]