from validate_docbr import CPF

cpf = CPF()

print(cpf.generate(True))
print(cpf.generate(False))

print(cpf.validate("239.144.568-76"))
print(cpf.validate("56235437820"))
print(cpf.validate("56235473820"))

CPFs = [
    "239.144.568-76"
    "56235437820"
]

print(cpf.validate_list(CPFs))
