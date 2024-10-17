from django.shortcuts import render, get_object_or_404, redirect
from .models import FeeType, Concession, ClassFee, Fee
from student.models import GRRegister, Classes, ClassRegister
from django.http import JsonResponse
from .forms import FeeTypeForm, ConcessionForm, ClassFeeForm, FeeSubmitForm

# Fee Type
def feeType(request):
    fee_type = FeeType.objects.all()
    return render(request, 'fee_type/fee_type.html', locals())

def feeTypeAdd(request):
    form = FeeTypeForm()
    if request.method == 'POST':
        form = FeeTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fee_type')
    return render(request, 'fee_type/fee_type_add.html', locals())

def feeTypeEdit(request, id):
    fee_type_edit = FeeType.objects.get(fee_code = id)
    form = FeeTypeForm(instance = fee_type_edit)
    if request.method == 'POST':
        form = FeeTypeForm(request.POST, instance = fee_type_edit)
        if form.is_valid():
            form.save()
            return redirect('fee_type')
    return render(request, 'fee_type/fee_type_edit.html', locals())

# Concession
def concession(request):
    concession = Concession.objects.all()
    return render(request, 'concession/concession.html', locals())

def concessionAdd(request):
    form = ConcessionForm()
    if request.method == 'POST':
        form = ConcessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('concession')
    return render(request, 'concession/concession_add.html', locals())

def concessionEdit(request, id):
    concession_edit = Concession.objects.get(concession_code = id)
    form = ConcessionForm(instance = concession_edit)
    if request.method == 'POST':
        form = ConcessionForm(request.POST, instance = concession_edit)
        if form.is_valid():
            form.save()
            return redirect('concession')
    return render(request, 'concession/concession_edit.html', locals())

# Class Fee
def classFee(request):
    class_fee = ClassFee.objects.all()
    return render(request, 'class_fee/class_fee.html', locals())

def classFeeAdd(request):
    form = ClassFeeForm()
    if request.method == 'POST':
        form = ClassFeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_fee')
    return render(request, 'class_fee/class_fee_add.html', locals())

def classFeeEdit(request, class_name):
    # Get the class_code using the class_name
    class_instance = get_object_or_404(Classes, class_name=class_name)
    class_fee_edit = get_object_or_404(ClassFee, class_code=class_instance)

    form = ClassFeeForm(instance=class_fee_edit)
    
    if request.method == 'POST':
        form = ClassFeeForm(request.POST, instance=class_fee_edit)
        if form.is_valid():
            form.save()
            return redirect('class_fee')

    return render(request, 'class_fee/class_fee_edit.html', locals())

# Fee
def fee(request):
    gr_number = GRRegister.objects.all()
    data = []

    for gr in gr_number:
        if gr.present:
            section = ClassRegister.objects.filter(gr_number=gr.gr_number) 
            if section.exists():
                for sec in section: 
                    class_fee = ClassFee.objects.filter(class_code=sec.class_code)
                    if class_fee.exists():
                        for fee_obj in class_fee:
                            fee_amount = fee_obj.fee_amount
                            concession_per = gr.concession_code.concession_persent if gr.concession_code else 0
                            discount = (concession_per / 100) * fee_amount
                            total_due_amount = fee_amount - discount

                            fee_record = Fee.objects.filter(gr_number=gr.gr_number).first()

                            if fee_record:
                                submit_amount = fee_record.submit_amount
                                if submit_amount == total_due_amount:
                                    total_due_amount = 0
                                    fee_status = fee_record.fee_status = True
                                else:
                                    total_due_amount = total_due_amount - submit_amount
                                    fee_status = fee_record.fee_status = False
                            else:
                                submit_amount = '0'
                            data.append({
                                'gr_number': gr.gr_number,
                                'class_code': gr.class_of_admission.class_name,
                                'section': sec.section_code.section_name,
                                'due_amount': total_due_amount,
                                'submit_amount': submit_amount,
                                'fee_status': fee_status,
                            })
                    else:
                        data.append({
                            'gr_number': gr.gr_number,
                            'class_code': gr.class_of_admission.class_name,
                            'section': sec.section_code.section_name,
                            'due_amount': 'No Fee Available',
                            'submit_amount': 'No Fee Submitted',
                            'month': 'N/A',
                            'fee_status': False,
                        })

    return render(request, 'fee/fee.html', {'data': data})


# views.py
def feeSubmit(request):
    form = FeeSubmitForm()

    if request.method == 'POST':
        form = FeeSubmitForm(request.POST)
        if form.is_valid():
            form.save()  
            
            return redirect('fee')

    return render(request, 'fee/fee_submit.html', locals())



def getDueAmount(request, gr_number):
    gr_register = GRRegister.objects.filter(gr_number=gr_number).first()
    if not gr_register:
        return JsonResponse({'error': 'GRRegister not found'}, status=404)

    concession = gr_register.concession_code
    class_fee = ClassFee.objects.filter(class_code=gr_register.class_of_admission).first()
    if not class_fee:
        return JsonResponse({'error': 'ClassFee not found'}, status=404)
    
    if gr_register.concession_code != None:
        fee_amount = class_fee.fee_amount
        concession_percent = concession.concession_persent
        discount = (concession_percent / 100) * fee_amount
        total_due_amount = fee_amount - discount
    else:
        total_due_amount = class_fee.fee_amount

    return JsonResponse({
        'due_amount': total_due_amount,
    })

def getSection(request, gr_number):
    class_register = ClassRegister.objects.filter(gr_number=gr_number).first()
    if not class_register:
        return JsonResponse({'error': 'GRRegister not found'}, status=404)

    section = class_register.section_code.section_name

    return JsonResponse({
        'section_code': section,
    })

# views.py
def getClassCode(request, gr_number):
    gr_register = GRRegister.objects.filter(gr_number=gr_number).first()
    if not gr_register:
        return JsonResponse({'error': 'GRRegister not found'}, status=404)

    class_code = gr_register.class_of_admission.class_name
    print(class_code)

    return JsonResponse({
        'class_code': class_code,
    })