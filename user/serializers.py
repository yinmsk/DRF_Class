from user.models import User as UserModel
from rest_framework import serializers

from blog.models import Category as CategoryModel
from blog.models import Article as ArticleModel
from blog.models import Comment as CommemtModel

from blog.models import User as UserModel
from blog.models import UserProfile as UserProfileModel
from blog.models import Hobby as HobbyMoedl

from blog.serializers import ArticleSerializer


class UserSignupSeralizer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        # create 안에 있는 내용 중에서 password만 꺼내서
        p = user.password
        # set_password 라는 매소드를 통해 매소드한 다음
        user.set_password(p)
        # 저장
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age"]


class UserSerializer(serializers.ModelSerializer):
    # 상세 정보 리턴?
    userprofile = UserProfileSerializer()
    # user.article_set에서 가져온 데이터를 many=True(리스트 형태로) 가져와서 변수에 넣는다.
    articles = ArticleSerializer(many=True, source="article_set")
    comments = CommentSerializer(many=True, source="comment_set")

    class Meta:
        # userprofile, articles, comments 3가지는  UserModel에 존재하지 않지만 새롭게 추가해 주었다.
        model = UserModel
        fields = ["username", "fullname", "email",
                  "join_data", "userprofile", "articles", "comments"]
