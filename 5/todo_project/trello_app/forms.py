from django import forms
from .models import Test
#class TestForm(forms.Form):
    # fields map to the input
    # widget provide extra thing which give feature like giving  big textbox to desc and drop down date features 
   # name=forms.CharField(max_length=50)
   # desc = forms.CharField(widget=forms.Textarea)
  #  created_at = forms.CharField(widget=forms.DateTime)
 #   due_date = forms.CharField(widget=forms.DateTimeInput)

# there was the issue in wiget so django provide extra thing model where u have define in model it will automatically convert into form

class TestForm(forms.ModelForm):
    # it allow  you to connect with the model directly
    # u dont have 
    class Meta :
        model = Test
       ## fields='__all__'
        fields =['name','desc','due_date','name_2','list']
        widgets={ 'due_date':forms.DateTimeInput(attrs={'type':'datetime-local'})}
      ##  widgets={ 'created_at':forms.DateTimeInput(attrs={'type':'datetime-local'})}