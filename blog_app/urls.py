from django.urls import path, include
from .views import main, PostsViewSet, DetailPostViewSet, CategoryViewSet, DetailCategoryViewSet, TagsViewSet, DetailTagsViewSet, UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')


# router.register(r'posts', PostsViewSet, basename='posts')
# router.register(r'posts/<int:pk>/', DetailPostViewSet, basename='detail_posts')
# router.register(r'categories', CategoryViewSet, basename='categories')
# router.register(r'categories/<int:pk>/', DetailCategoryViewSet, basename='detail_categories')
# router.register(r'tags', TagsViewSet, basename='tags')
# router.register(r'tags/<int:pk>/', DetailTagsViewSet, basename='detail_tags')





app_name = 'blog_app'

urlpatterns = [
    path('main/', main, name='main'),
    path('list_posts/', PostsViewSet.as_view(), name='ListPost'),
    path('detail_post/<int:pk>/', DetailPostViewSet.as_view(), name='DetailPost'),
    path('list_categories/', CategoryViewSet.as_view(), name='ListCategory'),
    path('detail_category/<int:pk>/', DetailCategoryViewSet.as_view(), name='DetailCategory'),
    path('list_tags/', TagsViewSet.as_view(), name='ListTags'),
    path('detail_tags/<int:pk>/', DetailTagsViewSet.as_view(), name='DetailTags'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),

]