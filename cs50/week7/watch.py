import re
import sys

def main():
    link_youtube = input("HTML: ")
    print(parse(link_youtube))

def parse(s):
    link = re.search(r".+src=\"https?:\/\/(www\.)?youtube\.com\/embed\/([a-zA-Z0-9]+)\".+",s)
    if link:
        return f"youtu.be/{link.group(2)}"
    else:
        return None
if __name__ == "__main__":
    main()