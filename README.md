
# Calculadora Simples com Interface Gráfica
**Projeto**: Calculadora
**Grupo**: Bryann Lucas Locatelli e Carlos Magno

---

##  Requisitos Funcionais

**Nome do projeto:** Calculadora Simples com Interface Gráfica  
**Objetivo:** Permitir ao usuário realizar operações matemáticas básicas (adição, subtração, multiplicação, divisão).  

###  Funcionalidades
- Interface gráfica com botões numerais e operadores.
- Suporte a ponto decimal.
- Cálculo de expressões com botão "=".
- Limpar entrada com "C".
- Validação de divisão por zero.

###  Tecnologias utilizadas
- Python 3
- Tkinter para GUI

###  Requisitos não-funcionais
- Aplicação deve ser responsiva e intuitiva.
- Deve exibir mensagens de erro em caso de entrada inválida.

---

##  Plano de Testes

| Caso de Teste       | Entrada | Saída Esperada | Resultado |
|---------------------|---------|----------------|-----------|
| Soma simples        | `2+3`   | `5`            |   ok      |
| Divisão por zero    | `10/0`  | `Erro`         |   ok      |
| Limpar entrada      | `C`     | Campo limpo    |   ok      |

---

##  Fluxograma (texto)

```
[Início]
   |
   v
[Usuário clica no botão]
   |
   v
[Verifica se é "C"]
   |--- Sim ---> [Limpa entrada] ---> [Fim]
   |--- Não ---->|
                 v
        [Verifica se é "="]
           |--- Sim ---> [Avalia expressão]
           |               |--- Erro? ---> [Exibe "Erro"]
           |               |--- Não -----> [Exibe resultado]
           |--- Não ----> [Adiciona valor na entrada]
                 |
                 v
                [Fim]
```
