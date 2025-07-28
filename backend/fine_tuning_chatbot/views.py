# backend/fine_tuning_chatbot/views.py

# 임표트
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import default_storage                   

from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated                              # DRF의 인증 허용

import os
import json
import google.generativeai as genai                                                 # Google AI 라이브러리 가져오기

from .models import FineTunedModel, TrainingData
from .serializers import FineTunedModelSerializer, TrainingDataSerializer           # DRF의 시리얼라이저 클래스

@api_view(['GET'])
def hello_world(request):
    return Response('Hello, World!')

class FineTunedModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)                                         # 인증된 사용자만 접근 허용
    queryset = FineTunedModel.objects.all()
    serializer_class = FineTunedModelSerializer

class TrainingDataViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)                                         # 인증된 사용자만 접근 허용
    queryset = TrainingData.objects.all()
    serializer_class = TrainingDataSerializer

# JSONL 파일 생성 함수 (변동 없음)
def create_and_save_jsonl(finetuned_model_id):
    training_data = TrainingData.objects.filter(fine_tuned_model_id=finetuned_model_id)

    file_name = f"fine_tuned_model_{finetuned_model_id}.jsonl"
    with open(file_name, 'w', encoding='utf-8') as f:                                       # 인코딩 추가
        for data in training_data:
            f.write(json.dumps({'prompt': data.prompt, 'completion': data.completion}))     # '\n' 제거
            f.write('\n')                                                                   # 각 객체 뒤에 개행 문자 추가

    return file_name, training_data

