import os
from django.conf import settings
from django.core.management.base import BaseCommand
import pandas as pd
from user_profile.models import Neighborhood

class Command(BaseCommand):
    help = 'Importa dados de um arquivo Excel para o banco de dados'

    def handle(self, *args, **kwargs):
        # Caminho para o arquivo Excel na raiz do projeto
        arquivo_excel = os.path.join(settings.BASE_DIR, 'Bairro_Processado.xlsx')

        try:
            # Lê o Excel
            dados = pd.read_excel(arquivo_excel)

            # Validar as colunas necessárias
            colunas_necessarias = {'id', 'bairro', 'cidade', 'estado'}
            if not colunas_necessarias.issubset(dados.columns):
                raise ValueError(f'O arquivo Excel deve conter as colunas: {colunas_necessarias}')

            # Itera sobre as linhas e cria os objetos no banco
            for _, linha in dados.iterrows():
                # Cria uma instância do modelo Neighborhood
                neighborhood = Neighborhood(
                    name=linha['bairro'],       # Mapeia 'bairro' para 'name'
                    locality=linha['cidade'],   # Mapeia 'cidade' para 'locality'
                    state=linha['estado'],      # Mapeia 'estado' para 'state'
                )
                # Salva no banco, aplicando validações
                neighborhood.save()

            self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao importar os dados: {e}'))
