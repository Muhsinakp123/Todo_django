from datetime import date
from django.db.models import Case, When, Value, IntegerField
from .models import Task
from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    tables = Task.objects.all().annotate(
        priority_order=Case(
            When(priority='H', then=Value(1)),
            When(priority='M', then=Value(2)),
            When(priority='L', then=Value(3)),
            output_field=IntegerField(),
        )
    ).order_by('priority_order')

    false = Task.objects.filter(status=False).count()
    today = date.today()
    return render(request, 'index.html', {'tables': tables, 'false': false, 'today': today})

def add (request):
    return render(request,'add.html',{"today": date.today()})
def add_task(request):
        a = request.POST["task"]
        c = request.POST['due_date']
        e = request.POST.get("priority", "M")   
        f = request.POST.get("category", "Other")
        new_task = Task(task=a, due_date=c, priority=e, category=f, )
        
        new_task.save()
        return redirect("index")
    
def delete_task(request, id):
    dele =  Task.objects.get(id=id)         # fetch member by id
    dele.delete()                          # delete from DB
    return redirect("index")

def status(request,id):
    cp = Task.objects.get(id=id)
    cp.status = True
    cp.save()
    return redirect('index')


def update(request, id):
    m = Task.objects.get(id=id)
    return render(request, "update.html", {
        "my_task": m,
        "today": date.today()
    })



    
# def update_task(request,id):
#         updated =  Task.objects.get(id=id)
#         updated.task = request.POST["task"]
#         updated.due_date = request.POST["due_date"]
#         updated.status = 'status' in request.POST
#         updated.save()
        
#         return redirect("index")
    

def update_task(request, id):
    updated = Task.objects.get(id=id)   
    if request.method == "POST":
        task = request.POST.get('task')
        due_date = request.POST.get("due_date")
        priority = request.POST.get('priority')
        category = request.POST.get('category')
        status = 'status' in request.POST  # checkbox handling
        
        updated.task = task
        updated.due_date = due_date  if due_date else None
        updated.status = status
        updated.category = category
        updated.priority = priority
        updated.save()
        return redirect("index")
    
    return redirect('update', id=id)
