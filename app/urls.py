from django.urls import path, include
from . import views
urlpatterns = [
<<<<<<< HEAD

    # path('upload/', views.upload),
    # path('upload_inverse/', views.upload_inverse),
=======
<<<<<<< HEAD

    path('upload/', views.upload),
    path('upload_inverse/', views.upload_inverse),
>>>>>>> c9dc42488970bd77d009e4a706fab4731398f6b8
    path('index/', views.index),
    path('',views.index),
    path('read_json/',views.read_json),
    path('search/',views.search),
<<<<<<< HEAD
    path('add_word/',views.add_word),
=======
=======
    # path('upload/', views.upload),
    path('', views.index),
    path('page2/', views.page2),
    # path('read/', views.read),
    # path('home/', views.home),
    # path('search/', views.search),
    # path('article/', views.article),
>>>>>>> fe82a2825e45d8b14d87f41bc5345a105dc09e55
>>>>>>> c9dc42488970bd77d009e4a706fab4731398f6b8
]
