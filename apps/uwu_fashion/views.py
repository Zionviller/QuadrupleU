from django.shortcuts import render, redirect

def index(request):
    print('\n\n** Displaying uwu fashion Index')
    if not 'user_id' in request.session:
        request.session['user_id'] = 0
        request.session['logged_in'] = False

    context = {}

    return render(request, "uwu_fashion/index.html", context)

def upload(request):
    print("\n\n** Displaying Upload Form:")
    context = {}

    return render(request, "uwu_fashion/upload.html", context)

def process_upload(request):
    
    return redirect('/')

def profile(request):
    print("\n\n** Profile!")
    context = {}

    return render(request, "uwu_fashion/profile.html", context)