# JSONL 파일 변환 API (GET 요청, 변동 없음)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def convert_jsonl_file(request, finetuned_model_id):
    try:
        FineTunedModel.objects.get(id=finetuned_model_id)
        file_name, training_data = create_and_save_jsonl(finetuned_model_id)
        file_info = os.stat(file_name)

        response = {
            'file_name': file_name,
            'lines': len(training_data),
            'file_size': file_info.st_size,
        }
        return JsonResponse(response)

    except FineTunedModel.DoesNotExist:
        return JsonResponse({'error': 'FineTunedModel with the given id does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# --- 아래부터 OpenAI API 관련 코드를 Gemini API에 맞게 '최대한 유사하게' 변경 ---
# 주의: Gemini API는 OpenAI처럼 'File upload for fine-tuning'이나 'FineTune.create'를 직접 제공하지 않음
#       따라서 이 함수들은 실제 Gemini fine-tuning 프로세스에 직접 매핑되지 않을 수 있음
#       교재의 로직을 유지하면서 Gemini API 호출로 대체하는 방향으로 진행

# Gemini는 OpenAI와 같은 'File upload for fine-tuning' API를 제공하지 않음
# Fine-tuning은 주로 Vertex AI 등 GCP 서비스를 통해 이루어지므로, 이 함수는 의미상 '학습 데이터 준비 확인' 정도로 변경
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_jsonl_file(request, finetuned_model_id):
    try:
        finetuned_model = FineTunedModel.objects.get(id=finetuned_model_id)
        file_name, _ = create_and_save_jsonl(finetuned_model_id)

        # Gemini API는 파일 업로드를 통한 Fine-tuning을 직접 지원하지 않음
        # 이 단계는 단순히 파일이 준비되었음을 확인하고, 필요하다면 Google Cloud Storage 등에 업로드하는 로직으로 대체
        # 여기서는 교재의 흐름을 유지하기 위해 '파일이 준비되었음'을 알리는 더미 응답을 반환
        # 실제 fine-tuning 로직은 Vertex AI를 통해 별도로 구현되어야 함
        result = {
            'status': 'success',
            'message': f'Training data file {file_name} prepared. '
                    'Actual Gemini fine-tuning would happen via Google Cloud Vertex AI or similar.',
            'file_name': file_name,
            'model_id': finetuned_model_id
        }

        # FineTunedModel 모델에 'file_id' 필드가 있다면, 여기서는 파일 이름이나 경로를 저장할 수 있음
        # 또는 이 필드가 OpenAI 특정이라면 사용하지 않을 수도 있습니다.
        # finetuned_model.file_id = file_name # 교재에 맞추어 임시로 파일 이름 저장
        finetuned_model.save()

        if default_storage.exists(file_name):
            default_storage.delete(file_name)

        return JsonResponse(result, status=status.HTTP_200_OK) # 성공 응답으로 변경

    except FineTunedModel.DoesNotExist:
        return JsonResponse({'error': 'FineTunedModel with the given id does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Gemini API는 OpenAI처럼 FineTune.create를 직접 제공하지 않음
# 이 함수는 Fine-tuning 요청을 시작하는 대신, 간단한 Gemini 모델 테스트 호출로 대체
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_finetune(request, finetuned_model_id):
    try:
        finetuned_model = FineTunedModel.objects.get(id=finetuned_model_id)

        # Gemini API 설정
        genai.configure(api_key=settings.GEMINI_API_KEY)

        # 교재의 의도는 'fine_tuned_model.base_model'을 사용해 fine-tuning 모델을 지정하는 것이나,
        # Gemini API는 fine-tuned 모델을 직접 호출하는 방식이 다름
        # 여기서는 단순히 Gemini 기본 모델을 사용하여 '프롬프트'에 대한 응답을 생성하는 예시로 대체
        # 실제 fine-tuning 결과 모델을 사용하려면, 해당 모델을 배포한 엔드포인트를 호출해야 함
        model = genai.GenerativeModel('gemini-2.5-flash-lite')             
        # 또는 fine_tuned_model.base_model 값에 따라 다른 Gemini 모델 사용
        
        # 간단한 테스트 프롬프트
        test_prompt = "Hello, how are you today?"
        response = model.generate_content(test_prompt)

        # 교재의 'fine_tune_id'에 해당하는 필드가 Gemini에서는 다를 수 있습니다.
        # 여기서는 단순히 성공 응답을 반환합니다.
        # finetuned_model.fine_tune_id = "gemini_fine_tune_job_id" # 적절한 필드에 저장 필요
        finetuned_model.save()

        return JsonResponse({'status': 'success', 'response_from_gemini': response.text}, status=status.HTTP_200_OK)

    except FineTunedModel.DoesNotExist:
        return JsonResponse({'error': 'FineTunedModel with the given id does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Gemini API는 OpenAI처럼 FineTune.retrieve를 직접 제공하지 않음
# 이 함수는 단순히 Gemini 모델이 잘 구성되었는지 확인하는 것으로 대체
@api_view(['PUT']) # PUT 메서드는 일반적으로 업데이트에 사용되나, 교재의 retrieve_finetune 메서드 시그니처를 따름
@permission_classes([IsAuthenticated])
def retrieve_finetune(request, finetuned_model_id):
    try:
        finetuned_model = FineTunedModel.objects.get(id=finetuned_model_id)
        
        # Gemini API 설정
        genai.configure(api_key=settings.GEMINI_API_KEY)

        # 여기서는 실제 fine-tune 작업의 상태를 조회하는 대신,
        # 간단히 Gemini 모델 리스트를 가져와서 API 연동이 잘 되었는지 확인합
        # 실제 fine-tuning 작업 상태 조회는 Vertex AI 등 별도 시스템을 사용해야 함
        list_models_response = genai.list_models()
        model_names = [m.name for m in list_models_response]

        # finetuned_model.status = "completed" # 실제 상태에 맞게 업데이트 필요
        # finetuned_model.fine_tuned_model = "gemini-pro" # 실제 파인튜닝 모델 이름으로 업데이트 필요
        finetuned_model.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Gemini API connection checked.',
            'available_gemini_models': model_names
        }, status=status.HTTP_200_OK)

    except FineTunedModel.DoesNotExist:
        return JsonResponse({'error': 'FineTunedModel with the given id does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


