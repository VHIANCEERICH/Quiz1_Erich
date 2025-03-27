from django.urls import path


from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("erich", views.erich, name="erich"),
    path("jhobs", views.jhobs, name="jhobs")
]
