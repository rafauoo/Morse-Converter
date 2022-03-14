import argparse as arg

code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}


def parse():
    parser = arg.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    return args.filename


def modify_line(line):
    modified_line = ""
    for char in line:
        if char in code.keys():
            modified_line += char
        elif char == " ":
            modified_line += char
    return modified_line


def output_maker():
    output = []
    with open(parse()) as txt:
        for line in txt:
            modified_line = modify_line(line)
            o_line = ""
            for index, char in enumerate(modified_line):
                if char != " ":
                    o_line += code[char]
                    if index != len(modified_line) - 1:
                        o_line += " "
                elif index > 0 and modified_line[index - 1] != " ":
                    o_line += "/ "
            output.append(o_line)
    return output


def main():
    output = output_maker()
    for line in output:
        print(line)


if __name__ == "__main__":
    main()