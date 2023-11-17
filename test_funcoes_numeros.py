from funcoes_numeros import eh_impar

def test_eh_impar_se_o_numero_for_impar_retorna_true():
  assert eh_impar(3) is True
  
def test_eh_impar_se_o_numero_for_par_retorna_false():
  assert eh_impar(2) is False