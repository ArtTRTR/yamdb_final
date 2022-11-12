import datetime as dt

from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title, User


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Вы не можете зарегистрироваться под именем me')
        return value


class ConfirmationSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = 'username', 'email', 'role', 'first_name', 'last_name', 'bio'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = 'name', 'slug'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = 'name', 'slug'


class TitleReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(
        read_only=True
    )
    genre = GenreSerializer(
        read_only=True,
        many=True
    )
    rating = serializers.FloatField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title

    def validate_year(self, value):
        current_year = dt.date.today().year
        if value > current_year:
            raise serializers.ValidationError('Проверьте год')
        return value


class TitleWriteSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True,
    )

    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Review
        exclude = ('title',)

    def validate(self, attrs):
        request = self.context.get('request')
        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        if (request.method == 'POST'
            and Review.objects.filter(
                title=title, author=request.user).exists()):
            raise ValidationError(
                'Отзыв от этого пользователя уже существует!')
        return attrs


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        exclude = ('review',)
