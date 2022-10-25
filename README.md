# A Canção de Vecna
  Para deter o vilão Vecna, de Stranger Things, Eleven e seus amigos encarregam a turma 5M1 de Estrutura de Dados III, do quinto semestre do curso de Ciência da Computação do IFSul, da importante tarefa de adentrar a dimensão upside-down e reproduzir as músicas favoritas de todos da equipe simultaneamente, o que enfraqueceria o vilão. Ao chegar no mundo invertido, a equipe descobre que as músicas estão embaralhadas, o que torna a sua reprodução em um grave perigo devido à irreconhecível distorção melódica na qual foram transformadas.

  As músicas foram embaralhadas de forma a conter treze arquivos, cada um contendo uma música correta escondida entre outras falsas e com as suas linhas misturadas entre si. O presente projeto foi encarregado de decifrar o arquivo da música de número três, denominado “songs3”. O problema apresentado, portanto, é da natureza de ordenação. Para solucioná-lo, deve-se ordenar cada música (arquivo) e a ordem de cada nota dentro do seu respectivo arquivo. Assim, cada música será tocada individualmente e será possível determinar qual é a correta. Ademais, a atmosfera do mundo invertido demanda a necessidade de uma execução no menor tempo possível, o que culminou na escolha do algoritmo Counting Sort para a ordenação.