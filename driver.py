from typing import List

from httpclients import Definition, WordsClient


def print_definitions(definitions: List[Definition]) -> None:
    def definition_line(index: int, definition: Definition) -> str:
        return f"{index + 1}. ({definition.partOfSpeech}) {definition.definition}"

    lines: List[str] = []
    for index, definition in enumerate(definitions):
        lines.append(f"    {definition_line(index, definition)}")
    definition = definitions[0]

    return print("\n".join(lines))


client = WordsClient()

while True:
    word = client.get_random_word(2, 3)
    print(f"Word: {word.word}")
    input()
    print_definitions(word.definitions)
    input()
