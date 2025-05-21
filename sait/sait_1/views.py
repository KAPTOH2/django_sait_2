from django.shortcuts import render
from django.http import HttpResponse
import datetime
from math import pi
from .forms import StudentForm
from .forms import  AbcModelForm
from .models import AbcModel
from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Min, Max, StdDev, Sum
from django.shortcuts import render, get_object_or_404
from .models import Item

def home(request):
    now = datetime.datetime.now()
    context = {
        "img" :"sait_1/images/фото.jpg",
        "name" :"Мураткин Илья Сергеевич",
        "phone" :"890006620444",
        "email" :"ismuratkin@edu.hse.ru",
        "group" :"Экономика",
        'now': now,
        "img_1" :"sait_1/images/фото_1.jpg",
        "name_1" :"Байгужин Искандер Рустамович",
        "phone_1" :"цифры)",
        "email_1" :"irbaigushin@edu.hse.ru",
        "prepod" : "Марширов В.В."

    }
    return render(request, 'home.html', context)

def index(request):
    return HttpResponse("Тут нет сайта. Иди сюда -> http://127.0.0.1:8000/home/")

def razdel_1(request):
    return render(request, 'razdel_1.html')

def zadacha(request, A, H, R, M):

    kub_volume = A**3
    cilindr_volume = R**2 * H * pi

    kub = M <= kub_volume
    cilindr = M <= cilindr_volume

    fits = "ни в одну фигуру"
    if kub and cilindr:
        fits = "в обе фигуры"
    elif kub:
        fits = "в куб"
    elif cilindr:
        fits = "в цилиндр"

    context = {
        'A': A,
        'H': H,
        'R': R,
        'M': M,
        'kub_volume': kub_volume,
        'cilindr_volume': cilindr_volume,
        'kub': kub,
        'cilindr': cilindr,
        'fits': fits,
    }
    return render(request, 'zadacha.html', context)

def student_grades(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            names = form.cleaned_data['names'].split()
            grades = form.cleaned_data['grades'].split()

            student_scores = {}
            for i, name in enumerate(names):
                grade_list = grades[i].split('-')
                total_score = sum(int(grade) for grade in grade_list)
                student_scores[name] = total_score

            if student_scores: 
                best_student = max(student_scores, key=student_scores.get)
                context = {'form': form, 'best_student': best_student}
                return render(request, 'student_grades.html', context)
    else:
        form = StudentForm()
    return render(request, 'student_grades.html', {'form': form})

def massiv(request):
    objects_array = [
        {
            "id": "1",
            "title": "Сникерс",
            "description": "Шоколадка",
            "price": 100,
            "img": "sait_1/images/snikers.jpg"
        },
        {
            "id": "2",
            "title": "Баунти",
            "description": "Шоколадка",
            "price": 200,
            "img": "sait_1/images/bounty.jpeg"
        },
        {
            "id": "3",
            "title": "Киткат",
            "description": "Шоколадка",
            "price": 300,
            "img": "https://avatars.mds.yandex.net/get-mpic/5177644/img_id5690238125692061619.jpeg/orig"
        },
        {
            "id": "4",
            "title": "Твикс",
            "description": "Шоколадка",
            "price": 400,
            "img": "https://main-cdn.sbermegamarket.ru/big1/hlr-system/582/366/004/103/014/19/100023331887b0.jpg"
        }
    ]
    dict_of_array = {'objects_array': objects_array}
    context = {'dict_of_array': dict_of_array}
    return render(request, "massiv.html", context)

def abc_model_form(request):
    print("request.method: ", request.method)
    if request.method == "POST":
        form = AbcModelForm(request.POST)
        if form.is_valid():
            print("\nform_is_valid:\n", form)
            form.save()
            return redirect("abc_result")
    else:
        form = AbcModelForm()
        print("\nform_else:\n", form)
    context = {"form": form}
    print("\ncontext:\n", context)
    return render(request, "abc_model_form.html", context)

def abc_result(request):
    object_list = AbcModel.objects.all().order_by("-id")
    print("\n\nobject_list: ", object_list)

    last_object = object_list.values("fam", "a", "b", "c")[0]
    print("\n\nlast_object: ", last_object)
    task_formulation = object_list.values("fam")[0]
    task_id = object_list.values("id")[0]["id"]
    print("task_id task_formulation: ", task_id, task_formulation)

    # list
    values_list = object_list.values_list()[0]
    print("\nvalues_list: ", values_list)
    task_formulation = values_list[1]
    print("\ntask_formulation: ", task_formulation)
    last_values = [values_list[1], values_list[2], values_list[3], values_list[4]]
    print("\nlast_values:", last_values)


    context = {
        "last_object": last_object,
        "task_formulation": task_formulation,
        "last_values": last_values,
    }
    return render(request, "abc_result.html", context)


def table(request):
    objects_values = AbcModel.objects.values()
    print("\nobjects_values:", objects_values)
    objects_values_list = (
        AbcModel.objects.values_list().filter(id__gte=0).order_by("id")
    ) 
    print("\nobjects_values_list:", objects_values_list)
    cur_objects = objects_values_list
    statics_val = [
        cur_objects.aggregate(Count("b")),
        cur_objects.aggregate(Avg("b")),
        cur_objects.aggregate(Min("b")),
        cur_objects.aggregate(Max("b")),
    ]
    print("\nstatics_val:", statics_val)
    statics = {"statics_val": statics_val}
    # fields_name
    fields = AbcModel._meta.get_fields()
    print("\nfields", fields)
    verbose_name_list = []
    name_list = []
    for e in fields:
        verbose_name_list.append(e.verbose_name)
        name_list.append(e.name)
    print("\nverbose_name_list:", verbose_name_list)
    print("\nname_list", name_list)
    field_names = verbose_name_list
    context = {
        "objects_values": objects_values,
        "name_list": name_list,
        "objects_values_list": objects_values_list,
        "verbose_name_list": verbose_name_list,
        "statics": statics,
        "field_names": field_names,
    }
    return render(request, "table.html", context)

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_detail.html', {'item': item})