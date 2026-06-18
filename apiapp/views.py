from django.shortcuts import render

# Create your views here.
from io import BytesIO

import qrcode

from django.core.files import File

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from qrapp.models import QRCode
from .serializers import QRCodeSerializer




@api_view(["POST"])
@permission_classes([IsAuthenticated])
def generate_qr(request):

    data = request.data.get("data")

    if not data:
        return Response(
            {"error": "Data is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    qr = qrcode.make(data)

    buffer = BytesIO()
    qr.save(buffer)

    qr_obj = QRCode(
        user=request.user,
        data=data
    )

    qr_obj.image.save(
        f"{request.user.username}.png",
        File(buffer),
        save=True
    )

    serializer = QRCodeSerializer(qr_obj)

    return Response(serializer.data)




@api_view(["GET"])
@permission_classes([IsAuthenticated])
def qr_history(request):

    qr_codes = QRCode.objects.filter(
        user=request.user
    )

    serializer = QRCodeSerializer(
        qr_codes,
        many=True
    )

    return Response(serializer.data)




@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_qr(request, pk):

    try:
        qr = QRCode.objects.get(
            id=pk,
            user=request.user
        )
    except QRCode.DoesNotExist:
        return Response(
            {"error": "Not Found"},
            status=404
        )

    qr.delete()

    return Response(
        {"message": "Deleted Successfully"}
    )    




    