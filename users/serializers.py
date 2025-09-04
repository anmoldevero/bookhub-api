from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = { 'password':{'write_only':True}, 'email':{'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user
        


class ChangePassword(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField(write_only=True)

