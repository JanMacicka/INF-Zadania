def rect(width, char="*"):
        print(char * width)
        print(char + " " * (width - 2 * len(char)) + char)
        print(char * width)
