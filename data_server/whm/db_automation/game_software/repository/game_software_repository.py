from abc import ABC, abstractmethod


class GameSoftwareRepository(ABC):

    @abstractmethod
    def list(self, page, perPage):
        pass

    @abstractmethod
    def findAll(self):
        pass

    @abstractmethod
    def create(self, title):
        pass

    @abstractmethod
    def findById(self, id):
        pass