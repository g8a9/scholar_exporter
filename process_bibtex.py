import re
import sys

def extract_citations(bib_file):
    with open(bib_file, 'r', encoding='utf-8') as f:
        content = f.read()
    # Regex pattern to extract citation keys
    pattern = re.compile(r'@\w+{(.*?),')
    citations = pattern.findall(content)
    return list(reversed(citations))  # Reverse order

def main(bib_file):
    citations = extract_citations(bib_file)
    for cite in citations:
        print(f"\\fullcite{{{cite}}}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <bibliography.bib>")
        sys.exit(1)
    main(sys.argv[1])

