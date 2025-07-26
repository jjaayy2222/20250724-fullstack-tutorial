# backend/myproject/myapp/views.py

# ====================================================================
# Django 기본 모듈 (General Django Core Modules)
# ====================================================================
from django.shortcuts import render, redirect       # HTML 템플릿을 렌더링하거나 다른 URL로 리다이렉트하는 함수들을 제공
from .forms import BookForm                         # Django 폼 기능을 사용하여 사용자 입력을 처리하는 BookForm 클래스 (현재 API 뷰에서는 직접 사용되지 않음)
from myapp.models import Book                       # Django ORM을 통해 데이터베이스와 상호작용할 'Book' 모델을 가져옴


# ====================================================================
# Django REST Framework (DRF) 관련 모듈 (DRF Specific Modules)
# ====================================================================
from rest_framework.decorators import api_view              # 함수 기반 뷰를 RESTful API 뷰로 변환하는 데 사용되는 데코레이터
from rest_framework.response import Response                # DRF에서 HTTP 응답을 생성하고 직렬화된 데이터를 포함하여 반환하는 클래스
from rest_framework import viewsets                         # RESTful API의 CRUD 작업을 하나의 클래스로 쉽게 구현할 수 있도록 돕는 ViewSet 클래스들을 제공
from rest_framework.pagination import PageNumberPagination  # 페이지네이션을 위한 클래스, API 응답을 페이지 단위로 나누어 반환
from rest_framework.filters import SearchFilter, OrderingFilter # 필터링과 정렬을 위한 클래스, API 요청에 대한 검색 및 정렬




# ====================================================================
# 프로젝트 내 시리얼라이저 (Project-Specific Serializers)
# ====================================================================
from .serializers import BookSerializer                     # 'Book' 모델 객체를 JSON 등 직렬화 가능한 형태로 변환하거나 그 반대로 역직렬화하는 시리얼라이저


# create_book 뷰 함수 재정의:
@api_view(['POST'])     # POST 요청만 처리하는 API 뷰 데코레이터
def create_book(request):
    """
    def create_book(request). =새로운 책 정보를 생성하는 API 뷰

    이 뷰는 HTTP POST 요청만 처리하도록 설정되어 있습니다.
    클라이언트로부터 JSON 형식의 데이터를 받아 Book 모델 객체를 생성하고,
    성공 시 생성된 객체 데이터와 201 Created 상태 코드를 반환합니다.
    데이터 유효성 검증 실패 시 에러 메시지와 400 Bad Request 상태 코드를 반환합니다.

    Args:
        request (HttpRequest): 클라이언트로부터 받은 HTTP 요청 객체입니다.
                                HTTP POST 요청 시 요청 본문(body)에 JSON 데이터가 포함됩니다.

    Returns:
        Response:
            - 성공 시: 직렬화된 책 데이터와 HTTP 201 (Created) 상태 코드.
            - 실패 시: 시리얼라이저 에러와 HTTP 400 (Bad Request) 상태 코드.
    """
    
    # 1. 시리얼라이저 인스턴스 생성 및 데이터 전달
    serializer = BookSerializer(data=request.data)
    # 클라이언트로부터 받은 요청(request)의 데이터(request.data)를 BookSerializer에 넘겨 유효성 검사 준비
    
    # 2. 데이터 유효성 검사
    # serializer.is_valid() 메서드를 호출 -> 데이터가 모델의 제약 조건과 시리얼라이저에 정의된 규칙에 맞는지 검사
    
    # 3. 유효성 검사 통과 시 데이터 저장
    if serializer.is_valid():       
        serializer.save()
        # 유효성이 검증된 데이터 -> 새로운 Book 객체를 데이터베이스에 생성(저장)
        
        # 4. 성공 응답 반환
        return Response(serializer.data, status=201)
        # serializer.data -> 직렬화된 데이터(책 정보)를 포함
        # Response 객체를 사용하여 HTTP 응답을 생성 -> HTTP 201 상태 코드와 함께 반환
    
    # 5. 유효성 검사 실패 시 에러 응답 반환
    return Response(serializer.errors, status=400)
    # serializer.errors(어떤 필드가 어떤 이유로 유효하지 않은지에 대한 정보)
    # 400 Bad Request 상태 코드를 클라이언트에 반환



def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})


# ====================================================================
# DRF ViewSets (Class-Based API Views)
# ====================================================================
class BookViewSet(viewsets.ModelViewSet):
    """
    class BookViewSet(viewsets.ModelViewSet) -> Book 모델에 대한 CRUD 작업 자동 처리 API 뷰셋

    - queryset: 이 뷰셋이 다룰 모델 객체들의 쿼리셋을 지정 -> 모든 Book 객체를 가져옴
    - serializer_class: 이 뷰셋에서 데이터 직렬화/역직렬화에 사용할 시리얼라이저를 지정
                        -> 여기서는 BookSerializer 사용
    - pagination_class: 페이지네이션을 적용할 클래스 지정 -> PageNumberPagination 사용
    - filter_backends: 필터링과 정렬을 위한 백엔드 클래스들 지정
                        -> SearchFilter와 OrderingFilter를 사용하여 검색과 정렬 기능을 활성화
    - search_fields: 검색 가능한 필드 지정 -> 'title'과 'author' 필드에서 검색 가능
    - ordering_fields: 정렬 가능한 필드 지정 -> 'publication_date'와 'price' 필드로 정렬 가능

    DRF의 ViewSet 클래스는 GET (목록, 상세), POST (생성), PUT/PATCH (업데이트), DELETE (삭제)
    요청을 별도의 함수를 정의할 필요 없이 한 클래스에서 처리할 수 있음.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['publication_date', 'price']
    
    def get_queryset(self):
        """
        요청에 따라 필터링 및 정렬된 쿼리셋을 반환
        이 메서드는 기본 쿼리셋을 가져온 후, 요청의 쿼리 매개변수에 따라 필터링 및 정렬을 적용
        """
        # 1. 부모 클래스의 기본 쿼리셋 가져오기
        queryset = super().get_queryset()
        
        # 2. 요청에서 필터링 매개변수 가져오기
        # 2.1.요청 URL의 쿼리 파라미터에서 'title' 값을 가져오되, 없으면 None 반환
        title = self.request.query_params.get('title', None)
        # 2.2.요청 URL의 쿼리 파라미터에서 'author' 값을 가져오되, 없으면 None 반환
        author = self.request.query_params.get('author', None)
        
        # 3. 필터링 적용
        # 3.1. 'title' 파라미터가 있는 경우, 대소문자를 구분하지 않고 제목에 해당 단어가 포함된 객체만 필터링
        if title:
            queryset = queryset.filter(title__icontains=title)
        # 3.2. 'author' 파라미터가 있는 경우, 대소문자를 구분하지 않고 저자 이름에 해당 단어가 포함된 객체만 필터링
        if author:
            queryset = queryset.filter(author__icontains=author)
    
        # 4. 정렬 적용
        # 4.1. 요청 URL의 쿼리 파라미터에서 'ordering' 값을 가져오되, 없으면 None 반환
        ordering = self.request.query_params.get('ordering', None)
        
        # 4.2. ordering' 값이 view에 정의된 정렬 가능 필드('ordering_fields') 목록에 포함되어 있는지 확인
        if ordering in self.ordering_fields:
            
            # # 쿼리셋을 해당 필드 기준으로 정렬
            queryset = queryset.order_by(ordering)
        
        # 5. 최종적으로 필터링 및 정렬된 쿼리셋을 반환    
        return queryset    
    
    