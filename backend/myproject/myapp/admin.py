# myapp/admin.py

from django.contrib import admin
from .models import Book # Book 모델 임포트

# @admin.register(Book) 데코레이터를 사용하여 Book 모델을 관리자 페이지에 등록합
# 이 데코레이터를 사용하면 admin.site.register(Book, BookAdmin)을 따로 호출할 필요가 없음
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # 1. 도서의 변경 목록 페이지에 표시되는 필드를 제어
    list_display = ['title', 'author', 'publication_date', 'price']       # 'status'도 함께 추가하여 확인하면 좋음

    # 2. 도서 제목, 작가로 검색할 수 있는 검색 창을 추가
    search_fields = ['title', 'author']

    # 3. 관리자 페이지에서 필터링할 수 있는 목록 필터를 추가 (작가, 출판 날짜 등)
    list_filter = ['author', 'publication_date']

    # 4. 관리자 페이지에서 사용할 사용자 정의 액션을 정의
    actions = ['mark_as_published']

    def mark_as_published(self, request, queryset):
        """
        선택한 도서를 '출판됨' 상태로 변경하는 액션.
        """
        queryset.update(status='p') # 'p'는 'published'를 의미한다고 가정
        self.message_user(request, f"{queryset.count()}개의 도서가 출판됨으로 변경되었습니다.", level=admin.messages.SUCCESS)
        # message_user 함수에 level 인자를 추가하여 성공 메시지 스타일 적용 (선택 사항)

    # 액션의 표시 이름을 지정
    mark_as_published.short_description = "선택된 도서를 게시된 것으로 표시"

# 참고: @admin.register(Book)을 사용했으므로 아래 줄은 필요 없음
# admin.site.register(Book, BookAdmin)