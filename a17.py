# Python program to sort city names from a file and save to another file

# Get filenames from user
input_filename = input("Enter input filename: ")
output_filename = input("Enter output filename: ")

try:
    # Read city names from file
    with open(input_filename, 'r') as file:
        cities = file.readlines()
    
    # Sort city names alphabetically
    cities = sorted(city.strip() for city in cities)
    
    # Write sorted names to output file
    with open(output_filename, 'w') as file:
        for city in cities:
            file.write(city + "\n")
    
    print("Cities sorted and saved in", output_filename)
except FileNotFoundError:
    print("Error: File not found!")
