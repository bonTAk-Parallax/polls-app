from django.urls import path
from polls_app import views


app_name = "polls_app"
urlpatterns = [
    path('', views.IndexView.as_view(), name="base-view" ),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
]

# urlpatterns = [
#     path('', views.index, name="base-view" ),
#     path('<int:question_id>/', views.detail, name="detail"),
#     path('<int:question_id>/results/', views.results, name="results"),
#     path('<int:question_id>/vote/', views.vote, name="vote"),
# ]