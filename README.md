### Tratamento de erros e exceções

O tratamento de erros e exceções em Python é uma técnica fundamental para lidar com situações inesperadas ou problemas durante a execução de um programa. Ao utilizar o tratamento de erros, o desenvolvedor pode garantir que o código continue funcionando mesmo quando ocorrem falhas, evitando que o programa quebre abruptamente e fornecendo feedback adequado ao usuário. Dessa forma, é possível criar aplicações mais robustas e resilientes, que conseguem lidar com diferentes cenários de erro de maneira controlada e amigável para o usuário. O tratamento de erros é realizado por meio do uso de blocos **try**, **except**, **else** e **finally**, que permitem capturar e tratar exceções específicas, além de executar ações complementares, como limpeza de recursos, independentemente de ocorrerem erros ou não. Essa abordagem torna o código mais seguro e confiável, tornando-se uma prática essencial para programadores Python em todas as etapas do desenvolvimento de software.



#### Script do arquivo trat1.py:

A interpretação do bloco try é a seguinte: "Tente fazer isso para mim, tente ler e dividir. Tentei executar os três comandos do bloco de código try e deu problema. Passamos para o bloco de código except, onde aplicamos a função print('Infelizmente tivemos um problema'). Agora, se não der problema, se tudo der certo, aplicamos a condicional else e imprimimos o resultado (f' O resultado é {r}'). As instruções do bloco finally serão executadas, tenha havido erro ou não, ou seja, independentemente se deu certo ou não. Lembrando que os comandos else e finally são opcionais em tratativas de erros e exceções.

Em frente ao comando except, podemos tratar o erro e inserir o que aconteceu. Primeiro, digitamos a palavra "Exception" com "E" maiúsculo mesmo, e em seguida o erro. Agora temos uma variável na qual posso mostrar no print do bloco except a formatação, registrando assim no print(f' O problema encontrado foi {erro.}').

Após esse erro. vamos inserir a classe, o contexto, a causa que o próprio Python sugere. Nesse caso, foi inserido a "classe". Ao executarmos o programa acima e der erro, o terminal do PyCharm vai nos dizer qual foi o erro e qual foi a classe do erro, como por exemplo: "O problema encontrado foi <class 'ValueError'>". Se tentarmos dividir 10/0, o terminal vai disparar: "O problema encontrado foi <class 'ZeroDivisionError'>".

Claro que as classes dos erros não devem ser mostradas ao usuário, contudo como desenvolvedores podemos capturar qual é o erro e criar uma mensagem simples e objetiva para mostrar para o nosso usuário. Lembre-se de que um try pode conter vários excepts, e cada except terá seu próprio bloco e sua própria mensagem, seu próprio tratamento, inclusive no arquivo **trat2.py** será abordado um código comtemplando esses comandos. 



#### Script do arquivo trat2.py:


Primeiro, o programa solicita ao usuário que insira um valor para o numerador e outro para o denominador.
Em seguida, ele tenta converter os valores digitados para números inteiros (int) e realiza a operação de divisão (a/b) para obter o resultado (r).

Caso ocorra uma exceção do tipo ValueError ou TypeError durante a conversão dos valores, o bloco de código no primeiro "except" será executado, e uma mensagem informando que houve um problema com os tipos de dados digitados será exibida.

Se ocorrer uma exceção do tipo ZeroDivisionError, o bloco de código no segundo "except" será executado, e uma mensagem informando que não é possível dividir um número por zero será exibida.
Se o usuário pressionar a combinação de teclas "Ctrl+C" durante a execução do programa (interrupção de teclado), o bloco de código no terceiro "except" será executado, e uma mensagem informando que o usuário preferiu não informar seus dados será exibida.

Se a operação de divisão for bem-sucedida, o bloco de código no "else" será executado, e o programa exibirá o resultado da divisão (f'O resultado é {r}').
Finalmente, independentemente se houve ou não exceções, o bloco de código no "finally" será executado, e uma mensagem de agradecimento será exibida, seguida de "Agradeço e volte sempre!!!".
O uso do bloco "try-except" é uma forma de tratar possíveis erros ou exceções durante a execução do programa, garantindo que ele continue funcionando mesmo quando ocorram situações inesperadas.


Por fim, o tratamento de erros e exceções é uma prática importante para garantir que o programa seja robusto e forneça feedback adequado aos usuários quando ocorrerem problemas.


