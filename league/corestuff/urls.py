from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('tilt-meter/', views.tilt_meter_page, name='tilt_meter_page'),  # Tilt Meter page
    path('api/tilt-meter/', views.tilt_meter_api, name='tilt_meter_api'),  # Tilt Meter API
    path('why-did-i-lose/', views.why_did_i_lose_page, name='why_did_i_lose'),
    path('api/why-did-i-lose/', views.why_did_i_lose_api, name='why_did_i_lose_api'),
    path('api/chat-translator/', views.chat_translator_api, name='chat_api'),
    path('api/patch-notes/', views.patch_notes_api, name='patch_notes_api'),
    path('api/should-i-queue/', views.should_i_queue_api, name='should_i_queue_api'),
    path('reaction-test/', views.reaction_test_page, name='reaction_test'),
]
