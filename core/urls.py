from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', home,name = 'home'),
    path('detail/<int:id>/', detailed_page, name = 'detailed-page'),
    path('filtr/', filtr_page, name = 'filtr-page'),
]