from app_auth.views import SignupView
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_nested import routers
from app_projects.views import (ProjectViewSet, IssueViewSet,
                                CommentViewSet, ContributorsViewset)

router = routers.SimpleRouter()
router.register('projects', ProjectViewSet)

projects_router = routers.NestedSimpleRouter(router, 'projects', lookup='project')
projects_router.register('issues', IssueViewSet, basename='projects-issues')
projects_router.register('users', ContributorsViewset, basename='projects-users')

issues_router = routers.NestedSimpleRouter(projects_router, 'issues', lookup='issue')
issues_router.register('comments', CommentViewSet, basename='issues-comments')

urlpatterns = [
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),

    path('api/', include(router.urls)),
    path('api/', include(projects_router.urls)),
    path('api/', include(issues_router.urls)),

    path('admin/', admin.site.urls),
]