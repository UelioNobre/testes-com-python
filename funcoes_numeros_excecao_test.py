import pytest
from funcoes_numeros import dividir
    
def test_deve_lancar_um_erro_ao_tentar_dividir_por_zero():
  with pytest.raises(ZeroDivisionError, match="division by zero"):
    dividendo = 36
    divisor = 0
    dividir(dividendo, divisor)
    
def test_deve_lancar_um_erro_ao_tentar_dividir_por_zero():
    assert dividir(36, 1) == 36