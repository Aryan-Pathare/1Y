import re

def get_words_by_length():
    filename = "textfiles.txt"  # Specify the file in the code
    lengths = [3, 4, 5]  # Define desired word lengths
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text)  # Extract words using regex
            
            length_dict = {length: [] for length in lengths}  # Dictionary to store words by length
            
            for word in words:
                if len(word) in lengths:
                    length_dict[len(word)].append(word)
            
            for length in lengths:
                print(f"Words of length {length}: {set(length_dict[length])}")  # Print unique words
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

get_words_by_length()
