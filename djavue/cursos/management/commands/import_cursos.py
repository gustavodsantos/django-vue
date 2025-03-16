import os

from django.core.management.base import BaseCommand

from djavue.cursos.models import Curso


class Command(BaseCommand):
    help = 'Importa cursos de um arquivo TXT'

    def handle(self, *args, **options):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = current_dir
        while not os.path.exists(os.path.join(base_dir, 'manage.py')):
            base_dir = os.path.dirname(base_dir)
            if base_dir == '/':
                raise FileNotFoundError('manage.py não encontrado')

        arquivo_txt = os.path.join(base_dir, 'cursos_realizados.txt')

        try:
            with open(arquivo_txt, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                cursos = conteudo.split('\n\n')

                for curso_texto in cursos:
                    if not curso_texto.strip():
                        continue

                    linhas = curso_texto.split('\n')
                    titulo = linhas[0].strip()
                    descricao = '\n'.join(linhas[1:]).strip() if len(linhas) > 1 else None

                    Curso.objects.create(titulo=titulo, descricao=descricao)

            self.stdout.write(self.style.SUCCESS(f'Cursos importados com sucesso de {arquivo_txt}'))
        except FileNotFoundError as e:
            self.stdout.write(self.style.ERROR(f'Arquivo não encontrado: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocorreu um erro: {e}'))
