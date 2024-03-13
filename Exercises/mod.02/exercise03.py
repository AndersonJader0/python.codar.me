valor_de_compra = 10.5
valor_do_frete = 2.5
cliente_fidelidade = "s"

pode_usar_cupom = valor_de_compra + valor_do_frete > 100 or cliente_fidelidade == "s"

print(pode_usar_cupom)