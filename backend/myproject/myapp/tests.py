# backend/myproject/myapp/tests.py

# Django의 기본 테스트 기능을 위한 임포트
from django.test import TestCase                    # Django의 테스트 케이스 기본 클래스

# Django REST Framework (DRF)의 테스트 유틸리티 임포트
from rest_framework import status                   # HTTP 상태 코드 (예: 200 OK, 404 Not Found 등)
from rest_framework.test import APIClient           # API 엔드포인트에 요청을 보내는 클라이언트 시뮬레이션 도구 (테스트 환경에서 API 호출)

# 현재 앱 (myapp) 내에서 정의된 모델과 시리얼라이저 임포트
from .models import Book                            # 테스트 대상이 되는 Book 모델
from .serializers import BookSerializer             # 테스트 대상이 되는 Book 모델의 시리얼라이저 (데이터 직렬화/역직렬화 담당)

class BookTests(TestCase):
    """
    BookAPITests 클래스 정의:
    - 이 클래스는 Django의 TestCase를 상속받아 Book 모델에 대한 API 테스트를 수행
    - APIClient를 사용하여 HTTP 요청을 시뮬레이션하고, 응답을 검증하는 메서드를 포함
    """
    
    def setUp(self):
        """
        setUp 메서드:
        - 테스트 실행 전 호출 -> 초기 설정 수행
        - Book 모델에 대한 테스트 환경 설정
        """
        self.client = APIClient()                   # API 요청을 시뮬레이션할 클라이언트 객체 생성
        self.book_data = {                          # 테스트에 사용할 책 데이터 정의
            'title': 'Test Book',
            'author': 'John Doe',
            'publication_date': '2023-01-01',
            'price': '9.99',                        # DecimalField에 맞게 문자열로 값 설정
        }
        
        self.book = Book.objects.create(**self.book_data)   # 테스트 데이터베이스에 Book 객체를 미리 하나 생성
        
    def test_get_all_books(self):
        """
        test_get_all_books 메서드:
        - 모든 책 목록을 가져오는 API 엔드포인트를 테스트
        - GET 요청을 보내고, 응답 상태 코드와 데이터가 예상대로 반환되는지 확인
        - 성공 시: HTTP 200 상태 코드와 직렬화된 책 목록
        - 실패 시: HTTP 404 (Not Found) 상태 코드
        """
        
        response = self.client.get('/myapp/books/')         # '/myapp/books/' 엔드포인트로 GET 요청 보내기
        books = Book.objects.all()                          # 데이터베이스에서 모든 Book 객체 가져오기
        serializer = BookSerializer(books, many=True)       # 가져온 객체들을 시리얼라이저로 직렬화 (API 응답과 비교 목적)
        
        # 응답 상태 확인
        self.assertEqual(response.status_code, status.HTTP_200_OK)      # 응답 상태 코드 = 200 = OK
        self.assertEqual(response.data['results'], serializer.data)  
                        # 응답 데이터의 'results' 키 값이 직렬화된 데이터와 일치하는지 확인
                        # 페이지네이션이 적용되어 'results' 키 안에 실제 데이터가 있기 때문

    def test_get_single_book(self):
        """
        test_get_single_book 메서드:
        - 특정 단일 책을 가져오는 API 엔드포인트 테스트
        - GET 요청을 보내고, 응답 상태 코드와 데이터가 예상대로 반환되는지 확인
        - 성공 시: HTTP 200 상태 코드와 직렬화된 책 정보
        - 실패 시: HTTP 404 (Not Found) 상태 코드
        """
        
        response = self.client.get(f'/myapp/books/{self.book.id}/')
                                # 생성된 책의 ID를 사용 -> 해당 책의 상세 정보 엔드포인트 -> GET 요청 보내기
        book = Book.objects.get(id=self.book.id)            # 데이터베이스에서 해당 ID의 Book 객체 가져오기
        serializer = BookSerializer(book)                   # 가져온 객체를 시리얼라이저로 직렬화 (API 응답과 비교 목적)
        
        # 응답 상태 확인 코드
        self.assertEqual(response.status_code, status.HTTP_200_OK)      # 응답 상태 코드 = 200 = OK
        self.assertEqual(response.data, serializer.data)                # 응답 데이터가 직렬화된 데이터와 일치하는지 확인

    def test_create_book(self):
        """
        test_create_book 메서드:
        - 새로운 책을 생성하는 API 엔드포인트 테스트
        - POST 요청을 보내고, 응답 상태 코드와 데이터가 예상대로 반환되는지 확인
        - 성공 시: HTTP 201 상태 코드와 직렬화된 새 책 정보
        - 실패 시: 시리얼라이저 에러와 HTTP 400 (Bad Request) 상태 코드
        """
        response = self.client.post('/myapp/create/', data=self.book_data, format='json')
                                    # '/myapp/create/' 엔드포인트로 POST 요청 보내기 -> 새로운 책을 생성
                                    # 데이터 -> JSON 형식으로 전송
                                    
        # 응답 상태 코드 확인
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)     # 응답 상태 코드 = 201 = Created
                        
        self.assertEqual(Book.objects.count(), 2)
                        # 데이터베이스에 총 2개의 책 (setUp에서 1개 + 여기서 1개)이 있는지 확인

    def test_update_book(self):
        """
        test_update_book 메서드:
        - 기존 책 정보를 업데이트하는 API 엔드포인트를 테스트
        - PUT 요청을 보내고, 응답 상태 코드와 데이터가 예상대로 반환되는지 확인
        - 성공 시: HTTP 200 상태 코드와 직렬화된 업데이트된 책 정보
        - 실패 시: 시리얼라이저 에러와 HTTP 400 (Bad Request) 상태 코드
        """
        
        # 업데이트할 데이터 정의
        updated_data = { 
            'title': 'Updated Book',
            'author': 'Jane Smith',
            'publication_date': '2023-02-01',
            'price': '19.99',                                           # DecimalField에 맞게 문자열로 값 설정
        }
        
        # 특정 책의 상세 정보 -> 엔드포인트 -> PUT 요청 -> 책 정보 업데이트
        response = self.client.put(f'/myapp/books/{self.book.id}/', data=updated_data, format='json')
                                # PUT 요청을 보내어 책 정보 업데이트
                                # f-string -> URL에 책 ID를 포함시킴
                                # data 매개변수에 업데이트할 데이터 = JSON 형식 <- format='json'    
        
        # 응답 상태 코드 확인
        self.assertEqual(response.status_code, status.HTTP_200_OK)          # 응답 상태 코드 = 200 = OK
        updated_book = Book.objects.get(id=self.book.id)                    # 업데이트된 책 객체를 데이터베이스에서 다시 가져오기
        
        # 업데이트된 필드 값들이 예상대로 변경되었는지 확인하기
        self.assertEqual(updated_book.title, updated_data['title'])         # 제목이 업데이트된 값과 일치하는지 확인
        self.assertEqual(updated_book.author, updated_data['author'])       # 저자가 업데이트된 값과 일치하는지 확인
        self.assertEqual(updated_book.publication_date.strftime('%Y-%m-%d'), updated_data['publication_date']) 
                        # 날짜 필드는 datetime 객체로 반환 -> 문자열 형식으로 비교
                        # 'publication_date'는 문자열로 전달되므로, strftime을 사용하여 형식 맞춤
        self.assertEqual(str(updated_book.price), updated_data['price'])
                        # DecimalField는 Decimal 객체로 반환 -> 문자열로 변환 -> 비교
                        # 가격이 업데이트된 값과 일치하는지 확인    
                        # 데이터베이스에 업데이트된 책 객체가 존재하는지 확인

    def test_delete_book(self):
        """
        def test_delete_book(self):
        - 특정 책을 삭제하는 API 엔드포인트를 테스트
        - DELETE 요청을 보내고, 응답 상태 코드가 204 (No Content)인지 확인
        - 성공 시: HTTP 204 상태 코드
        - 실패 시: HTTP 404 (Not Found) 상태 코드
        """
        
        response = self.client.delete(f'/myapp/books/{self.book.id}/')
                                # 특정 책의 상세 정보 엔드포인트 -> DELETE 요청 -> 책 삭제
        
        # 응답 상태 확인
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # 응답 상태 코드 = 204 = No Content
                                                                            # 성공적으로 삭제되어 반환할 내용 없는지 확인
        self.assertEqual(Book.objects.count(), 0)                           # 데이터베이스에 책이 남아있지 않은지 (0인지) 확인
        
        