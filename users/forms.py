from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True) # Email requied.

    def clean_email(self):
        """Checking to see if e-mail is in use."""
        if CustomUser.objects.filter(email=self.cleaned_data['email'].lower()).exists():

            raise forms.ValidationError("The given E-mail is already registered.")

        return self.cleaned_data['email']

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email'].lower()
        if commit:
            user.save()
        return user


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'age',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age',)