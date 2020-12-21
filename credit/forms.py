import datetime
from django import forms

from .models import Borrower, Blacklist


class CreditForm(forms.ModelForm):
    # price = forms.IntegerField(help_text='how much do you want to borrow?', required=True)

    class Meta:
        model = Borrower
        fields = ["iin"]


    # def save(self, commit=True):
    #     super().save(commit)
    #
    #     self.instance.birthday =


    # age_min = self.cleaned_data['age_min']
        # if age_min < 18:
        #     raise forms.ValidationError('Заемщик не подходит по возрасту')
        #
        # return age_min

    # def clean_inn(self):
    #      inn = self.cleaned_data['id']
    #      if inn
    #
    # def clean(self):
    #     iin = self.c
