from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    # Verificação para ignorar arquivos com o mesmo nome
    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None

    # Validações e leitura do TXT baseado na função "txt_importer"
    importar_txt = txt_importer(path_file)

    # Formata as informações de acordo com o Readme
    txt_processado = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(importar_txt),
        'linhas_do_arquivo': importar_txt
    }

    # Coloca a nova instância (Arquivo processado) na fila
    instance.enqueue(txt_processado)
    # Reademe pede que cada saída seja enviada pelo stdout
    sys.stdout.write(str(txt_processado))


def remove(instance):
    if not instance:
        return sys.stdout.write("Não há elementos\n")
    tirar_da_fila = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {tirar_da_fila} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        # Busca pelo index do arquivo e exibe como string
        busca_txt = instance.search(position)
        return sys.stdout.write(str(busca_txt))
    except IndexError:
        print('Posição inválida', file=sys.stderr)
