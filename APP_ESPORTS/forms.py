from django import forms
from APP_ESPORTS.models import *
class RaceTypeForm(forms.ModelForm):
    class Meta:
        model = typeList
        fields = ('nameType', 'gender')
        gender = [('ชาย'),('หญิง')]
        widgets = {
            'nameType': forms.TextInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
            'gender': forms.Select(choices=gender),
        }
        labels = {
            'nameType': 'ประเภทการแข่ง',
            'gender': 'เพศ',
        }

class Director(forms.ModelForm): #กรรมการ
    class Meta:
        model = Director
        fields = ('name', 'gender','brithDay','tel','address')
        gender = [('ชาย'),('หญิง')]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
            'gender': forms.Select(choices=gender),
            'birthDay': forms.TextInput(attrs={'class ': 'form-control',  'size':55, 'maxlength':50}),
            'tel': forms.TextInput(attrs={'class ': 'form-control', 'size': 55, 'maxlength': 50}),
            'address': forms.TextInput(attrs={'class ': 'form-control', 'size': 200, 'maxlength': 50}),

        }
        labels = {
            'name': 'ชื่อกรรมการ',
            'gender': 'เพศ',
            'birthday': 'วันเกิด',
            'tel': 'เบอร์โทร',
            'address': 'ที่อยู่',
        }

class AgeCategory(forms.ModelForm): #ประเภทอายุแข่ง
    class Meta:
        model = AgeCategory
        fields = ('name', 'desc')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
            'desc': forms.TextInput(attrs={'class ': 'form-control', 'size': 55, 'maxlength': 50}),
        }
        labels = {
            'name': 'ชื่อประเภท',
            'desc': 'รายละเอียด',
        }

class Season(forms.ModelForm): #ประเภทอายุแข่ง
    class Meta:
        model = AgeCategory
        fields = ('name', 'desc')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
            'desc': forms.TextInput(attrs={'class ': 'form-control', 'size': 55, 'maxlength': 50}),
        }
        labels = {
            'name': 'ชื่อประเภท',
            'desc': 'รายละเอียด',
        }

