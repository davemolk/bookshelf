from django import forms


from .models import Record


class RecordForm(forms.ModelForm):
    
    class Meta:
        model = Record
        fields = [
            'title',
            'notes',
            'record_url',
        ]
        labels = {
        'title': 'Record Title',
        'notes': 'My Notes',
        'record_url': 'URL for Cover',
        }