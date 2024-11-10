import re
def main():
    text = input("Text: ")
    print(count(text))

def count(text):
    x = re.findall(r"\b(um|Um)\b",text)
    return len(x)
if __name__ == "__main__":
    main()