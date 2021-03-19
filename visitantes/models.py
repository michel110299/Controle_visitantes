from django.db import models


class Visitante(models.Model):

    nome_completo = models.CharField(
        verbose_name = "Nome Completo",
        max_length = 194,
    )

    cpf = models.CharField(
        verbose_name = "CPF",
        max_length = 11,
    )
    data_nascimento = models.DateField(
        verbose_name = "Data de nascimento",
        auto_now = False,
        auto_now_add = False,
    )
    numero_casa = models.PositiveSmallIntegerField(
        verbose_name = "Numero da casa a ser visitada",
    )
    placa_veiculo = models.CharField(
        verbose_name = "Placa de veiculo",
        max_length = 7,
        blank = True,
        null = True,
    )
    horario_chegada = models.DateTimeField(
        verbose_name= "Horário de chegada na portaria",
        auto_now_add = True,
    )
    horario_saida = models.DateTimeField(
        verbose_name="Horário de saída do condominio",
        auto_now= False,
        blank = True, 
        null = True,
    )
    horario_autorizacao = models.DateTimeField(
        verbose_name = "Horário de autorização de entrada",
        auto_now = False,
        blank = True, 
        null = True,
    )
    moderador_responsavel = models.CharField(
        verbose_name="Nome do morador ao autorizar a entrada do visitante",
        max_length= 194,
        blank = True,
    )
    registrado_por = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name = "Porteiro responsavél pelo registro",
        on_delete = models.PROTECT, 
    )

    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
        return "Horário de saida não registrado"

    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao
        return "Visitante aguardando autorização"

    def get_morador_responsavel(self):
        if self.moderador_responsavel:
            return self.moderador_responsavel
        return "Visitante aguardando autorização"
        
    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
        return "Veículo não registrado"
    
    class meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "Visitante"
    
    def __str__(self):
        return self.nome_completo 

