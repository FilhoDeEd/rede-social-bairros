import os
from django.conf import settings
from django.core.management.base import BaseCommand
import pandas as pd
from user_profile.models import Neighborhood  # Ajuste para o nome real do seu modelo

class Command(BaseCommand):
    help = 'Importa dados de um arquivo Excel para o banco de dados'

    def handle(self, *args, **kwargs):
        # Caminho para o arquivo Excel na raiz do projeto
        arquivo_excel = os.path.join(settings.BASE_DIR, 'Bairro_Processado.xlsx')

        try:
            # Lê o Excel
            dados = pd.read_excel(arquivo_excel)

            # Validar as colunas necessárias
            colunas_necessarias = {'Bairro', 'Cidade', 'Estado'}
            if not colunas_necessarias.issubset(dados.columns):
                raise ValueError(f'O arquivo Excel deve conter as colunas: {colunas_necessarias}')

            # Itera sobre as linhas e cria os objetos no banco
            for _, linha in dados.iterrows():
                Neighborhood.objects.create(
                    bairro=linha['Bairro'],
                    cidade=linha['Cidade'],
                    estado=linha['Estado']
                )

            self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao importar os dados: {e}'))
