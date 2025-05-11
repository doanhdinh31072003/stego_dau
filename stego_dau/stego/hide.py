import sys
def hide_bits_with_commas(text, bitstring):
    lines = text.split('\n')
    result = []
    bit_index = 0

    for line in lines:
        if bit_index >= len(bitstring):
            result.append(line)
            continue

        bit = bitstring[bit_index]

        if bit == '0':
            if ", và " in line:
                line = line.replace(", và ", " và ", 1)
                bit_index += 1
            elif " và " in line:
                # đã đúng, không cần sửa
                bit_index += 1
        elif bit == '1':
            if ", và " in line:
                    # đã đúng, không cần sửa
                bit_index += 1
            elif " và " in line:
                line = line.replace(" và ", ", và ", 1)
                bit_index += 1
         

        result.append(line)

    return '\n'.join(result), bit_index



def main():
    if len(sys.argv) != 3:
        print("Usage: python3 hide.py [input_text.txt] [binary.txt]")
        return

    text_file = sys.argv[1]
    binary_file = sys.argv[2]

    with open(text_file, "r", encoding="utf-8") as f:
        text = f.read()

    with open(binary_file, "r") as f:
        bitstring = f.read().strip()

    hidden_text, used = hide_bits_with_commas(text, bitstring)

    with open("hidden_text.txt", "w", encoding="utf-8") as f:
        f.write(hidden_text)

    print(f"Đã giấu {used}/{len(bitstring)} bits vào hidden_text.txt")

if __name__ == "__main__":
    main()
