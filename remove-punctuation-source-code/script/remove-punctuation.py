import string

def remover_pontuacao(texto):
    translator = str.maketrans('', '', string.punctuation)
    texto_sem_pontuacao = texto.translate(translator)
    return texto_sem_pontuacao

def processar_arquivo(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as input_file:
            texto = input_file.read()

        texto_sem_pontuacao = remover_pontuacao(texto)

        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(texto_sem_pontuacao)

        print(f"Pontuação removida e texto salvo em {output_path}")

    except FileNotFoundError:
        print(f"Arquivo {input_path} não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

input_path = './input/in.txt'
output_path = './output/out.txt'

processar_arquivo(input_path, output_path)
