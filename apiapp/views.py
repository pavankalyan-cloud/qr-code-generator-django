from io import BytesIO
import uuid
import os
from django.http import FileResponse, Http404
from .pagination import QRPagination

import qrcode
from django.core.files import File

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from qrapp.models import QRCode
from .serializers import QRCodeSerializer, RegisterSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def generate_qr(request):
    data = request.data.get("data")

    # Validate input
    if not data or not data.strip():
        return Response(
            {"error": "Data is required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # Generate QR Code
        qr = qrcode.make(data)

        # Save QR image to memory
        buffer = BytesIO()
        qr.save(buffer)
        buffer.seek(0)

        # Create database object
        qr_obj = QRCode(
            user=request.user,
            data=data
        )

        # Generate unique filename
        filename = f"{request.user.username}_{uuid.uuid4().hex}.png"

        # Save image
        qr_obj.image.save(
            filename,
            File(buffer),
            save=True
        )

        serializer = QRCodeSerializer(qr_obj)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )




@api_view(["GET"])
@permission_classes([IsAuthenticated])
def qr_history(request):

    search = request.GET.get("search")

    qr_codes = QRCode.objects.filter(
        user=request.user
    )

    if search:
        qr_codes = qr_codes.filter(
            data__icontains=search
        )

    qr_codes = qr_codes.order_by("-created_at")

    paginator = QRPagination()

    result_page = paginator.paginate_queryset(
        qr_codes,
        request
    )

    serializer = QRCodeSerializer(
        result_page,
        many=True
    )

    return paginator.get_paginated_response(
        serializer.data
    )


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
            {"error": "QR Code not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    # Delete image from storage
    if qr.image:
        qr.image.delete(save=False)

    qr.delete()

    return Response(
        {"message": "QR Code deleted successfully."},
        status=status.HTTP_200_OK
    )

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def download_qr(request, pk):
    try:
        qr = QRCode.objects.get(
            id=pk,
            user=request.user
        )

        if not qr.image:
            return Response(
                {"error": "QR image not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        return FileResponse(
            open(qr.image.path, "rb"),
            as_attachment=True,
            filename=os.path.basename(qr.image.name)
        )

    except QRCode.DoesNotExist:
        return Response(
            {"error": "QR Code not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    except FileNotFoundError:
        raise Http404("Image file not found.")

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_qr(request, pk):
    try:
        qr = QRCode.objects.get(
            id=pk,
            user=request.user
        )

    except QRCode.DoesNotExist:
        return Response(
            {"error": "QR Code not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    data = request.data.get("data")

    if not data or not data.strip():
        return Response(
            {"error": "Data is required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Generate new QR
    qr_image = qrcode.make(data)

    buffer = BytesIO()
    qr_image.save(buffer)
    buffer.seek(0)

    # Delete old image
    if qr.image:
        qr.image.delete(save=False)

    filename = f"{request.user.username}_{uuid.uuid4().hex}.png"

    qr.data = data
    qr.image.save(
        filename,
        File(buffer),
        save=True
    )

    serializer = QRCodeSerializer(qr)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )

@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            {
                "message": "User registered successfully."
            },
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )