from django.contrib.auth.models import User
from django.db import models

# FineTunedModel 모델 정의 = 세부 모델
class FineTunedModel(models.Model):
    MODEL_CHOICES = [
        ('ada', 'Ada'),
        ('babbage', 'Babbage'),
        ('curie', 'Curie'),
        ('davinci', 'Davinci'),
    ]

    model_name = models.CharField(max_length=100)
    base_model = models.CharField(max_length=100, choices=MODEL_CHOICES)
    
    # 새로운 필드 추가 = OpenAI API를 사용하여 모델의 세부 조정 프로세스 관련된 정보 저장하는 필드
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fine_tuned_models', null=True)   # 관계 필드
    """
    User field  = 관계 필드
        - FineTunedModel과 User 모델 간 다대일 관계 생성 
            - FineTunedModel 인스턴스 = 단일 User 인스턴스와 관련
            - User 인스턴스 = 여러 FineTunedModel 인스턴스를 가질 수 있음
        - on_delete=models.CASCADE = 관련된 User가 삭제될 때 해당 User와 관련된 FineTunedModel 인스턴스도 함께 삭제되도록 지정
        - related_name='fine_tuned_models' = 역참조 이름 지정
        - null=True = 데이터베이스 레벨에서 User 필드가 비어 있을 수 있도록 허용 -> 반드시 User 객체를 참조하지 않아도 저장될 수 있음
    """ 
    file_id = models.CharField(max_length=200, null=True, blank=True)                                       # 텍스트 필드
    """
    file_id = 문자열 데이터를 저장하는 필드 (반드시 max_length를 지정해야 함)  
        - 파일을 업로드할 때 OepnAI API가 반환하는 파일 ID 저장하는 문자 필드
        - max_length=200 = 200자 이하의 문자열 데이터를 저장
        - null=True = 데이터베이스 레벨에서 데이터가 비어 있을 수 있도록 허용 -> 반드시 데이터를 참조하지 않아도 저장될 수 있음
        - blank=True = 폼 유효성 검사에서 빈 값 허용 -> 입력에서 필수가 아님
    """
    fine_tune_id = models.CharField(max_length=200, null=True, blank=True)
    # finet_tune_id = 세부 조정 프로세스를 시작할 때 OPenAI API가 반환하는 파일 ID을 저장하는 문자 필드
    # 이후 세부 조정 프로세스의 상태를 확인하거나 검색하기 위해 사용
    
    fine_tuned_model = models.CharField(max_length=200, null=True, blank=True)
    # fine_tuned_model = 세부 조정 프로세스가 완료된 후 OPenAI API가 반환하는 세부 조정된 모델의 식별자를 저장
    
    status = models.CharField(max_length=50, null=True, blank=True)
    # status = 세부 조정 프로세스의 상태를 저장 -> "processing", "complete", "failed" 등과 같은 값

    def __str__(self):
        return self.model_name

# TrainingData 모델 정의 = 특정 세부 모델과 연결된 훈련 데이터
class TrainingData(models.Model):
    fine_tuned_model = models.ForeignKey(FineTunedModel, on_delete=models.CASCADE, related_name='training_data')
    prompt = models.TextField()
    completion = models.TextField()
    
    # 새로 추가된 필드
    is_fine_tuned = models.BooleanField(default=False)                                                      # 불린 필드
    """
    is_fine_tuned = 불린 필드
        - 주어진 훈련 데이터가 모델의 세부 조정에 사용되었는지 여부를 나타냄
        - 기본값 = False -> 필드의 초깃값 = 거짓 -> 새 객체는 **아직 튜닝되지 않았다**의 의미로 자동 설정
    """
    will_be_fine_tuned = models.BooleanField(default=False)                                                 # 불린 필드
    # 주어진 훈련 데이터가 나중에 모델의 세부 조정에 사용될지 여부를 나타내는 필드
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='training_datas', null=True)      # 관계 필드
    # TrainingData 모델와 User 모델을 관계시키는 다대일 관계 필드

    def __str__(self):
        return f"Training Data for {self.fine_tuned_model.model_name}"          # {model_name} = 훈련 데이터와 관련된 모델 이름
    