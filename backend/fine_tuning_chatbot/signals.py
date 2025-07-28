# 임포트
from django.dispatch import receiver                        # 장고의 시그널 리시버 기능 가져오기
from django.db.models.signals import post_save              # 모델 저장 이후(post_save) 이벤트 감지 위한 시그널
from django.contrib.auth.models import User                 # 장고의 기본 모델 유저
from rest_framework.authtoken.models import Token           # DRF의 토큰 모델   

# User모델에 대한 post_save 시그널 리시버 = 자동 호출
@receiver(post_save, sender=User)                           # `User` 모델에서 인스턴스가 저장된 뒤(`post_save`) 자동으로 호출될 함수를 지정
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    def create_auth_token(sender, instance=None, created=False, **kwargs):
    - 사용자 (User) 인스턴스가 새로 생성된 경우에만 실행

    Args:
        sender: 신호(signal)를 발생시킨 모델 클래스 그 자체 -> 어디에서 신호가 왔는지 알려주는 역할
        instance: 신호가 발생한 실제 모델 인스턴스 = 데이터 객체(User 객체의 속성들
        created (bool, optional): 객체가 새로 생성되었을 때만 실행되도록 조건 설정, Defaults to False.
        
    Returns:
    if created:
        Token.objects.create(user=instance)
        = 새로 생성된 유저에 대해 자동으로 토큰을 DB에 발급 (1:1 대응)
    """
    if created:
        Token.objects.create(user=instance)
