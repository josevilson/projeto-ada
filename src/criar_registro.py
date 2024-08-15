from datetime import datetime
from typing import Dict, Union



def entradas_novo_registro() -> Dict[str, Union[str, float, datetime]]:

    data = solicitar_input('data')

    tipo_movimentacao = solicitar_input('entrada')

if __name__ == '__main__':
    entradas_novo_registro()
