from django.contrib import admin
from user.models import User as UserModel, UserProfile
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserProfileInline(admin.StackedInline):
    model = UserProfileModel
    # admin 페이지를 꾸밀 수 있는 기능중 하나? hobby를 꾸며주었다.
    filter_horizontal = ['hobby']


# UserAdmin 등록 방법은 장고 공식문서에 나와있다.
class UserAdmin(BaseUserAdmin):

    list_display = ('id', 'username', 'fullname', 'email')
    list_display_links = ('username', )
    list_filter = ('username', )
    list_fields = ('username', 'email', )

    fieldsets = (
        ("info", {'fields': ('username', 'password',
         'email', 'fullname', 'join_date',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active',)}),)
    # UserAdmin 아래에 UserProfileInline을 붙여준다.
    inlines = (
        UserProfileInline,
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'fullname', 'password1', 'password2')}
         ),
    )

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date', )
        else:
            return ('join_date', )


# Register your models here.
admin.site.register(UserModel)
admin.site.register(UserProfileModel)
admin.site.register(HobbyModel)
