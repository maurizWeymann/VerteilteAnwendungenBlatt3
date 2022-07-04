from dataclasses import dataclass
from unicodedata import name
# from dataclasses_json import dataclass_json

filename = 'user.json'


# @dataclass_json
@dataclass
class User:
    """Class for keeping track of an user in users."""

    name: str = ''
    password: str = ''
    highscore: int = 0

    def return_name(self) -> str:
        return self.name
    def return_password(self) -> int:
        return self.password
    def return_highscore(self) -> int:
        return self.highscore




