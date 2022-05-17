def notas(*n, sit=False):
    r= dict()
    total= len(n)
    r['total']= total
    media= sum(n)/total
    maior= max(n)
    menor= min(n)
    r['maior']= maior
    r['menor']= menor
    r['média']= media
    if sit:
        if r['média'] >= 7:
            r['situação']= 'BOA'
        elif r['média'] >= 5:
            r['situação']= 'RAZOÁVEL'
        else:
            r['situação']= 'RUIM'
    return r

resp = notas(8.4,7.5,9.5,8.6, sit=True)

print('~'*20)
for k,v in resp.items():
    print(f'{k}: {v}')
print('~'*20)
