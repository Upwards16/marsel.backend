from abc import ABC

from rest_framework import serializers, exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from .models import User, Position, Status


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "status 1"
        model = Status
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    position = PositionSerializer(many=False)
    status = StatusSerializer(many=False)

    class Meta:
        model = User
        fields = (
            'id', 'firstname', 'email', 'lastname', 'date_start_work',
            'date_of_birth', 'position', 'github', 'linkedin',
            'telegram', 'phone', 'salary', 'hourly_payment_cost', 'status',
            'cv', 'bank_details'
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'firstname', 'email', 'lastname', 'date_start_work',
            'date_of_birth', 'position', 'github', 'linkedin',
            'telegram', 'phone', 'salary', 'hourly_payment_cost', 'status',
            'cv', 'bank_details', 'password'
        )

    def update(self, instance, validated_data):
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.email = validated_data.get('email', instance.email)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.date_start_work = validated_data.get('date_start_work', instance.date_start_work)
        instance.telegram = validated_data.get('telegram', instance.telegram)
        instance.position = validated_data.get('position', instance.position)
        instance.github = validated_data.get('github', instance.github)
        instance.linkedin = validated_data.get('linkedin', instance.linkedin)
        instance.telegram = validated_data.get('telegram', instance.telegram)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.hourly_payment_cost = validated_data.get('hourly_payment_cost', instance.hourly_payment_cost)
        instance.cv = validated_data.get('cv', instance.cv)
        instance.bank_details = validated_data.get('bank_details', instance.bank_details)
        instance.position = validated_data.get('position', instance.position)
        instance.status = validated_data.get('status', instance.status)

        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))
        instance.save()

        return instance


class UserListSerializer(serializers.ModelSerializer):
    position = PositionSerializer(many=False)
    status = StatusSerializer(many=False)

    class Meta:
        model = User
        fields = (
            'id', 'firstname', 'email', 'lastname', 'date_start_work',
            'date_of_birth', 'position', 'github', 'linkedin',
            'telegram', 'phone', 'salary', 'hourly_payment_cost', 'status',
            'cv', 'bank_details'
        )


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'firstname', 'email', 'lastname', 'date_start_work',
            'date_of_birth', 'position', 'github', 'linkedin',
            'telegram', 'phone', 'salary', 'hourly_payment_cost', 'status',
            'cv', 'bank_details', 'password'
        )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        email = attrs.get('email', '')
        user = User.objects.get(email=email)
        data.update(
            {
                "user": {
                    "id": user.pk,
                    "firstname": user.firstname,
                    "lastname": user.lastname,
                    "position": {
                        "id": user.position.pk,
                        "name": user.position.name,
                        "slug": user.position.slug,
                    }
                }
            }
        )

        return data

