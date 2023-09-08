"""Defines URL patterns for journal."""

from django.urls import path

from . import views

app_name = 'journal'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page that shows all public topics.
    path('public_topics/', views.public_topics, name='public_topics'),
    # Detail page for a single public topic.
    path('public_topics/<int:topic_id>/', views.public_topic, name='public_topic'),
    # Page for corona stats.
    path('public_topics/corona_stats_ch/', views.corona_stats_ch, name='corona_stats_ch'),
    # URL for /dashboard/covid.
    path('covid/', views.corona_stats_ch, name='dashboard_covid'),
    # URL for /dashboard/us-air-passengers.
    path('us-air-passengers/', views.us_air_passenger_stats, name='dashboard_us-air-passengers'),
    # Page for visitor details.
    path('visitors/', views.visitors, name='visitors'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]