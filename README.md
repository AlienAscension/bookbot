# bookbot

BookBot is my first guided project from Boot.dev!

BookBot is a Python script that analyzes a text file and generates a report on the occurrences of each letter in the text.

## Features

- Counts the number of words in the text file.
- Analyzes the occurrences of each letter (case-insensitive) in the text file.
- Generates a report on the letter frequencies.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/AlienAscension/bookbot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd bookbot
    ```

3. Edit the path in the main.py to the document you want to analyse:

    ```bash
    file_path = 'books/frankenstein.txt'
    ```

4. run the main.py:

    ```bash
    python main.py
    ```



## Example Output

--- Begin report of books/frankenstein.txt ---  
77986 words found in the document

The e character was found 89288 times   
The t character was found 61902 times  
The a character was found 48991 times  
...  \
  \
--- End report ---


