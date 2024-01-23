from django.urls import path
from .views import home, outdoor, indoor,  contact, futsal, basketball, cricket, detail_futsal, add_futsal

urlpatterns = [
    path("",home, name='home_page'),
    path("outdoor/", outdoor, name='outdoor_page'),
    path("indoor/", indoor, name='indoor_page'),
    path("contact/", contact, name='contact_us_page'),
    path("futsal/", futsal, name="futsal_page"),
    path("basketball/", basketball, name="basketball_page"),
    path("cricekt/", cricket, name="cricket_page"),
    path('detail-futsal/<int:id>/', detail_futsal, name="detail_futsal"),
    path('add-futsal', add_futsal, name='add_futsal'),
    
]
