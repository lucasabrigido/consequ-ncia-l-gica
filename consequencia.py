atomicas = ['c', 'g', 'm']
formula = [[['c'], ['&'], [['~'], ['g']]], ['=>'], ['m']]


def qtdAtom(A):
    if (len(A) == 1):
        return 1
    if (len(A)==3):
        return qtdAtom(A[0]) + qtdAtom(A[2])
    if (len(A)==2):
        return qtdAtom(A[1])

def atom(A):
    if (len(A) == 1):
        return [A[0]]
    if (len(A)==3):
        return atom(A[0]) + atom(A[2])
    if (len(A)==2):
        return atom(A[1])

def valoracao(form, interpretacao):
    if (len(form) == 1):
        return interpretacao[form[0]]
    if (len(form)==3):
        if (form[1]==['||']):
            return valoracao(form[0],interpretacao) or valoracao(form[2],interpretacao)
        if (form[1] == ['&']):
            return valoracao(form[0],interpretacao) and valoracao(form[2],interpretacao)
    if (len(form)==2):
        return not valoracao(form[1],interpretacao)

conectivos = ['&', '~', '||', '=>', '<=>']
premissas = [[[['c'], ['&'], [['~'], ['g']]], ['=>'], ['m']], ['c'], [['~'], ['m']]]
formula = ['q']

def consequencia(premissas, formula):
    atomicas = atom(formula)
    for premissa in premissas:
        atomicas = atomicas + atom(premissa)
    interpretacao = {}
    return tabela_consequencia(premissas, formula, atomicas, interpretacao)

def tabela_consequencia(premissas, formula, atomicas , interpretacao):
    if (len(atomicas)==0):
        if (valoracao(formula, interpretacao)):
            return True
        valor_premissa = True
        for premissa in premissas:
            valor_premissa = valor_premissa and valoracao(premissa, interpretacao)
        if valor_premissa:
            return False
        return True
    atomica = atomicas[0]
    atomicas = atomicas[1:]
    interpretacao1 = {
        atomica: True
    }
    interpretacao1.update(interpretacao)

    interpretacao2 = {
        atomica:False
    }
    interpretacao2.update(interpretacao)
    return tabela_consequencia(premissas, formula, atomicas, interpretacao1) and tabela_consequencia(premissas, formula, atomicas, interpretacao2)

print(consequencia(premissas, formula))