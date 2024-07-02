# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email', 'password1', 'password2')
from django import forms
from .models import Recipe

# forms.py

from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['DishName', 'DishType', 'DishSort', 'DishTime', 'ProductOtherProducts', 'Machinery']

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']

RecipeImageFormSet = inlineformset_factory(Recipe, RecipeImage, form=RecipeImageForm, extra=1, can_delete=True)


from django import forms

class SearchRecipeForm(forms.Form):
    word1 = forms.CharField(required=False)
    word2 = forms.CharField(required=False)
    word3 = forms.CharField(required=False)
    dishtime = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        keywords = [cleaned_data.get(f'word{i}') for i in range(1, 4)]
        cleaned_data['keywords'] = [kw for kw in keywords if kw]
        return cleaned_data
