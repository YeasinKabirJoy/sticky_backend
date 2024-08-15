from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        max_length=128,
        write_only=True,
        required=True,
        error_messages={
            'blank': 'Please provide password confirmation.',
        }
    )

    class Meta:
        model = User
        fields = ['email','username', 'password', 'password_confirm']
        extra_kwargs = {
            'email': {
                'error_messages': {
                    'blank': 'Please provide an email address.',
                }
            },
            'username': {
                'error_messages': {
                    'blank': 'Please provide an username.',
                }
            },
            'password': {
                'write_only': True,
                'error_messages': {'blank': 'Please provide a password.'}
            },
        }

    def validate(self, data):
        password = data.get('password')
        password_confirm = data.get('password_confirm')

        if not password_confirm:
            raise serializers.ValidationError({
                'password_confirm': 'Please provide a password confirmation.'
            })

        if password != password_confirm:
            raise serializers.ValidationError({
                'password_confirm': 'Passwords do not match.'
            })
        return data

    def create(self, validated_data):
        password_confirm = validated_data.pop('password_confirm', None)

        if password_confirm is None:
            raise serializers.ValidationError('Password confirmation is required.')

        user = User.objects.create_user(**validated_data)
        return user

