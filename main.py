

def main():

    file_path = 'books/frankenstein.txt'
    text = get_book_text(file_path)
    num_words = count_words(text)
    letters = count_letters(text)
    #print(f"{num_words} words found in the document")
    #print(letters)
    liste = dict_to_list_of_dicts(letters)
    log_output(liste, num_words, file_path)


def get_book_text(path):
    with open(path, "r") as f:
        return f.read()


def count_words(text):
    count = text.split()
    return len(count)

def count_letters(text):
    letter_count = {}
    lower_text = text.lower()

    for i in lower_text:
        if i not in letter_count:
            letter_count[i] = 1
        else:
            letter_count[i] += 1
    return letter_count

def log_output(lst, num_words, file_path):
    print(f"--- Begin report of {file_path} ---")
    print((f"{num_words} words found in the document\n"))
    
    sorted_list = sorted(lst, key=lambda x: x["num"], reverse=True)

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")

    print("--- End report ---")

def sort_on(dict):
    return dict["num"]


def dict_to_list_of_dicts(dict):
    list_of_dicts = []
    for i in dict:
        empty_dict = {}
        empty_dict["char"] = i
        empty_dict["num"] = dict[i]
        list_of_dicts.append(empty_dict)
    return list_of_dicts

main()