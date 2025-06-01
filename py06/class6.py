from typing import Union, Optional

def greet(name: Optional[str] = None) -> str:
    if name == None:
        return "Hello Guest"
    else:
        return f"Hello, {name}"

age: Union[int, str] = "Twenty"

print(greet())
print(greet("Osama"))

names: list[str] = ["Alice", "Bob", "Charlie"]
ages: list[int] = [25, 35, 30]

zipped = zip(names, ages)

for name, age in zipped:
    print(f"{name} is {age} year old.")