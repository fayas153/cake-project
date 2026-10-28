from django.urls import path

from . import views

urlpatterns = [
    path('cake/',views.CakeListCreateView.as_view()),
    path('cake/<int:id>/',views.CakeRetrieveUpdateDestroyView.as_view()),

    path('category/',views.CategoryCreateListView.as_view()),
    path('category/<int:pk>/',views.CategoryRetrieveUpdateDestroyView.as_view()),

    path('shape/',views.ShapeCreateListView.as_view()),
    path('shape/<int:pk>/',views.ShapeRetrieveUpdateDestroyView.as_view()),

    path('weight/',views.WeightCreateListView.as_view()),
    path('weight/<int:pk>/',views.WeightRetrieveUpdateDestroyView.as_view())
]