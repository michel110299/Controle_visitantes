from django import forms
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = ["nome_completo","cpf","data_nascimento","numero_casa","placa_veiculo"]
        error_messages = {
            "nome_completo" : {
                "required": "O nome completo do visitante é obrigatório para o registro"
            },
            "cpf" : {
                "required": "O cpf do visitante é obrigatório para o registro"
            },
            "data_nascimento" : {
                "required": "A data de nascimento do visitante é obrigatória para o registro",
                "invalid": "Por favor, informe um formato válido para a data de nascimento (DD/MM/AAAA) "
            },
            "numero_casa" : {
                "required": "Porfavor, informe o numero da casa a ser visitada"
            },


        }
class AutorizaVisitanteForm(forms.ModelForm):
    moderador_responsavel = forms.CharField(required=True)
    class Meta:
        model = Visitante

        fields = {
            "moderador_responsavel"
        }
        error_messages = {
            "moderador_responsavel":{
                "required " : "Por favor, informe o nome do morador responsável por autorizar a entrada o visitante"
            }
              
        }