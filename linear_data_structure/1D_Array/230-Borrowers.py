import sys

def main():
    books = {}
    shelf = []
    borrowed = set()
    returned = []

    # Read book list
    while True:
        line = input()
        if line == "END":
            break
        title, author = line.split('" by ')
        title = title[1:]  # remove leading quote
        books[title] = author
        shelf.append(title)

    # Sort shelf by (author, title)
    shelf.sort(key=lambda t: (books[t], t))

    while True:
        line = input()
        if line == "END":
            break
        if line.startswith("BORROW"):
            title = line.split('"')[1]
            borrowed.add(title)
        elif line.startswith("RETURN"):
            title = line.split('"')[1]
            borrowed.remove(title)
            returned.append(title)
        elif line == "SHELVE":
            returned.sort(key=lambda t: (books[t], t))
            for book in returned:
                index = -1
                for i, b in enumerate(shelf):
                    if b == book:
                        continue
                    if b not in borrowed and (books[b], b) < (books[book], book):
                        index = i
                if index == -1:
                    print(f'Put "{book}" first')
                else:
                    print(f'Put "{book}" after "{shelf[index]}"')
            print("END")
            returned.clear()

if __name__ == "__main__":
    main()
