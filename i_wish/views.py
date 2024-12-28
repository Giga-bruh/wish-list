from django.http import HttpResponse
from django.shortcuts import render
from i_wish import models
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from i_wish import forms

from django.contrib.auth.decorators import login_required

@login_required
def add_zelanie(request):
    if request.method == "POST":
        form = forms.Formi_add_zelanie(request.POST,request.FILES)

        if form.is_valid():
            zelanie = form.save(commit=False)
            zelanie.polzovatel = request.user
            zelanie.save()

            return redirect('wish_list',pol_id=request.user.id)

    else:
        form = forms.Formi_add_zelanie()

    context = {'form': form}
    return render(request, 'add_zelanie.html', context)






@login_required
def wish_list(zapros,pol_id):
    a=models.Polzovatel.objects.get(id=pol_id)
    n=a.zelania.all()

    print(zapros.user.id)
    if zapros.user.id==a.id:

        otvet = render(zapros, "wish_list.html", context={"wishes": n})
    else:
        otvet = render(zapros, "public_wish_list.html", context={"wishes": n,"bruh":a})
    return otvet
@login_required
def confirm_delete(zapros,zel_id):
    item = get_object_or_404(models.Zelanie, id=zel_id)
    if zapros.method == "POST":
        item.delete()
        return redirect('wish_list', pol_id=zapros.user.id)  # Переадресация на список объектов
    context = {'wish': item}
    return render(zapros, 'confirm_delete.html', context)


def registration(request):
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            user=form.save()
            login(user=user,request=request)
            return redirect("wish_list",pol_id=user.id)
    else:
        form=CustomUserCreationForm()
    return render(request,"registration/registration.html",context={"form":form})