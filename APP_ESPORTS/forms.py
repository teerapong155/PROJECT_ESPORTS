from django import forms
from APP_ESPORTS.models import *
class RaceTypeForm(forms.ModelForm):
    class Meta:
        gender = (
            ('ชาย', 'ชาย'), ('หญิง', 'หญิง'))
        model = TypeList
        fields = ('nameType', 'gender')

        widgets = {
            'nameType': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'gender': forms.Select(choices=gender, attrs={'class': 'form-control'}),
        }
        labels = {
            'nameType': 'ประเภทการแข่ง',
            'gender': 'เพศ',
        }

    def deleteForm(self):
        self.fields['nameType'].widget.attrs['readonly'] = True
        self.fields['gender'].widget.attrs['readonly'] = True


class DirectorForm(forms.ModelForm):  # กรรมการ
    class Meta:
        GENDER = (
            ("male", "male"),
            ("female", "female"),
        )
        model = Director
        fields = ('name', 'gender', 'birthdate', 'tel', 'address')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'gender': forms.Select(choices=GENDER, attrs={'class': 'form-control'}),
            'birthdate': forms.NumberInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tel': forms.TextInput(attrs={'class ': 'form-control', 'size': 55, 'maxlength': 50}),
            'address': forms.TextInput(attrs={'class ': 'form-control', 'size': 200, 'maxlength': 50}),

        }
        labels = {
            'name': 'ชื่อกรรมการ',
            'gender': 'เพศ',
            'birthdate': 'วันเกิด',
            'tel': 'เบอร์โทร',
            'address': 'ที่อยู่',
        }

    def deleteForm(self):
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['gender'].widget.attrs['readonly'] = True
        self.fields['birthdate'].widget.attrs['readonly'] = True
        self.fields['tel'].widget.attrs['readonly'] = True
        self.fields['address'].widget.attrs['readonly'] = True


class AgeCategoryForm(forms.ModelForm):  # ประเภทอายุแข่ง
    class Meta:
        model = AgeCategory
        fields = ('name', 'desc')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'desc': forms.TextInput(attrs={'class ': 'form-control', 'size': 55, 'maxlength': 50}),
        }
        labels = {
            'name': 'ชื่อประเภท',
            'desc': 'รายละเอียด',
        }

    def deleteForm(self):
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['desc'].widget.attrs['readonly'] = True


class SeasonForm(forms.ModelForm):  # ประเภทอายุแข่ง
    class Meta:
        model = Season
        fields = ('name', 'desc')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'desc': forms.TextInput(attrs={'class ': 'form-control', 'size': 55, 'maxlength': 50}),
        }
        labels = {
            'name': 'ชื่อประเภท',
            'desc': 'รายละเอียด',
        }

    def deleteForm(self):
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['desc'].widget.attrs['readonly'] = True

class TeamFrom(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('nameTeam', 'logo','name1','name2','name3','name4','name5','name6'
                  ,'player1','player2','player3','player4','player5','player6',
                  'email1','email2','email2','email3','email4','email5','email6')

        widgets = {
            'nameTeam': forms.TextInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
            'logo':forms.FileInput(attrs={'class': 'form-control', 'accept':'image/*'}),
            'name1': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'name2': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'name3': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'name4': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'name5': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'name6': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'player1': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'player2': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'player3': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'player4': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'player5': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'player6': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'email1': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'email2': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'email3': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'email4': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'email5': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'email6': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),

        }
        labels = {
            'nameTeam' : 'ชื่อทีม',
            'logo': 'โลโก้',
            'name1': 'ชื่อคนที่ 1',
            'name2': 'ชื่อคนที่ 2',
            'name3': 'ชื่อคนที่ 3',
            'name4': 'ชื่อคนที่ 4',
            'name5': 'ชื่อคนที่ 5',
            'name6': 'ชื่อคนที่ 6',
            'player1': 'ชื่อในเกมคนที่ 1',
            'player2': 'ชื่อในเกมคนที่ 2',
            'player3': 'ชื่อในเกมคนที่ 3',
            'player4': 'ชื่อในเกมคนที่ 4',
            'player5': 'ชื่อในเกมคนที่ 5',
            'player6': 'ชื่อในเกมคนที่ 6',
            'email1': 'อีเมลคนที่ 1 ',
            'email2': 'อีเมลคนที่ 2',
            'email3': 'อีเมลคนที่ 3',
            'email4': 'อีเมลคนที่ 4',
            'email5': 'อีเมลคนที่ 5',
            'email6': 'อีเมลคนที่ 6'
        }
    def deleteForm(self):
        self.fields['nameTeam'].widget.attrs['readonly'] = True
        self.fields['name1'].widget.attrs['readonly'] = True


# class TeamVs(forms.ModelForm): #ประเภทอายุแข่ง
#     class Meta:
#         model = TeamVs
#         fields = ('nameTeam1', 'nameTeam2','score1','score2','logo1','logo2')
#         widgets = {
#             'nameTeam1': forms.TextInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
#             'nameTeam2': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
#             'score1': forms.TextInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
#             'score2': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
#             'logo1': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
#             'logo2': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
#         }
#         labels = {
#             'nameTeam1': 'ชื่อทีมที่ 1 ',
#             'nameTeam1': 'ชื่อทีมที่ 2',
#             'score1': 'คะแนนทีมที่ 1',
#             'score2': 'คะแนนทีมที่ 2',
#             'logo1': 'logo 1',
#             'logo1': 'logo 2',
#         }
