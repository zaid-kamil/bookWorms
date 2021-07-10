
from django.urls import path
from .views import  index
from app import views

urlpatterns = [
    path('',index,name='home'),
    path('dash/',views.dashboard,name='dashboard'),
    path('report/',views.report,name='report'),
    path('contact/',views.contact,name='contact'),

    path('book/add',views.book_add,name='book_add'),
    path('book/<int:pk>/edit',views.book_edit,name='book_edit'),
    path('book/<int:pk>/delete',views.book_delete,name='book_delete'),
    path('book/<int:pk>/',views.book_detail,name='book_detail'),
    path('book/',views.book_list,name='book_list'),
    path('book/search',views.book_search,name='book_search'),
    path('author/add',views.author_add,name='author_add'),
    
    path('share/<int:pk>/books',views.share_book,name='share_book'),
    path('share/<int:pk>/delete',views.share_delete,name='share_delete'),
    path('share/<int:pk>/',views.share_detail,name='share_detail'),
    path('share/',views.share_list,name='share_list'),

    path('profile/', views.profileview, name='profile_view'),
    path('profile/edit/',views.profile_edit,name='profile_edit'),

    path('request/<int:pk>/book',views.request_book,name='request_book'),
    path('request/view',views.request_list,name='request_list'),


]