from . import views
from django.urls import path

urlpatterns = [
    path("", views.splash, name="splash"),
    path("reports/", views.EventList.as_view(), name="reports"),
    path("home/", views.home, name="home"),
    path("logout/", views.logout, name="logout"),
    path("my-events/", views.UserEventList.as_view(), name="my_events"),
    path('add_event/', views.AddEvent.as_view(), name='add_event'),
    path(
        'reports/<slug:slug>/',
        views.EventDetail.as_view(),
        name='event_detail'),
    path(
        'like/<slug:slug>',
        views.EventApprove.as_view(),
        name='event_approve'),
    path(
        'dislike/<slug:slug>',
        views.EventDisprove.as_view(),
        name='event_disprove'),
    path(
        'event/edit/<slug:slug>/',
        views.UpdateEvent.as_view(),
        name='update_event'),
    path(
        'delete/<slug:slug>/remove',
        views.DeleteEvent.as_view(),
        name='delete_event'),
]
