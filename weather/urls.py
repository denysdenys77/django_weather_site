from django.urls import path
from .views import (SearchPageView, DeleteCityView,
                    CityWeatherDetailView, UserCitiesView,
                    SearchResultView, AddedCityView)

urlpatterns = [
    path('', SearchPageView.as_view(), name='search_page'),
    path('search/', SearchResultView.as_view(), name='search_result_page'),
    path('city_weater_class_based/<str:cityname>', CityWeatherDetailView.as_view(), name='city_weather_class_based'),
    path('user_cities_view/', UserCitiesView.as_view(), name='user_cities_view'),
    path('added_city/<str:cityname>', AddedCityView.as_view(), name='added_city_view'),
    path('delete_city/<str:cityname>', DeleteCityView.as_view(), name='delete_city_view'),
]