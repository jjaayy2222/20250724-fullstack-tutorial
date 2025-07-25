# backend/myproject/myapp/serializers.py

# 필요한 모듈 가져오기
from rest_framework import serializers
from .models import Book

# Book 모델을 위한 serializer 클래스 정의
class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer 클래스 정의:
    
    class BookSerializer(클래스의 목적과 상속 관계 설명):

    - serializers.ModelSerializer를 상속받아 Book 모델 객체를 JSON과 같은 직렬화 가능한 형식으로 변환
    - 혹은 역직렬화하여 파이썬 객체로 변환하는 데 사용됨
    """
    class Meta:
        """
        Meta 클래스 = BookSerializer에 대한 메타데이터 옵션 정의
        = 상위 클래스의 동작 방식을 제어

        Attributes(클래스 내부에 정의된 속성variables, properties를 설명할 때 사용):
            - model (class): 이 시리얼라이저와 연결될 Django 모델 ->'Book' 모델과 연결됨
            - fields (str or list): 시리얼라이저 표현에 포함될 모델의 필드 
                                -> '__all__'은 모델의 모든 필드를 포함하도록 지정
        """
        model = Book
        fields = '__all__'

