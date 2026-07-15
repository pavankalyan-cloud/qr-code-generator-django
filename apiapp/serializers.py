from rest_framework import serializers
from qrapp.models import QRCode
from django.contrib.auth.models import User
from rest_framework import serializers

class QRCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = QRCode
        fields = "__all__"
        read_only_fields = ("user", "image")





class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user