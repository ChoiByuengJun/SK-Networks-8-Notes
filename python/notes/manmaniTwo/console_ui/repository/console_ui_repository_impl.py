from console_ui.entity.console_ui_message_state import ConsoleUiMessageState
from console_ui.handler.main_handler import MainHandler
from console_ui.handler.register_handler import RegisterHandler
from console_ui.repository.console_ui_repository import ConsoleUiRepository


class ConsoleUiRepositoryImpl(ConsoleUiRepository):
    __instance = None
    __messageTable = {}
    __handlerTable = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__handlerTable[ConsoleUiMessageState.MAIN.value] = MainHandler.processUserInputOnMain
            cls.__instance.__handlerTable[ConsoleUiMessageState.REGISTER.value] = RegisterHandler.processUserInputOnRegister

            cls.__instance.__messageTable[ConsoleUiMessageState.MAIN.value] = \
                ("일심칠십 게임(MAIN)에 오신 것을 환영합니다.\n"
                 "1번을 누르면 회원 가입이 진행됩니다.\n"
                 "2번을 누르면 로그인을 진행합니다.\n"
                 "3번을 누르면 게임이 종료됩니다.")
            cls.__instance.__messageTable[ConsoleUiMessageState.REGISTER.value] = \
                ("회원 가입을 진행 합니다.")
            cls.__instance.__messageTable[ConsoleUiMessageState.LOBBY.value] = \
                ("일삼칠십 게임 LOBBY에 진입하셨습니다.\n"
                 "1번을 누르면 게임이 시작됩니다.\n"
                 "2번을 누르면 전적을 확인 할 수 있습니다.\n"
                 "3번을 누르면 게임이 MAIN으로 돌아갑니다.")

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def printMessage(self, state):
        print(f"{self.__messageTable[state]}")

    def processUserInput(self, state):
        handlerFunction = self.__handlerTable[state]
        return handlerFunction()
