from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, write_only=True)
    name = serializers.CharField(min_length=4, write_only=True)
    last_name = serializers.CharField(min_length=5, write_only=True)
    age = serializers.IntegerField(min_value=0, write_only=True)
    country = serializers.CharField(min_length=2, write_only=True)
    phone_number = serializers.CharField(min_length=5, write_only=True)



    class Meta:
        model = User
        fields = '__all__'

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with given email already exist')
        return email

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirmation = validated_data.get('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError('Passwords don\'t match')
        return validated_data

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        user = User.objects.create_user(email, password, first_name, last_name)
        return user
