from django import forms
from .models import User_profile

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = [
            'name', 'surname', 'email', 'cellphone',
            'perfil_image', 'birthday',  
            # 'neighborhood', 'state', 'locality', 'country', 'status'
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            # 'status': forms.Select(),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = [
            
            #verificar quais informações são editáveis (não lembro se pode mudar de email)

            'name', 'surname', 'email', 'cellphone',
            'perfil_image', 'birthday', 
            # 'neighborhood', 'state', 'locality', 'country', 'status'
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            # 'status': forms.Select(),
        }
