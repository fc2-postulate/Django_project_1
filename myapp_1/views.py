from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MemberForm

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_success')
    else:
        form = MemberForm()
    
    return render(request, 'add_member.html', {'form': form})

def member_success(request):
    return HttpResponse('Member added successfully!')

