from rest_framework import serializers
from account.models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode 
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class UserRegestrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ["email", "password", "userName", "mobile", "password2"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
        
    # Validating Password and confirm password while regestration
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and confirm password should be same")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ["email", "password"]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "mobile"]

class UserChangePassSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only= True)
    password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only= True)
    class Meta:
        fields = ["password", "password2"]

    def validate(self, attrs):
        # bajaj finance
        # assian paints
        # mtar tech
        password=attrs.get('password')
        password2=attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Password and confirm password should same")
        user.ser_password(password)
        user.save()

        return attrs

class SendPassResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        fields = ["email"]

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exist():
            user = User.objects.get(email=email)
        else:
            raise ValidationError("This email id is not regestered with us")
