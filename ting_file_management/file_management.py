import sys
from os.path import exists


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not exists(path_file):
        return print(f'Arquivo {path_file} não encontrado', file=sys.stderr)

    if (path_file[-3:] != 'txt'):
        print('Formato inválido', file=sys.stderr)

    with open(path_file, mode='r') as arquivo_txt:
        linhas = arquivo_txt.read().splitlines()
        return linhas
