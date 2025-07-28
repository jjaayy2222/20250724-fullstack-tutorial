# 20250725-fullstack-tutorial/backend/fine_tuning_chatbot/urls.py

# 임포트
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FineTunedModelViewSet, TrainingDataViewSet,
    convert_jsonl_file, upload_jsonl_file, create_finetune, retrieve_finetune,          # 새로운 API 연동 로직
#    deprecated,
)

router = DefaultRouter()
"""
DefaultRouter() 
    - 각각의 뷰셋에 대해 표준 액션 (목록, 생성, 조회, 업데이트, 삭제)에 대한 적절한 URL 패턴을 자동으로 생성
    - 이후 라우터의 모든 URL을 루트 경로 아래의 urlpatterns에 포함
"""

router.register(r'fine_tuned_models', FineTunedModelViewSet)
router.register(r'training_data', TrainingDataViewSet)
"""
    /fine_tuned_models/ = 경로에 FineTunedModelViewSet 클래스에 대한 CRUD URL 패턴을 자동으로 생성
        - /fine_tuned_models/ 
            - GET = 모든 세부 조정된 모델 나열
            - POST = 새로운 세부 조정된 모델 생성
        - /fine_tuned_models/<id>/
            - GET = 주어진 id의 세부 조정된 모델 검색
            - PUT, PATCH = 해당 모델 업데이트
            - DELETE = 해당 모델 삭제
        - API를 통해 FineTunedModel 및 TrainingData 데이터와 상호작용 가능 
    
    /training_data/ = 경로에 TrainingDataViewSet 클래스에 대한 CRUD URL 패턴을 자동으로 생성
"""

# 변수 이름을 gemini_patterns로 변경
gemini_patterns = [
    path('convert/<int:finetuned_model_id>/', convert_jsonl_file, name='convert_jsonl_file'),
    path('upload/<int:finetuned_model_id>/', upload_jsonl_file, name='upload_jsonl_file'),
    path('create/<int:finetuned_model_id>/', create_finetune, name='create_finetune'),
    path('retrieve/<int:finetuned_model_id>/', retrieve_finetune, name='retrieve_finetune'),
]


urlpatterns = [
    path('', include(router.urls)),
    path('gemini/', include((gemini_patterns, 'gemini'))),
]
"""
    - DRF에서 ModelViewSet은 list, create, retrieve, update, destroy 기능 자동 포함 -> URL 자동 생성
    - /api/fine_tuned_models/ URL 예시
        - List: GET `/api/fine_tuned_models/`
        - Create: POST `/api/fine_tuned_models/`
        - Retrieve: GET `/api/fine_tuned_models/{id}/`
        - Update: PUT `/api/fine_tuned_models/{id}/`                # 특정 fine tuned 모델 업데이트
        - Update: PATCH `/api/fine_tuned_models/{id}/`              # 특정 fine tuned 모델 **부분적** 업데이트
        - Destroy: DELETE `/api/fine_tuned_models/{id}/`
    
    - /api/training_data/ URL -> `/api/fine_tuned_models/`와 기능적으로 같음
"""
