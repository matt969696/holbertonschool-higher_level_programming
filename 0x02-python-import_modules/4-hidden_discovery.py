#!/usr/bin/python3


def main():
    import hidden_4

    for word in dir(hidden_4):
        if "__" not in word:
            print(word)


if __name__ == "__main__":
    main()
