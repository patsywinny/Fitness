
from django.contrib import admin
from django.urls import path
from fitnessapp import views

urlpatterns = [
    path('admin/ ', admin.site.urls),
    path('home/', views.home, name='home'),
    path('', views.sign_up, name='sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('training/', views.training, name='training'),
    path('review_us/', views.review_us, name='review_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('show/', views.show, name='show'),
    path('display/', views.display, name='display'),
    path('delete_1/<int:id>', views.delete_1, name='delete_1'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit2/<int:id>', views.edit2, name='edit2'),
    path('update/<int:id>', views.update, name='update'),
    path('update_1/<int:id>', views.update_1, name='update_1'),

]
