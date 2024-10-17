from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Classes, Section, Session, GRRegister, ClassRegister
from .forms import ClassForm, SectionForm, SessionForm, GRRegisterForm, ClassRegisterForm

# Front Pages
def home(request):
    return render(request, 'front_pages/home.html')

# Class Pages
def classes(request):
    classes = Classes.objects.all()
    return render(request, 'classes/classes.html', locals())

def classAdd(request):
    form = ClassForm()
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes')
    return render(request, 'classes/class_add.html', locals())

def classEdit(request, id):
    class_edit = Classes.objects.get(class_code = id)
    form = ClassForm(instance = class_edit)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance = class_edit)
        if form.is_valid():
            form.save()
            return redirect('classes')
    return render(request, 'classes/class_edit.html', locals())

# Section Pages
def section(request):
    sections = Section.objects.all()
    return render(request, 'section/sections.html', locals())

def sectionAdd(request):
    form = SectionForm()
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section')
    return render(request, 'section/section_add.html', locals())

def sectionEdit(request, id):
    section_edit = Section.objects.get(section_code = id)
    form = SectionForm(instance = section_edit)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance = section_edit)
        if form.is_valid():
            form.save()
            return redirect('section')
    return render(request, 'section/section_edit.html', locals()) 

# Session Pages
def session(request):
    sessions = Session.objects.all()
    return render(request, 'session/sessions.html', locals())

def sessionAdd(request):
    form = SessionForm()
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('session')
    return render(request, 'session/session_add.html', locals())

def sessionEdit(request, id):
    session_edit = Session.objects.get(session_code = id)
    form = SessionForm(instance = session_edit)
    if request.method == 'POST':
        form = SessionForm(request.POST, instance = session_edit)
        if form.is_valid():
            form.save()
            return redirect('session')
    return render(request, 'session/session_edit.html', locals()) 

# GR Register Pages
def grRegister(request):
    gr_register = GRRegister.objects.all()
    return render(request, 'gr_register/gr_register.html', locals())

def grRegisterAdd(request):
    form = GRRegisterForm()
    if request.method == 'POST':
        form = GRRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gr_register')
        else:
            print(form.errors)
    return render(request, 'gr_register/gr_register_add.html', locals())

def grRegisterEdit(request, id):
    gr_register_edit = GRRegister.objects.get(gr_number = id)
    form = GRRegisterForm(instance = gr_register_edit)
    if request.method == 'POST':
        form = GRRegisterForm(request.POST, instance = gr_register_edit)
        if form.is_valid():
            form.save()
            return redirect('gr_register')
    return render(request, 'gr_register/gr_register_edit.html', locals()) 

# Class Register Pages
def classRegister(request):
    class_register = ClassRegister.objects.all()
    return render(request, 'class_register/class_register.html', locals())

def classRegisterAdd(request):
    form = ClassRegisterForm()
    if request.method == 'POST':
        form = ClassRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_register')
    return render(request, 'class_register/class_register_Add.html', locals())

def classRegisterEdit(request, id):
    class_register_edit = ClassRegister.objects.get(gr_number = id)
    form = ClassRegisterForm(instance = class_register_edit)
    if request.method == 'POST':
        form = ClassRegisterForm(request.POST, instance = class_register_edit)
        if form.is_valid():
            form.save()
            return redirect('class_register')
    return render(request, 'class_register/class_register_edit.html', locals()) 