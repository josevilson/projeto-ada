import json


def salvar_registros(registros, arquivo):
    """Salva os registros financeiros no arquivo JSON."""

    with open(arquivo, 'w') as f:
        json.dump(registros, f, indent=4)
