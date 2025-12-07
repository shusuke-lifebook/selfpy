import dataclasses


@dataclasses.dataclass(frozen=True)
class Person:
    firstname: str
    lastname: str


if __name__ == "__main__":
    for f in dataclasses.fields(Person):
        print(f)
