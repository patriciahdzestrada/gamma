from ETL import funcion

def test_function():
    resultado = funcion()
    assert resultado == 89, (
        f"Se esperaba 89, pero se obtuvo {resultado}."
    )