from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password               # Django의 기본 패스워드 검증 도구

from rest_framework import serializers
from rest_framework.authtoken.models import Token                                   # Token 모델
from rest_framework.validators import UniqueValidator                               # 이메일 중복 방지를 위한 검증 도구

class RegisterSerializer(serializers.ModelSerializer):                              # 회원가입 시리얼라이저
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],                  # 이메일 중복 검증
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],                                             # 비밀번호 검증
    )
    password2 = serializers.CharField(write_only=True, required=True)               # 비밀번호 확인을 위한 필드
    
    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')
        
    def validate(self, data):                                                       # 비밀번호 일치 여부 학인
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password":"password fields didn't match."}
            )
        return data
    
    def create(self, validated_data):
        """ CREATE 요청에 대해 create 메소드를 오버라이딩, 유지를 생성하고 토근을 생성하게 함. """
        user = User.objects.create_user(
            username=validate_data['username'],
            email=validate_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        
        return user