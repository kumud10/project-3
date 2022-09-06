from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('activities',views.activities,name='activities'),
    path('blog',views.blog,name='blog'),
    path('competition',views.competition,name='competition'),
    path('events',views.events,name='events'),
    path('programs',views.programs,name='programs'),
    path('register',views.register,name='register'),
    path('staff',views.staff,name='staff'),
    path('application',views.application,name='application'),
]