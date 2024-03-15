notas = [8, 10, 8.5]

notas.append(9)

print(notas)
notas.sort(reverse=True)
print(notas)

x = notas.pop()
print(notas)
print("x", x)

notas.insert(0, 8)
print("após inserção")
print(notas)

notas.pop(0)
print(notas)    