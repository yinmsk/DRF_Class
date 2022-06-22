from unicodedata import category
from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from blog.models import Article as ArticleModel
from ai.permissions import RegisteredMoreThanThreeDaysUser

from blog.serializers import ArticleSerializer

from django.utils import timezone

# 임포트 status


class ArticleView(APIView):
    # 로그인 한 사용자의 게시글 목록 return
    permission_classes = [RegisteredMoreThanThreeDaysUser]

    def get(self, request):
        user = request.user
        today = timezone.now()
        articles = ArticleModel.objects.filter(
            exposure_start_date__lte=today,
            exposure_end_date__gte=today,
        ).order_by("-id")

        serializer = ArticleSerializer(articles, many=True).data

        return Response(serializer, status=status.HTTP_200_OK)

        # articles = ArticleModel.objects.filter(user=user)
        # titles = [article.title for article in articles]  # list 축약 문법

        # titles = []

        # for article in articles:
        #     titles.append(article.title)

        # return Response({"article_list": titles})

    def post(self, request):
        user = request.user
        title = request.data.get("title", "")
        contents = request.data.get("content", "")
        categorys = request.data.get("category", [])
        exposure_start_date = request.data.get("exposure_start_date")
        exposure_end_date = request.data.get("exposure_end_date")

        if len(title) <= 5:
            # 임포트 해주기
            return Response({"error": "타이틀은 5자 이상 작성하셔야 합니다."}, status=status.HTTP_400)

        if len(contents) <= 20:
            # 임포트 해주기
            return Response({"error": "내용은 20자 이상 작성하셔야 합니다."}, status=status.HTTP_400)

        if not categorys:
            # 임포트 해주기
            return Response({"error": "카테고리가 지정되지 않았습니다."}, status=status.HTTP_400)

        article = ArticleModel(
            user=user,
            title=title,
            contents=contents,
            exposure_start_date=exposure_start_date,
            exposure_end_date=exposure_end_date,
        )
        article.save()
        article.category.add(*categorys)
        # 임포트 해주기
        return Response({"message": "성공"}, status=status.HTTP_200_OK)
