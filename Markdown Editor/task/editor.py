def get_list():
    while True:
        try:
            number_of_rows = int(input("Number of rows: "))
            assert number_of_rows > 0
        except (ValueError, AssertionError):
            print("The number of rows should be greater than zero")
            continue
        break
    return [input(f'Row #{num + 1}: ') for num in range(number_of_rows)]


class MdBuilder():
    def create_header():
        while True:
            try:
                level = int(input("Level: "))
                assert 1 <= level <= 6
            except (ValueError, AssertionError):
                print("The level should be within the range of 1 to 6")
                continue
            break
        return f'{"#" * level} {input("Text: ")}\n'


    def create_list():
        return "".join([f'{i}. {item}\n' for i, item in enumerate(get_list(), 1)])

    def create_unordered_list():
        return "".join([f'* {item}\n' for item in get_list()])

    md_text: str = ""
    formatters = {
        "plain": lambda: input("Text: "),
        "bold": lambda: f'**{input("Text: ")}**',
        "italic": lambda: f'*{input("Text: ")}*',
        "header": create_header,
        "link": lambda: f'[{input("Label: ")}]({input("URL: ")})',
        "inline-code": lambda: f'`{input("Text: ")}`',
        "new-line": lambda: "\n",
        "ordered-list": create_list,
        "unordered-list": create_unordered_list,
    }

    def main(self):
        while (formatter := input("Choose a formatter: ")) != "!done":
            if formatter == "!help":
                print("Available formatters: ", *self.formatters, "\nSpecial commands: !help !done")
            elif formatter in self.formatters:
                self.md_text += self.formatters[formatter]()
                print(self.md_text)
            else:
                print("Unknown formatting type or command")
        file = open('output.md', 'w', encoding='utf-8')
        file.write(self.md_text)
        file.close()


my_builder = MdBuilder()
my_builder.main()
