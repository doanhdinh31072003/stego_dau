import sys

def extract_bits_from_commas(text):
    lines = text.split('\n')
    bits = []

    for line in lines:
        if ", và " in line:
            bits.append('1')
        elif " và " in line:
            bits.append('0')

    return ''.join(bits)

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract.py [hidden_text.txt]")
        return

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        text = f.read()

    bitstring = extract_bits_from_commas(text)

    with open("extracted_bits.txt", "w") as f:
        f.write(bitstring)

    print(f"Đã trích xuất {len(bitstring)} bit vào extracted_bits.txt")

if __name__ == "__main__":
    main()
