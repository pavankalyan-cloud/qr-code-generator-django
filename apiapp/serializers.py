from rest_framework import serializers
from qrapp.models import QRCode

class QRCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = QRCode
        fields = "__all__"
        read_only_fields = ("user", "image")