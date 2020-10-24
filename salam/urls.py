from django.urls import path,include
form django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mohtaj),
         path('',include(user.urls)),

]




