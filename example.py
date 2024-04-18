import re

def extract_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            # Use regular expression to find all numbers in the text
            numbers = re.findall(r'\d+', text)
            return numbers
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

def main():
    file_path = input("test.txt")
    numbers = extract_numbers_from_file(file_path)
    if numbers:
        print("Numbers found in the file:")
        for number in numbers:
            print(number)
    else:
        print("No numbers found in the file.")

if __name__ == "__main__":
    main()
