# Remoção de Pontuação em Texto com Python

Este é um utilitário em Python para remover pontuação de texto em um arquivo de texto. Ele utiliza a biblioteca `string` do Python para identificar e remover sinais de pontuação.

### Estrutura do Diretório

- A pasta **[Código Fonte da Remoção de Pontuação](./remove-punctuation-source-code/)** contém as entradas e saídas usadas no projeto criado, bem como o código fonte em si.
- Na pasta **[Script](./remove-punctuation-source-code/script/)**, você encontrará o código fonte do projeto.

## Como Funciona

O utilitário lê um arquivo de texto e remove toda a pontuação, criando um novo arquivo sem pontuação. Ele utiliza as funções `str.maketrans` e `str.translate` para realizar essa tarefa.

## Como Usar

Siga estes passos para remover pontuação de um arquivo de texto:

1. Clone este repositório ou baixe o código fonte para o seu ambiente local.

2. Modifique a variável `nome_arquivo_entrada` para especificar o caminho do seu arquivo de texto de entrada (`in.txt`).

3. Modifique a variável `nome_arquivo_saida` para especificar o caminho e nome do arquivo de saída onde o texto sem pontuação será salvo.

4. Execute o script Python fornecido (`remove_punctuation.py`). Este script processará o arquivo de texto de entrada, removerá a pontuação e salvará o texto limpo no arquivo de saída.

5. Após a execução, o texto sem pontuação será salvo no arquivo de saída.

## Por que Remover a Pontuação?

Remover pontuação do texto pode ser útil em várias tarefas de processamento de linguagem natural e análise de texto, além de simplificar o texto para determinadas aplicações.

***

# Text Punctuation Removal with Python

This is a Python utility for removing punctuation from text in a text file. It uses the Python `string` library to identify and remove punctuation marks.

### Folder Structure

- The **[Remove Punctuation Source Code](./remove-punctuation-source-code/)** folder contains the inputs and outputs used in the created project, as well as the source code itself.
- In the **[Script](./remove-punctuation-source-code/script/)** folder, you will find the source code for the project.

## How It Works

The utility reads a text file and removes all punctuation, creating a new file without punctuation. It uses the `str.maketrans` and `str.translate` functions to perform this task.

## How to Use

Follow these steps to remove punctuation from a text file:

1. Clone this repository or download the source code to your local environment.

2. Modify the `nome_arquivo_entrada` variable to specify the path to your input text file (`in.txt`).

3. Modify the `nome_arquivo_saida` variable to specify the path and name of the output file where the text without punctuation will be saved.

4. Run the provided Python script (`remove_punctuation.py`). This script will process the input text file, remove punctuation, and save the cleaned text to the output file.

5. After execution, the punctuation-free text will be saved in the output file.

## Why Remove Punctuation?

Removing punctuation from text can be useful in various natural language processing and text analysis tasks, as well as simplifying text for certain applications.