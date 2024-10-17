from django import forms
from .models import FeeType, Concession, ClassFee, Fee
from student.models import Classes

class FeeTypeForm(forms.ModelForm):
    class Meta:
        model = FeeType
        fields = ['fee_code', 'fee_type', 'fee_remarks']

        widgets = {
            'fee_code':forms.NumberInput(attrs={'class':'form-control'}),
            'fee_type':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fee Type'}),
            'fee_remarks':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fee Remarks'}),
        }

class ConcessionForm(forms.ModelForm):
    class Meta:
        model = Concession
        fields = ['concession_code', 'concession_type', 'concession_amount', 'concession_persent', 'concession_remarks']

        widgets = {
            'concession_code':forms.NumberInput(attrs={'class':'form-control'}),
            'concession_type':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Concession Type'}),
            'concession_amount':forms.NumberInput(attrs={'class':'form-control'}),
            'concession_persent':forms.NumberInput(attrs={'class':'form-control'}),
            'concession_remarks':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Concession Remarks'}),
        }

class ClassFeeForm(forms.ModelForm):
    class Meta:
        model = ClassFee
        fields = ['class_code', 'fee_amount']

        widgets = {
            'class_code':forms.Select(attrs={'class':'form-control'}),
            'fee_amount':forms.NumberInput(attrs={'class':'form-control'}),
        }


class FeeSubmitForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ['gr_number', 'class_code', 'section_code', 'due_amount', 'submit_amount', 'fee_status']

        widgets = {
            'gr_number':forms.NumberInput(attrs={'class':'form-control', 'onchange': 'updateClassCodeDueAmountAndSection(this)'}),
            'class_code':forms.TextInput(attrs={'class':'form-control','readonly': 'readonly'}),
            'section_code':forms.TextInput(attrs={'class':'form-control','readonly': 'readonly'}),
            'due_amount':forms.NumberInput(attrs={'class':'form-control','readonly': 'readonly'}),
            'submit_amount':forms.NumberInput(attrs={'class':'form-control'}),
            # 'mounth':forms.Select(attrs={'class':'form-control'}),
            'fee_status':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }
    