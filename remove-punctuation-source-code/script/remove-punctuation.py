import string

def remover_pontuacao(texto):
    translator = str.maketrans('', '', string.punctuation)
    texto_sem_pontuacao = texto.translate(translator)
    return texto_sem_pontuacao

nome_arquivo_entrada = './input/in.txt'
nome_arquivo_saida = './output/out.txt'

with open(nome_arquivo_entrada, 'r', encoding='utf-8') as arquivo_entrada:
    texto = arquivo_entrada.read()

texto_sem_pontuacao = remover_pontuacao(texto)

with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(texto_sem_pontuacao)

print(f"Pontuação removida e texto salvo em {nome_arquivo_saida}")
