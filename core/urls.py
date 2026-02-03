from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', home,name = 'home'),
    path('detail/<int:id>/', detailed_page, name = 'detailed-page'),
    path('filtr/', filtr_page, name = 'filtr-page'),
    path('filtr-rus/', filtr_page_rus, name = 'filtr-page-rus'),
    path('filtr-turk/', filtr_page_turk, name = 'filtr-page-turk'),
    path('filtr-ing/', filtr_page_ing, name = 'filtr-page-ing'),
    path('news/<int:id>/',news_page, name = 'news_page'),
    path('event/<int:id>/',event_page, name = 'event_page'),
    path('club/<int:id>/',club_page, name = 'club_page'),

]