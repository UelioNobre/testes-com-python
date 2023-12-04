valores = {
    "qtd": [
        "um-dois-tes",
        "um-dois-tres-quatro",
        "um-dois-tres-quatro-cinco",
        "u-m-d-o-i-s-t-r-e-s",
        "um",
    ]
}

maior_por_len = max(valores["qtd"], key=len)
maior_por_hifens = max(valores["qtd"], key=lambda hifens: hifens.split("-"))

print(f"Maior pela chave len {maior_por_len}")
print(f"Maior usando funcao lambda {maior_por_hifens}")
