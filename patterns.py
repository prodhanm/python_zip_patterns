chars = [".", "-", "#", "=", "*", "+", "@", "!", "."]
repetitions = [5, 4, 3, 2, 1, 2, 3, 4, 5]

def zip_patterns(chars,repetitions):
    for char1, char2 in zip(chars,repetitions):
        print(char1 * char2)

def main():
    zip_patterns(chars,repetitions)

if __name__ == "__main__":
    main()