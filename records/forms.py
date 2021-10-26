from django import forms


from .models import Record


class RecordForm(forms.ModelForm):
    
    class Meta:
        model = Record
        fields = [
            'title',
            'musicians',
            'notes',
            'record_url',
        ]
        labels = {
        'title': 'Record Title',
        'musicians': 'Musicians',
        'notes': 'My Notes',
        'record_url': 'URL for Cover',
        }