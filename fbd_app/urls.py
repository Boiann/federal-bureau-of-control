from . import views
from django.urls import path

urlpatterns = [
    path("", views.EventList.as_view(), name="home"),
    path("splash/", views.splash, name="splash"),
    path("about/", views.about, name="about"),
    path('add_event/', views.AddEvent.as_view(), name='add_event'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
    path('like/<slug:slug>', views.EventApprove.as_view(), name='event_approve'),
    path('dislike/<slug:slug>', views.EventDisprove.as_view(), name='event_disprove'),
    path('event/edit/<slug:slug>/', views.UpdateEvent.as_view(), name='update_event'),
    path('delete/<slug:slug>/remove', views.DeleteEvent.as_view(), name='delete_event'),
]
