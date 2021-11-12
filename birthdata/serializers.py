from datetime import date

from django.core.validators import MaxValueValidator

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator

from birthdata.models import Town, Writer


class WriterSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=100)
    patronymic = serializers.CharField(max_length=100)
    lastname = serializers.CharField(max_length=100)
    birth_place = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Town.objects
    )
    birth_date = serializers.DateField(
        format='%d.%m.%Y',
        input_formats=['%d.%m.%Y', 'iso-8601'],
        validators=[MaxValueValidator(date(1999, 12, 31))]
    )

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Writer.objects,
                fields=['firstname', 'patronymic', 'lastname']
            )
        ]

    def validate(self, attrs):
        set_attrs = set(
            [attrs['firstname'], attrs['patronymic'], attrs['lastname']]
        )
        if len(set_attrs) != 3:
            raise ValidationError(
                'Имя, отчество и фамилия не могут совпадать между собой',
                code='duplicate values'
            )
        return attrs

    def create(self, validated_data):
        return Writer.objects.create(**validated_data)
