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
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('reaction_test/', views.reaction_test_page, name='reaction_test'),
    # ADD THIS LINE
    path('api/save-score/', views.save_score_api, name='save_score_api'),
    path('community/', views.community_wall, name='community_wall'),
    path('champions_insights/', views.champion_roller, name='champion_roller'),
    path('quiz/', views.quiz_view, name='quiz_view'),
]
