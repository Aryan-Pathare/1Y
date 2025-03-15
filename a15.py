# Python program to read a file and print words of a given length

# Get filename from the user
filename = input("Enter the filename: ")

# Get word length from the user
word_length = int(input("Enter the word length to search for: "))

try:
    # Open the file and read content
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        
        # Filter words based on length
        matching_words = []
        for word in words:
            clean_word = word.strip(".,!?;:")
            if len(clean_word) == word_length:
                matching_words.append(clean_word)
        
        # Display matching words
        if matching_words:
            print("Words of length", word_length, ":", ", ".join(matching_words))
        else:
            print("No words of that length found.")
except FileNotFoundError:
    print("Error: File not found! Please check the filename and try again.")