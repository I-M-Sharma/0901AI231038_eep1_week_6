```python
import os
import sys

def load_files(folder_path):
    files = {}

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                files[filename] = f.read()

    return files


def stats(filename, files):
    if filename not in files:
        print("File not found.")
        return

    text = files[filename]

    line_count = len(text.splitlines())
    word_count = len(text.split())
    char_count = len(text)

    print("Lines:", line_count)
    print("Words:", word_count)
    print("Characters:", char_count)


def top_words(n, filename, files):
    if filename not in files:
        print("File not found.")
        return

    try:
        n = int(n)
    except ValueError:
        print("n must be an integer.")
        return

    words = files[filename].lower().split()

    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    sorted_words = sorted(
        counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("Top", n, "words:")

    for word, count in sorted_words[:n]:
        print(word, count)


def search(word, files):
    word = word.lower()

    found_files = []

    for filename in files:
        words = files[filename].lower().split()

        if word in words:
            found_files.append(filename)

    if len(found_files) == 0:
        print("Word not found in any file.")
    else:
        print("Found in:")

        for filename in found_files:
            print(filename)


def main():
    if len(sys.argv) != 2:
        print("Usage: python analyze.py <folder_path>")
        return

    folder_path = sys.argv[1]

    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    files = load_files(folder_path)

    print("Interactive Text Corpus Analyzer")

    while True:
        command = input("> ").strip()

        if command == "":
            continue

        parts = command.split()

        if parts[0].lower() == "quit":
            print("Goodbye!")
            break

        elif parts[0].lower() == "stats":
            if len(parts) != 2:
                print("Usage: stats <filename>")
            else:
                stats(parts[1], files)

        elif parts[0].lower() == "top":
            if len(parts) != 3:
                print("Usage: top <n> <filename>")
            else:
                top_words(parts[1], parts[2], files)

        elif parts[0].lower() == "search":
            if len(parts) != 2:
                print("Usage: search <word>")
            else:
                search(parts[1], files)

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
```
