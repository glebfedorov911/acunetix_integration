from abc import ABC, abstractmethod


class Body(ABC):


    @abstractmethod
    def body(self) -> dict: ...

class Api(ABC):


    @abstractmethod
    def do(self) -> dict: ...