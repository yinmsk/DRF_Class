from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone
from rest_framework.exceptions import APIException
from rest_framework import status


class RegisteredMoreThanThreeDaysUser(BasePermission):
    massage = '가입 후 3일 이상 지난 사용자만 사용하실 수 있습니다아..'

    def has_permission(self, request, view):
        user = request.user
        return bool(user.is_authenticated and
                    request.user.join_date < (timezone.now() - timedelta(days=3)))


class IsAdminOrIsAuthenticateReadOnly(BasePermission):
    SAFE_METHODS = ('GET', )
    message = '접근 권한이 없습니다.'

    def gas_permission(self, request, view):
        user = request.user

        if not user.is_authentticated:
            response = {
                "detail": "서비스를 이용하기 위해 로그인 해주세요.",
            }
        raise GenericAPIException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if user.is_authentticated and request.method in self.SAFE_METHODS:
            return True

        if user.is_authentticated and user.is_admin or \
                uer.join_date < (datetime.now().date() - timedelta(days=7)):
            return True
