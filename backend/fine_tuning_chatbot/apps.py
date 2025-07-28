# 임포트
from django.apps import AppConfig                                       # 앱의 설정 정보 정의 위한 AppConfig 가져오기


# FineTuningChatbot 앱의 설정 클래스 선언
class FineTuningChatbotConfig(AppConfig):
    """
    class FineTuningChatbotConfig(AppConfig):
    - 앱의 설정 정보를 정의하는 클래스
    
    Args:
        - default_auto_field (str, optional)
            - 새로 생성되는 모델의 기본 PK(Primary Key) 타입 지정 
            - Defaults to `django.db.models.BigAutoField` = = 기본 자동 증가 필드 타입 지정
            - `BigAutoField` = (auto_created=True, primary_key=True) -> 아주 많은 데이터 (큰 숫자 PK 지원) 필요한 경우 사용 
        name (str, optional): 앱 이름 정의
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fine_tuning_chatbot'

    # 장고가 앱을 시작할 때 시작되는 메서드 
    def ready(self):
        """
        def ready(self):
        - 앱 로딩 시점에 호출 되는 메서드
        - `signals.py` 파일 import -> 시그널(이벤트 핸들러) 연결 코드가 실행
        - # `noqa`: linter(코드 검사기)로부터 이 줄의 경고를 무시하게 하는 주석
            - # `noqa` = `No Quality Assurance`의 준말
            - 파이썬 코드 검사 도구가 이 줄에 대해 코드 스타일, 미사용 import 등 오류나 경고를 무시하라고 알려주는 주석
            - 의도적으로 signal 파일을 import 하는 것이니 코드 검사 경고를 무시하라는 의미        
        """
        import fine_tuning_chatbot.signals  # noqa
