from django import forms
from .models import Classes, Section, Session, GRRegister, ClassRegister

# Classes
class ClassForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ['class_code', 'class_name']

        widgets = {
            'class_code':forms.NumberInput(attrs={'class':'form-control'}),
            'class_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Class Name'}),
        }

# Sections
class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['section_code', 'section_name']

        widgets = {
            'section_code':forms.NumberInput(attrs={'class':'form-control'}),
            'section_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Section Name'}),
        }

# Sessions
class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['session_code', 'session_name']

        widgets = {
            'session_code':forms.NumberInput(attrs={'class':'form-control'}),
            'session_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Session Name'}),
        }

# GR Registers
class GRRegisterPersonalForm(forms.ModelForm):
    class Meta:
        model = GRRegister
        fields = ['gr_number', 'name', 'father_name', 'gender','present']

        widgets = {
            'gr_number':forms.NumberInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'father_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Father Name'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'present':forms.TextInput(attrs={'class':'form-control'}),
        }

class GRRegisterForm(forms.ModelForm):
    class Meta:
        model = GRRegister
        fields = ['gr_number', 'name', 'father_name', 'address', 'date_of_birth','date_of_admission','class_of_admission','last_school','cell_number_1','cell_number_2','location','gender','class_of_removal','date_of_removal','present']

        widgets = {
            'gr_number':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'GR Number'}),
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'father_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Father Name'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'date_of_birth':forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date of Birth'}),
            'date_of_admission':forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date of Admission'}),
            'class_of_admission':forms.Select(attrs={'class':'form-control'}),
            'last_school':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last School'}),
            'cell_number_1':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cell No. 1'}),
            'cell_number_2':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cell No. 2'}),
            'location':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}),
            'gender':forms.Select(attrs={'class':'form-control', 'placeholder':'Location'}),
            'class_of_removal':forms.Select(attrs={'class':'form-control'}),
            'date_of_removal':forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date of removal'}),
            'present':forms.TextInput(attrs={'class':'form-control'}),
        }

# Class Register
class ClassRegisterForm(forms.ModelForm):
    class Meta:
        model = ClassRegister
        fields = ['gr_number', 'class_code', 'section_code', 'session_code', 'present']

        widgets = {
            'gr_number':forms.Select(attrs={'class':'form-control'}),
            'class_code':forms.Select(attrs={'class':'form-control'}),
            'section_code':forms.Select(attrs={'class':'form-control'}),
            'session_code':forms.Select(attrs={'class':'form-control'}),
            'present':forms.TextInput(attrs={'class':'form-control'}),
        }