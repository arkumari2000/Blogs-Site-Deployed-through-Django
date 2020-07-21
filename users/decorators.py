from django.shortcuts import redirect


def decorator(view_func):
    def wrapper_func(request, *arg, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request, *arg, **kwargs)

    return wrapper_func
