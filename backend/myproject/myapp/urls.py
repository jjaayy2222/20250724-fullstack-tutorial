# backend/myproject/myapp/urls.py

# ====================================================================
# 모듈 가져오기 (Import Modules)
# ====================================================================
# Django 기본 URL 처리 모듈
from django.urls import path, include               # URL 패턴을 정의하고 다른 URLconf를 포함


# Django REST Framework (DRF) 관련 모듈 (DRF Specific Modules)
from rest_framework import routers                  
# ViewSet을 URL에 자동으로 등록하여 RESTful API 엔드포인트를 쉽게 생성할 수 있도록 돕는 라우터


# 애플리케이션의 뷰 가져오기 (Import App-Specific Views)
# BookViewSet: DRF의 ModelViewSet을 상속받아 Book 모델에 대한 CRUD API를 제공
from .views import BookViewSet                      # Book 모델에 대한 CRUD API를 처리하는 ViewSet 클래스

# 함수 기반 뷰: 특정 URL 패턴에 따라 호출될 일반적인 Django 뷰 함수들
from .views import create_book, book_list          # 책 생성 API 뷰(함수 기반)와 책 목록을 보여주는 HTML 뷰 함수


# ====================================================================
# DRF 라우터 설정 (DRF Router Configuration)
# ====================================================================

router = routers.DefaultRouter()
# DefaultRouter 인스턴스를 생성
# 이 라우터는 ViewSet에 대한 기본 CRUD URL 패턴을 자동으로 생성

router.register('books', BookViewSet)
# 'books'라는 접두사(prefix)로 BookViewSet을 등록 -> /books/, /books/{id}/ 같은 URL이 자동으로 생성


# ====================================================================
# URL 패턴 정의 (URL Patterns Definition)
# ====================================================================
urlpatterns = [
    path('', include(router.urls)),
    # DRF 라우터가 생성한 URL들을 포함
    # 예: /myapp/books/, /myapp/books/{id}/ 등이 여기에 포함

    path('create/', create_book, name='create_book'), 
    # 함수 기반 뷰에 대한 URL 패턴
    # /myapp/create/ 경로에 create_book API 뷰(POST 요청만 처리)를 연결
    # Note: 이 뷰는 DRF API 뷰이므로, BookViewSet의 POST와 중복될 수 있음
    
    path('list/', book_list, name='book_list'),
    # HTML 렌더링 뷰에 대한 URL 패턴
    # /myapp/list/ 경로에 book_list HTML 뷰를 연결
    # Note: BookViewSet의 GET (목록)과 기능이 중복될 수 있음
]