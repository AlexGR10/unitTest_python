from typing import List

class ShoppingCart:
    def __init__(self) -> None:
        self.items: list[str] = [] 

    def add_item(self, item: str):
        self.items.append(item)
    
    def size(self) -> int:
        return len(self.items)
    
    def get_items(self) -> list[str]: 
        return self.items.copy()