from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20, 30))

@dataclass
class Book:
    # You can define default values when attributes are declared
    title: str = "history"
    author: str = "morgen frimen"
    pages: int = 0
    price: float = field(default_factory=price_func)
    
b2 = Book("hello world", "mark menson", 3434)    
b3 = Book("spaider man", "tom haland", 311)    

print(b2)
print(b3)
