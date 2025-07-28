# 임포트
from django.contrib import admin                            # 장고 관리자 기능 사용 위한 모듈 가져오기
from .models import FineTunedModel, TrainingData            # models.py에서 정의된 모델 가져오기

# FineTunedModel 모델을 관리자 사이트에 등록하는 클래스
# @admin.register(...) 데코레이터 사용 -> admin 등록을 간편하게 처리
@admin.register(FineTunedModel)
class FineTunedModelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'base_model')             # 관리자 목록에서 보여줄 필드 설정
    search_fields = ('model_name', 'base_model')            # 검색창에서 검색 가능한 필드 지정

# TrainingData 모델의 관리자 설정 클래스
@admin.register(TrainingData)
class TrainingDataAdmin(admin.ModelAdmin):
    """
    class TrainingDataAdmin(admin.ModelAdmin):
        - list_display: 관리자 목록에서 보여줄 필드 설정
            - prompt = 모델에 입력한 질문
            - completion = 모델이 출력한 응답
            - fine_tuned_model = 연결된 파인튜닝 모델
            - is_fine_tuned = 훈련에 실제 사용되었는지 여부
            - will_be_fine_tuned = 훈련에 사용할 예정인지 여부
        - search_fields: 검색창에서 검색 가능한 필드 지정
            - fine_tuned_model__model_name = 관련 FineTunedModel 인스턴스의 model_name으로 검색할 수 있도록 함
        - list_filter: 관리자 목록에서 필터링 가능한 필드 지정 = 목록의 오른쪽 사이드바에 나타남
    """

    list_display = ('prompt', 'completion', 'fine_tuned_model', 'is_fine_tuned', 'will_be_fine_tuned')   # is_fine_tuned, will_be_fine_tuned 추가
    search_fields = ('prompt', 'completion', 'fine_tuned_model__model_name')
    list_filter = ('fine_tuned_model', 'is_fine_tuned', 'will_be_fine_tuned')                            # is_fine_tuned, will_be_fine_tuned 추가
