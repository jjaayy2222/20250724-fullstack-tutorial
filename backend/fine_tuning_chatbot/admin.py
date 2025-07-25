from django.contrib import admin
from .models import FineTunedModel, TrainingData

# 아래의 데코레이터들을 admin.ModelAdmin을 상속받은 클래스임
@admin.register(FineTunedModel)
class FineTunedModelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'base_model')
    search_fields = ('model_name', 'base_model')

@admin.register(TrainingData)
class TrainingDataAdmin(admin.ModelAdmin):
    list_display = ('prompt', 'completion', 'fine_tuned_model')
    search_fields = ('prompt', 'completion', 'fine_tuned_model__model_name')
    list_filter = ('fine_tuned_model',)
