from dice.repository.dice_repository import DiceRepository


class DiceRepositoryImpl(DiceRepository):

    __instance=None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance=super.__new__(cls)
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance=cls()
        return cls.__instance

    def rollDice(self):
        pass
