from django import forms

class AttendeeForm(forms.Form):
    first_name = forms.CharField(label = 'First Name', max_length=200)
    last_name = forms.CharField(label = 'Last Name', max_length=200)
    group = forms.Select()
