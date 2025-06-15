# Classes

class Pakistani:
    national_language: str = "Urdu"
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def find_national_language(self) -> str:
        return f"National language is {self.national_language}."
    
# Example usage
pakistani = Pakistani("Ali", 30)
print(pakistani)
print(pakistani.name)
print(pakistani.age)
print(pakistani.greet())
print(pakistani.find_national_language())
print(Pakistani.national_language)

print("---------------------")
print("---------------------")
print("---------------------")

from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class PakistaniDataClass:
    national_language: ClassVar[str] = "Urdu"
    name: str
    age: int
    courses: list | None = field(default_factory=list)

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    @classmethod
    def find_national_language(cls) -> str:
        return f"National language is {cls.national_language}."
    
# Example usage
pakistani_data_class = PakistaniDataClass(name="Ali", age=30)
print(pakistani_data_class)
pakistani_data_class.courses.append("Python")
print(pakistani_data_class)
print(pakistani_data_class.name)
print(pakistani_data_class.age)
print(pakistani_data_class.courses)
print(pakistani_data_class.greet())
print(PakistaniDataClass.find_national_language())
print(PakistaniDataClass.national_language)

print("---------------------")
print("---------------------") 
print("---------------------")

