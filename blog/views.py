from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
from blog.models import Category, History, Item

# Create your views here.

@user_passes_test(lambda u: u.is_superuser)
def welcome_page(request):
    return render(request, "blog/welcome.html")

@user_passes_test(lambda u: u.is_superuser)
def history(request):
    histories = History.objects.all()

    return render(request, "blog/history.html", {'histories': histories})

@user_passes_test(lambda u: u.is_superuser)
def process(request):
    categories = Category.objects.all()
    items = Item.objects.all()

    if (request.method == "POST"):
        id_item = request.POST['items']
        count = request.POST['count']

        item_obj = items.get(id=id_item)

        if 'add' in request.POST:
            item_obj.count += int(count)
            History.objects.create(item=items.get(id=id_item), number=count, process = "add")
            
        elif 'remove' in request.POST:
            item_obj.count -= int(count)
            History.objects.create(item=items.get(id=id_item), number=count, process = "remove")

        item_obj.save()

    context = {
        'categories': categories,
        'items': items
    }
    return render(request, 'blog/process.html', context)

@user_passes_test(lambda u: u.is_superuser)
def barren(request):
    items = Item.objects.all()

    context = {
        'items':items,
    }
    return render(request, 'blog/barren.html', context)

@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    categories = Category.objects.all()

    if request.method == "POST":
        categories.create(title=request.POST["title"])

    context = {
        'categories':categories,
    }
    return render(request, 'blog/categories.html', context)

@user_passes_test(lambda u: u.is_superuser)
def delete_category(request, id):
    Category.objects.get(id=id).delete()
    return redirect('categories')

@user_passes_test(lambda u: u.is_superuser)
def items(request):
    items = Item.objects.all()
    categories = Category.objects.all()

    if request.method == "POST":
        items.create(
            category=categories.get(id=request.POST["categories"]),
            name=request.POST["name"],
            count=request.POST["count"],
            )
        History.objects.create(item=items[items.count() - 1], number=request.POST["count"], process="add")

    context = {
        'categories': categories,
        'items':items,
    }
    return render(request, 'blog/items.html', context)

@user_passes_test(lambda u: u.is_superuser)
def delete_item(request, id):
    Item.objects.get(id=id).delete()
    return redirect('items')