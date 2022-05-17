tupla=('palavra', 'letra', 'cinema', 'bataman', 'angola', 'kuduairo', 'felas', 'toguro', 'aipon')
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for l in palavra:
        if l.lower() in 'aeiou':
            print(l, end=' ')