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