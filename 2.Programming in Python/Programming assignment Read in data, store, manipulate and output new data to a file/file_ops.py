def read_file(file_name: str) -> str:
    with open(file_name, mode="r") as file:
        textLine = file.read()
        print(textLine)
        return textLine


def read_file_into_list(file_name: str) -> list:
    with open(file_name, mode="r") as file:
        fileContent = []
        for textLine in file.readlines():
            fileContent.append(textLine)
        return fileContent


def write_first_line_to_file(file_contents: str, output_filename: str) -> None:
    with open(output_filename, mode="w") as outputFile:
        splitted = file_contents.split("\n")
        outputFile.write(splitted[0])


def read_even_numbered_lines(file_name: str) -> list:
    with open(file_name, mode="r") as file:
        evenNumberedLines = []
        cnt = 0
        for line in file.readlines():
            if cnt % 2 != 0:
                evenNumberedLines.append(line)
            cnt += 1
        return evenNumberedLines


def read_file_in_reverse(file_name: str) -> list:
    with open(file_name, mode="r") as file:
        fileContent = []
        for l in file.readlines():
            fileContent.append(l)
        fileContent.reverse()
        print(fileContent)
        return fileContent


def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))


if __name__ == "__main__":
    main()
