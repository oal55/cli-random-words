from typing import Any, Dict, List
from dataclasses import dataclass
import requests
from .creds import AUTH_HEADERS


@dataclass
class Definition:
    definition: str
    partOfSpeech: str
    examples: List[str]

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Definition":
        return Definition(
            definition=d["definition"],
            partOfSpeech=d["partOfSpeech"],
            examples=d.get("examples", []))


@dataclass
class Word:
    word: str
    definitions: List[Definition]

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Word":
        return Word(
            word=d["word"],
            definitions=[Definition.from_dict(definition) for definition in d["results"]])


class WordsClient:

    def __init__(self) -> None:
        self.base_url = "https://wordsapiv1.p.rapidapi.com/words/"
        self.session = requests.session()
        self.session.headers.update(AUTH_HEADERS)

    def get_random_word(self, min_freq: float, max_freq: float) -> "Word":
        response = self.session.get(self.base_url, params={
            "random": "true",
            "frequencymin": str(min_freq),
            "frequencymax": str(max_freq),
            "hasDetails": "examples",
        }).json()
        return Word.from_dict(response)
