'''
geradores e iteradores são ''potinhos'' com quantidades limitadas de
itens. quando vc passa por todos eles, seja com um for ou com a função next
eles acabam, simplesmente

um iterável, um tipo de objeto que possibilita a ação de repetição sobre seus elementos, 
como listas e strings.
No Python, um objeto é considerado iterável se ele implementa o método __iter__, 
permitindo, por exemplo, que um loop for seja executado sobre ele.

Um iterador é sempre um iterável, 
mas que produz um valor a cada vez que é usado como argumento da função nativa next().
'''
a = 'python'
a = iter(a)
print(next(a))
