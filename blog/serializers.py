





from unicodedata import category


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    comments = COmmentSerializer(many=True, source="comment_set")

    def get_category(self, obj):
        return [category.name for category in obj.category.all()]

    class Meta:
        model = ArticleModel
        fields = ["category", "title", "contents", "comments"]