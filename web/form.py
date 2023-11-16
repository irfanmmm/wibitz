from django.forms import ModelForm
from django import forms
from django.forms.widgets import EmailInput,TextInput,Select
from web.models import Contact
from web.models import COMPONY_SIZE,INDUSTRY,JOB_ROLE,COUNTRY


#                      "empty"-> "placeholder" + options
EMPTY_COMPONY_SIZE = (("","Compony Size"),) + COMPONY_SIZE
EMPTY_INDUSTRY = (("","Industry"),) + INDUSTRY
EMPTY_JOB_ROLE = (("","Jobe Role"),) + JOB_ROLE
EMPTY_COUNTRY = (("","Country"),) + COUNTRY




class ContactForm(ModelForm):
    compony_size = forms.ChoiceField(choices=EMPTY_COMPONY_SIZE)
    indutry = forms.ChoiceField(choices=EMPTY_INDUSTRY)
    job_role = forms.ChoiceField(choices=EMPTY_JOB_ROLE)
    country = forms.ChoiceField(choices=EMPTY_COUNTRY)

    class Meta:
        model = Contact
        #  ella fieldsum edukkan
        fields = "__all__"
        widgets = {
            "email": EmailInput(attrs={"placeholder":"Work email"}),
            "first_name": TextInput(attrs={"placeholder":"First Name"}),
            "last_name": TextInput(attrs={"placeholder":"First Name"}),
            "compony": TextInput(attrs={"placeholder":"Compony"}),
        }