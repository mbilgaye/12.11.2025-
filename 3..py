# Write a program that implements a listener pattern, and asks for input from the user constantly.
# For every string entered, it displays the length of it and the number of words in it.
# If the string is empty, it will just be skipped using continue.
# If the input string is “break”, break out of the loop.

def main():
    while True:
        words = input("input a string or (break to stop)")

        if words == "break":
            break
        if words.strip() == '':
            continue
        length = len(words)
        word_count = len(words.split())
        print(f"length of words is {length} and word count is {word_count}")

if __name__ == "__main__":
    main()