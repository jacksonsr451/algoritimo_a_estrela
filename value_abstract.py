from abc import ABC, abstractmethod


class ValueAbstract(ABC):
    def __init__(self, name: str, value_weight: int, value_back: int, value_end: int):
        self.name: str = name
        self.value_weight: int = value_weight
        self.value_back: int = value_back
        self.value_end: int = value_end

    @abstractmethod
    def get_value_weight(self) -> int:
        return self.value_weight

    @abstractmethod
    def get_value_back(self) -> int:
        return self.value_back

    @abstractmethod
    def get_value_end(self):
        return self.value_end

    @abstractmethod
    def get_name(self) -> str:
        return self.name

    @abstractmethod
    def __str__(self):
        return f'nome: {self.name} -> peso: {self.value_weight} -> peso: {self.value_weight} -> fim: {self.value_end}'
