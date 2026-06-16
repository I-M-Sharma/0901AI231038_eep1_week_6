import sys
import os
import collections

def process_files(folder_path):
    file_data = {}
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        sys.exit(1)
        
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                file_data[filename] = f.read()
    return file_data

def handle_stats(filename, file_data):
    if filename not in file_data:
        print(f"Error: {filename} not found.")
        return
    text = file_data[filename]
    lines = len(text.splitlines())
    words = len(text.split())
    chars = len(text)
    print(f"Stats for {filename}:")
    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Characters: {chars}")

def handle_top(n, filename, file_data):
    if filename not in file_data:
        print(f"Error: {filename} not found.")
        return
    try:
        n = int(n)
    except ValueError:
        print("Error: n must be an integer.")
        return
        
    text = file_data[filename].lower()
    words = text.split()
    counter = collections.Counter(words)
    print(f"Top {n} words in {filename}:")
    for word, count in counter.most_common(n):
        print(f"{word}: {count}")

def handle_search(word, file_data):
    word = word.lower()
    found_in = []
    for filename, text in file_data.items():
        if word in text.lower().split():
            found_in.append(filename)
    
    if found_in:
        print(f"Word '{word}' found in:")
        for fn in sorted(found_in):
            print(f"- {fn}")
    else:
        print(f"Word '{word}' not found in any files.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze.py <folder_path>")
        sys.exit(1)
        
    folder_path = sys.argv[1]
    file_data = process_files(folder_path)
    
    print("Welcome to the interactive text analyzer!")
    while True:
        try:
            command_line = input("> ").strip()
        except EOFError:
            break
            
        if not command_line:
            continue
            
        parts = command_line.split()
        cmd = parts[0].lower()
        
        if cmd == "quit":
            print("Goodbye!")
            break
        elif cmd == "stats" and len(parts) == 2:
            handle_stats(parts[1], file_data)
        elif cmd == "top" and len(parts) == 3:
            handle_top(parts[1], parts[2], file_data)
        elif cmd == "search" and len(parts) == 2:
            handle_search(parts[1], file_data)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
