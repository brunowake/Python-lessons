conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto2.union(conjunto)
# unicao soma todos os conteudos de conjunto 1 e 2
print('unicao {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
#intersecção junta somente o que tem igual entre conjunto 1 e 2
print('intersecção {}'.format(conjunto_interseccao))
#a diferença entre os conjuntos, elimina o que tem igual entre eles antes de imprimir
conjunto_diferenca = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print("diferença conjunto para conjunto2 {}".format(conjunto_diferenca))
print("diferença conjunto2 para conjunto {}".format(conjunto_diferenca2))
#junta conjunto 1 e 2 porém elimina o que há de igual entre eles
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('diferença simetrica entre conjunto 1 e 2 {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
#subset é um conjunto inteiro que está presente em outro conjunto
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('a é um subconjunto de b: {}'.format(conjunto_subset))
#uperset é o conjunto que comtém um subset de outro conjunto
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('b é um super conjunto de a: {}'.format(conjunto_superset))
# tirando duplicidade de lista transformando em conjunto
lista = ['cachorro', 'cachorro','gato','gato','lesma','lesma']
print('lista com duplicidade {}'.format(lista))
conjunto_animais = set(lista)
lista = list(conjunto_animais)
print('lista sem duplicidade após sem convertida em conjunto {}'.format(lista))

# conjunto = {1, 2, 3, 4, 4, 2}
# conjunto.add(5)
# conjunto.discard(3)
# print(conjunto)