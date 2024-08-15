
class ValidarDadosGeneric(ExceptionGroup):
    """
    Exceção para dados inválidos.

    Attributes:
        message (str):
        A mensagem de erro a ser exibida quando a exceção é levantada.

    Args:
        message (str):
        A mensagem de erro para descrever as exceções agrupadas.

    Methods:
        __init__(self, message):
        Inicializa a exceção com a mensagem de erro fornecida.
    """
    def __init__(self, message) -> None:
        super().__init__(message)
