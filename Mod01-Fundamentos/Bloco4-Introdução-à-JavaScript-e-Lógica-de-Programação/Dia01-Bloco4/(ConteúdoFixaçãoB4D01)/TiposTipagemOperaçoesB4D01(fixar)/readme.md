# Exercícios

###### Agora que você já conhece os operadores aritméticos básicos do JavaScript, vamos praticá-los? Você pode consultar a lista de operadores na tabela JavaScript Arithmetic Operators disponível <a href="https://www.w3schools.com/js/js_operators.asp" target="_blank">nesse link</a> se tiver dúvidas. Vamos fazer algumas operações simples para encontrarmos a área e o perímetro de um retângulo de base 5 e altura 8.

##### 1 - Crie uma costante chamada base e uma variável chamada height e atribua os seus respectivos valores: 5 e 8.
```
const base = 5;
let height = 8;
```
##### 2 - Crie uma constante chamada area e atribua a ela o resultado da multiplicação da base pela altura. Dica: lembre-se de usar sempre o console.log() para imprimir as variáveis e checar os resultados das operações!
```
const area = base * height;
console.log(area)
```
##### 3 - Crie uma constante chamada perimeter e atribua a ela a soma de todos os lados do retângulo.
```
const perimeter = (2 * base) + (2 * height);
console.log(perimeter)
```