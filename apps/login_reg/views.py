from django.shortcuts import render, redirect, HttpResponse

def index(request):
    print("\n\n**** Login Index!")
    if not 'user_id' in request.session:
        request.session['user_id'] = 0
        request.session['logged_in'] = False

    if request.session['logged_in']:
        return redirect('/')

    return render(request, "login_reg/index.html")

def validate_login(request):
    if request.method == 'POST':
        print("\n\n**** Validating Login!")
        request.session['user_id'] = 1
        request.session['logged_in'] = True
        return redirect('/')

    return redirect('/login')

def logout(request):
    print('\n\n**** Log Out!')
    request.session["user_id"] = 0
    request.session["logged_in"] = False
    return redirect('/')
