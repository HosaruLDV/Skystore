from django.urls import path
from sbl.views import home, contacts
from sbl.apps import SblConfig

app_name = SblConfig.name

urlpatterns = [
    path('', home , name = 'home'),
    path('contacts/', contacts, name = 'contacts')
]