from django.shortcuts import render
# from itsdangerous import Serializer
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
# 로그인 기능 구현 authenticate
from django.contrib.auth import login, logout, authenticate

from user.serializers import UserSerializer, UserSignupSeralizer


class UserView(APIView):
    # permission_classes = [permissions.AllowAny]  # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    permission_classes = [permissions.IsAuthenticated]  # 로그인 된 사용자만 view 조회 가능

    # 사용자 정보 조회
    def get(self, request):
        return Response(UserSerializer(request.user).data, status.HTTP_200_OK)

    # 회원가입
    def post(self, request):
        Serializer = UserSignupSeralizer(data=request.data)
        # request.data 해서 가져온 데이터가 유효한지 빠진 값이 없는지 검증해준다.
        if serializer.is_valid():
            # 인스턴스를 저장해준다.
            serializer.save()
            return Response({"message": "가입 완료"})
        else:
            # 인스턴스를 저장해준다.
            print(serializer.errors)
            return Response({"message": "가입 실패"})

    # 회원 정보 수정
    def put(self, request):
        return Response({"message": "put method!!"})

    # 회원 탈퇴
    def delete(self, request):
        return Response({"message": "delete method!!"})


class UserAPIView(APIView):
    # 로그인
    def post(self, request):
        # json 형식으로 데이터를 주고 받을 때는 data를 사용한다.
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        # 인증을 하지 못하면 None값이 담긴다.
        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})

        login(request, user)
        return Response({"message": "login success!!"})

    def delete(self, request):
        logout(request)
        return Response({"message": "logout success!!"})
