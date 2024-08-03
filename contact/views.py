# contact/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InquiryForm

def contact_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'お問い合わせを送信しました')
            return redirect('contact')
    else:
        form = InquiryForm()
    return render(request, 'contact/contact.html', {'form': form})
