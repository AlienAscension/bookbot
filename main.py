# Define the main function to process the text file
def main():
    # Define the path to the text file
    file_path = 'books/frankenstein.txt'
    
    # Read the content of the text file
    text = get_book_text(file_path)
    
    # Count the number of words in the text
    num_words = count_words(text)
    
    # Count the occurrences of each letter in the text
    letters = count_letters(text)
    
    # Convert the letter count dictionary into a list of dictionaries
    liste = dict_to_list_of_dicts(letters)
    
    # Log the output of the analysis
    log_output(liste, num_words, file_path)


# Function to read the content of the text file
def get_book_text(path):
    with open(path, "r") as f:
        return f.read()


# Function to count the number of words in the text
def count_words(text):
    count = text.split()
    return len(count)


# Function to count the occurrences of each letter in the text
def count_letters(text):
    letter_count = {}
    lower_text = text.lower()

    for i in lower_text:
        if i not in letter_count:
            letter_count[i] = 1
        else:
            letter_count[i] += 1
    return letter_count


# Function to log the output of the analysis
def log_output(lst, num_words, file_path):
    print(f"--- Begin report of {file_path} ---")
    print((f"{num_words} words found in the document\n"))
    
    # Sort the list of dictionaries based on the 'num' key in descending order
    sorted_list = sorted(lst, key=lambda x: x["num"], reverse=True)

    # Iterate over the sorted list and print the character counts
    for item in sorted_list:
        # Skip non-alphabetic characters
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")

    print("--- End report ---")


# Function to define the sorting criteria based on the 'num' key
def sort_on(dict):
    return dict["num"]


# Function to convert a dictionary to a list of dictionaries
def dict_to_list_of_dicts(dict):
    list_of_dicts = []
    for i in dict:
        empty_dict = {}
        empty_dict["char"] = i
        empty_dict["num"] = dict[i]
        list_of_dicts.append(empty_dict)
    return list_of_dicts

# Call the main function to start the analysis
main()
