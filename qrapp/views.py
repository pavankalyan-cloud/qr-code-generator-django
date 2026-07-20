
from rest_framework import status
from django.core.files import File
from io import BytesIO
import qrcode

from .models import QRCode
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.method == "POST":
        data = request.POST.get("data")

        qr = qrcode.make(data)
        buffer = BytesIO()
        qr.save(buffer)

        qr_obj = QRCode(user=request.user, data=data)
        qr_obj.image.save(f"{request.user.username}.png", File(buffer), save=True)

        return redirect('dashboard')

    return render(request, "home.html")


@login_required
def dashboard(request):
    qrs = QRCode.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"qrs": qrs})
    
    
    
    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login




from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please login.")
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})




import qrcode
from django.shortcuts import render
from io import BytesIO
import base64

def index(request):
    img = None

    if request.method == "POST":
        data = request.POST.get('data')

        if data:
            qr = qrcode.make(data)

            buffer = BytesIO()
            qr.save(buffer, format="PNG")

            img_str = base64.b64encode(buffer.getvalue()).decode()
            img = f"data:image/png;base64,{img_str}"

    return render(request, 'index.html', {'img': img})



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import qrcode
from io import BytesIO
import base64


@api_view(["POST"])
def generate_qr_api(request):
    text = request.data.get("text")

    if not text:
        return Response(
            {"error": "Please enter text"},
            status=status.HTTP_400_BAD_REQUEST
        )

    qr = qrcode.make(text)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    img = base64.b64encode(buffer.getvalue()).decode()

    return Response({
        "image": f"data:image/png;base64,{img}"
    })