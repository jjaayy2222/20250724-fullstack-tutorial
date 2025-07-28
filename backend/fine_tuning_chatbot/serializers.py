# 20250724-fullstack-tutorial/backend/fine_tuning_chatbot/serializers.py

# 임포트
from rest_framework import serializers                              # DRF의 시리얼라이저 가져오기
from .models import FineTunedModel, TrainingData                    # models.py에서 정의된 모델 가져오기

# FineTunedModel 모델에 대한 시리얼라이저 클래스 정의
class FineTunedModelSerializer(serializers.ModelSerializer):
    """
    `class FineTunedModelSerializer(serializers.ModelSerializer)`:
    - FineTunedModel 모델에 대한 시리얼라이저 클래스
        - `serializers` = **API 데이터 송수신 시 파이썬 객체 <-> JSON 간 변환** -> 직렬화, 역직렬화을 위한 기능 
                        = 입력값의 유효성 검사 및 검증
                        = 검증된 데이터로 DB 저장 및 갱신 처리 
                    
            - 직렬화 (serialization) = 복잡한 파이썬 객체(예: 모델 인스턴스, 쿼리셋 등) -> Python의 기본 데이터 타입(딕셔너리, 리스트 등) 
                                    -> 다시 JSON이나 XML 등과 같은 다양한 콘텐츠 유형으로 쉽게 변환(렌더링)
            - 역직렬화 (Deserialization) = 외부에서 받은 JSON, XML 등 데이터 -> Python의 기본 데이터 타입
                                    -> 모델 인스턴스를 새로 생성 or 업데이트 + 유효성 검사(validation)도 함께 처리
                                    
        - `ModelSerializer` = 장고 모델을 기반으로 자동으로 시리얼라이저 필드를 생성해주는 DRF 클래스
    """
    class Meta:
        """
        class Meta:
        - 모델에 대한 메타데이터 옵션 정의
            - model = FineTunedModel
            - fields = ['id', 'model_name', 'base_model'] 필드만을 직렬화/역직렬화 과정에서 사용해야 함을 지정
                - id = 모델 고유 식별자 (자동 생성됨, 주로 PK 사용)
                - model_name = 세부 모델의 이름
                - base_model = 어떤 기본 모델에서 파인 튜닝되었는지 나타내는 필드
        """

        model = FineTunedModel
        fields = ['id', 'model_name', 'base_model']

class TrainingDataSerializer(serializers.ModelSerializer):
    """
    `class TrainingDataSerializer(serializers.ModelSerializer)`:
    - TrainingData 모델에 대한 시리얼라이저 클래스
    """
    class Meta:
        """
        class Meta:
        - 모델에 대한 메타데이터 옵션 정의
            - model = TrainingData
            - fields = ['id', 'fine_tuned_model', 'prompt', 'completion', 'is_fine_tuned', 'will_be_fine_tuned']
                - id = 모델 고유 식별자
                - fine_tuned_model = 훈련된 모델
                - prompt = 모델에 주어진 입력 문장
                - completion = 모델이 생성한 응답(출력 문장)
                - is_fine_tuned = 이 데이터가 이미 파인튜닝에 활용되었는지를 나타냄 (T/F)
                - will_be_fine_tuned = 향후 파인튜닝에 사용할 예정인지 여부 (T/F)
        
        """
        model = TrainingData
        fields = ['id', 'fine_tuned_model', 'prompt', 'completion', 'is_fine_tuned', 'will_be_fine_tuned']
