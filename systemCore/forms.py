from django import forms
from .models import Person

caca = Person.get_all_people()
FAVORITE_COLORS_CHOICES = []

for person in caca:
    FAVORITE_COLORS_CHOICES.append(tuple((getattr(person, 'pk'), getattr(person, 'first_name'))))

class form1(forms.Form):
    UserType = forms.CharField(
        widget=forms.Select(choices=FAVORITE_COLORS_CHOICES)
    )
    