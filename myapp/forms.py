from django import forms


from .models import Aluno, Experimento_Pratico

class ExpForm(forms.ModelForm):

    class Meta:
        modek = Experimento_Pratico
        fields = ('experimento_p', 'temp_ebulicao_p', 'concentracao_p')