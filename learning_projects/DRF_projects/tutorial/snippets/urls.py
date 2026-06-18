from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views



# snippet_list = views.SnippetViewSet.as_view({
#     'get':'list',
#     'post':'create'
# })

# snippet_detail = views.SnippetViewSet.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'patch': 'partial_update',
#     'delete':'destroy'
# })

# snippet_highlight=views.SnippetViewSet.as_view({
#     'get':'highlight'
    
# },renderer_classes=[renderers.StaticHTMLRenderer])

# user_list = views.UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = views.UserViewSet.as_view({
#     'get': 'retrieve'
# })

urlpatterns = [
    path('', views.RootView.as_view()),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail)
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('user/', views.UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', views.USerDetail.as_view(), name='user-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlighted.as_view(), name='snippet-highlight')
    # path('snippets/', snippet_list, name='snippet-list'),
    # path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    # path('user/', user_list, name='user-list'),
    # path('user/<int:pk>/', user_detail, name='user-detail'),
    # path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight')
]

urlpatterns = format_suffix_patterns(urlpatterns)


# router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet,basename="snippet")
# router.register(r'users', views.UserViewSet,basename="user")

# urlpatterns=[
#     path('', include(router.urls))
# ]
