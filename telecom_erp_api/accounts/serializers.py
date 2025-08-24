from rest_framework import serializers
from .models import UserProfile, Role
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    email= serializers.EmailField(source='user.email', read_only=True)
    class Meta:
        model = UserProfile
        fields = [ 'full_name', 'phone_number', 'email', 'profile_picture']
        read_only_fields = ('user', 'created_at')
    
    def get_full_name(self, obj):
        return obj.full_name
    
class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'role', 'department', 
            'department_name', 'profile', 'date_joined', 'is_active'
        ]
        read_only_fields = ('date_joined', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True, 'required': False}
        }
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop("profile", None)

        # update the user fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # update profile if data is provided
        if profile_data:
            profile, created = UserProfile.objects.get_or_create(user=instance)
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        return instance

class UserRegisterResponseSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'role', 'department', 
            'department_name', 'profile', 'date_joined', 'is_active'
        ]
        read_only_fields = ('date_joined', 'is_active')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, min_length=8, required=True)
    first_name = serializers.CharField(write_only=True, required=True, max_length=150)
    last_name = serializers.CharField(write_only=True, required=True, max_length=150)


    class Meta:
        model = User
        fields = ["email", "password", 'password_confirm', 'first_name','last_name','department']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Password fields doesn't match."})
        return attrs
    
    def create(self, validated_data):
        # extrat params to be used in the profile data
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')

        # create user
        user = User.objects.create_user(password=password, **validated_data)

        # Create profile with names 
        user.profile.first_name=first_name
        user.profile.last_name=last_name
        user.profile.save()
        
        return user
    
    def to_representation(self, instance):
        # Use the detailed serializer for response
        return UserRegisterResponseSerializer(instance, context=self.context).data
    
class AdminRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, min_length=8, required=True)
    first_name = serializers.CharField(write_only=True, required=True, max_length=150)
    last_name = serializers.CharField(write_only=True, required=True, max_length=150)

    class Meta:
        model = User
        fields = ["email", "password", 'password_confirm', 'first_name', 'last_name', 'department']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Password fields doesn't match."})
        return attrs
    
    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')

        user = User.objects.create_superuser(password=password, **validated_data)

        user.profile.first_name=first_name
        user.profile.last_name=last_name
        user.profile.save()
        # user = User.objects.create(**validated_data)
        # user.set_password(password) #password hashes here
        # user.save()
        return user
