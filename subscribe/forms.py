from django.forms import forms, ModelForm

from user.models import UserProfile

class UserProfileform(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'revenue', 'sub']
        
        