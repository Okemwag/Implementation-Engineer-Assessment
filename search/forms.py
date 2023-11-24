from django import forms
from .models import Search



class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['item', 'details']
        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'item': 'Item',
            'details': 'Details',
        }
        
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['item'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        