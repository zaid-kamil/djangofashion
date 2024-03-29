from django import forms

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'first_name', 'last_name', 'gender',  'bio']