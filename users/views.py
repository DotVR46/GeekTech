from django.shortcuts import render

from users.forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return render(request, "registration/register_done.html", {"user": new_user})
    else:
        user_form = UserRegisterForm()
    return render(request, "registration/register.html", {"form": user_form})
