from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.contrib.auth import authenticate
from django.core import exceptions
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser

class AuthCustomTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            if EmailValidator(email):
                user_request = CustomUser.objects.get(
                    email=email,
                )
            else:
                msg = _('User is unknown.')
                raise exceptions.ValidationError(msg)

            user = authenticate(email=email, password=password)
            print(user)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise exceptions.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Must include "email" and "password"')
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    token = serializers.SerializerMethodField()

    def get_token(self, instance):
        tok, created = Token.objects.get_or_create(user=instance)
        return tok.key


    class Meta:
        model = CustomUser
        fields = ('email','password', 'password2', 'token')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        
        return user