def reverse(phrase):
    return ' '.join(list(map(lambda x: x[::-1], phrase.split())))

print("Escriba una palabra:")
nombre = input()
print(reverse(nombre))