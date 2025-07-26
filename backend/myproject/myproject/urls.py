# myproject/urls.py

"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# 정적/미디어 파일 서빙을 위한 임포트
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns                         # 개발 서버 정적 파일 서빙에 사용

# DRF 관련 임포트
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView      # DRF 문서화 도구

urlpatterns = [
    path('admin/', admin.site.urls),                                        # Admin URL
    path('myapp/', include('myapp.urls')),                                  # 'myapp' 앱의 URL 포함
    path('api/', include('rest_framework.urls')),                           # DRF의 기본 인증 URL 포함
    
    # DRF Spectacular URLS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # 대화형 UI
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),   # 읽기 전용 API
    
    # <--- 여기에 새로운 템플릿 실습 URL을 추가합니다!
    path('hello/', TemplateView.as_view(template_name='hello.html', extra_context={'name': '사용자'})),
]

# 개발 서버 (DEBUG=True)에서 정적 파일 및 미디어 파일을 제공하기 위한 설정
# 프로덕션 환경에서는 웹 서버 (Nginx, Apache 등)가 이 역할을 대신함
if settings.DEBUG:
    # 1. Django 앱의 static 폴더 및 STATICFILES_DIRS에 지정된 정적 파일 서빙
    urlpatterns += staticfiles_urlpatterns()

    # 2. MEDIA_ROOT에 저장된 사용자 업로드 미디어 파일 서빙
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)