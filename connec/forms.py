from django import forms




class FormPostgres(forms.Form):
    host = forms.CharField(initial='localhost', max_length=255)
    port = forms.IntegerField(required=False, initial='5432')
    database = forms.CharField(max_length=255)
    user = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput,
                               required=False)
    table = forms.CharField(max_length=255)

class FormMySQL(forms.Form):
    host = forms.CharField(initial='localhost', max_length=255)
    port = forms.IntegerField(required=False, initial='3306')
    database = forms.CharField(max_length=255)
    user = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput,
                               required=False)
    table = forms.CharField(max_length=255)