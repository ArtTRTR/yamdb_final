from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (CategoryViewSet, CommentViewSet, CreateUserViewSet,
                    GenreViewSet, GetJWTTokenViewSet, ReviewViewSet,
                    TitleViewSet, UserViewSet)

app_name = 'api'

router = SimpleRouter()
router.register('auth/signup', CreateUserViewSet, basename='signup')
router.register('auth/token', GetJWTTokenViewSet, basename='token')
router.register('users', UserViewSet, basename='users')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews'
    r'/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls))
]
