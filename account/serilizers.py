from rest_framework import serializers
from account.models import User

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
