
from agente_ucv.agent import explicar_concepto


def test_explicar_sistema_inteligente():
    resultado = explicar_concepto("sistema inteligente")

    assert resultado["status"] == "success"
    assert resultado["concepto"] == "sistema inteligente"
    assert "percibir información" in resultado["explicacion"]


def test_explicar_machine_learning():
    resultado = explicar_concepto("machine learning")

    assert resultado["status"] == "success"
    assert "aprender patrones" in resultado["explicacion"]


def test_concepto_no_registrado():
    resultado = explicar_concepto("robotica")

    assert resultado["status"] == "not_found"
    assert resultado["concepto"] == "robotica"


def test_normalizar_concepto():
    resultado = explicar_concepto("  MINIMAX  ")

    assert resultado["status"] == "success"
    assert resultado["concepto"] == "minimax"
