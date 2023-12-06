from django.shortcuts import render, redirect
from menu.models import Menu
from menu.forms import MenuForm

def create(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('menu:listeM')
            except :
                pass
    else:
        form = MenuForm()

    return render(request, 'menu/create.html', {'form': form})


def show(request):
    menu = Menu.objects.all()
    return render(request, "menu/listeM.html", {'menu': menu})

def edit(request, id):
    menu = Menu.objects.get(id=id)
    form = MenuForm(instance=menu)
    return render(request, 'menu/edit.html', {'menu': menu, 'form': form})

def update(request, id):
    menu = Menu.objects.get(id=id)
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            return redirect("menu:listeM")
    return render(request, 'menu/edit.html', {'menu': menu, 'form': form})

def delete(request, id):
    menu = Menu.objects.get(id=id)
    menu.delete()
    return redirect("menu:listeM")
