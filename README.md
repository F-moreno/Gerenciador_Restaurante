# Gerenciador_Restaurante
Sistema Gerenciador para Restaurante

## Resumo:
Este projeto visa desenvolver um sistema abrangente para a gestão de um restaurante, abordando desde o atendimento ao cliente até a administração interna. A implementação de classes de herança, como Pessoa, Funcionário, Cliente e Dependentes, proporcionará uma estrutura robusta para o gerenciamento eficiente do restaurante.

## Palavras-chave:
Restaurante, Gestão, Sistema, Classes de Herança, Pessoa, Funcionário, Cliente, Dependentes.

## Justificativa:
A automação dos processos em restaurantes é crucial para otimizar a eficiência operacional, melhorar a experiência do cliente e facilitar a gestão interna. Este projeto aborda a necessidade de um sistema integrado que abranja todas as áreas do restaurante, proporcionando maior controle e organização.

## Objetivos 

### Objetivos Gerais:
Desenvolver um sistema completo de gestão para restaurantes, integrando funções de atendimento e administração.

### Objetivos Específicos:

Implementar classes de herança para representar entidades como Pessoa, Funcionário, Cliente e Dependentes.
Desenvolver um módulo de atendimento ao cliente que inclua pedidos e reservas.
Criar funcionalidades administrativas para gerenciamento de funcionários, estoque e finanças.
Realizar levantamento de requisitos para identificar necessidades específicas do restaurante.
Realizar modelagem do sistema para definir a estrutura das classes e a interação entre os módulos.
Implementar o sistema de acordo com os requisitos e a modelagem estabelecidos.
Validar o sistema por meio de testes abrangentes, garantindo sua eficácia e confiabilidade.

## Metodologia:

### Levantamento de Requisitos:

Identificar as necessidades do restaurante em termos de atendimento, administração e controle operacional.

```Pessoa```: Existe a necessidade da criação de uma classe generica para armazenar os dados pessoais dos clientes,funcionarios e dependentes. Com a finalidade de economia e reaproveitamento de código.

```Dependente```: O sistema deve possuir um controle para dependentes, esta informação pode ser útil ao decorrer da vida útil do sistema, informações pertinentes a recursos humanos devem ser armazenadas. cada dependente será associado a apenas um unico funcionário, entretanto um funcionario deve poder possuir diversos dependentes. Cada dependente tambem deve armazenar o tipo de parentesco.

```Funcionario```: Existe a necessidade da criação de uma classe para armazenar dados genericos pertinentes a todos os funcionarios independente dos cargos, para evitar uma repetição de código e facilitar futuras manutenções.

```Recepcionista```: Esta classe deve possuir metodos para criar e verificar reservas e abrir ,fechar e ocupar mesas.

```Cozinheiro```: Esta classe deve ser responsavel por finalizar comandas e associar seu id a elas.

```Garcon```: Esta classe é responsavel por abrir as comandas associando seu id a elas.

```Cliente```: No momento o cliente nao interage com o sistema, assim sendo esta classe deve somente armazer o id e definir pessoas como clientes para utilização das outras classes.

```Reserva```: Esta classe representa as reservas contendo data e referencia de mesa e cliente associado.

```Mesa```: Essa classe represeta o objeto responsavel por indicar o consumo total da mesa, e ao ser finalizada deve invocar a classe Venda para finalizar o consumo. deve tambem permitir que o garçom insira comandas a ela.



### Modelagem:

Utilizar diagramas UML para modelar a estrutura das classes, suas relações e os fluxos de processos no sistema.
Definir os atributos e métodos essenciais para cada classe, levando em consideração a hierarquia de herança.
```Pessoa```:
>Atributos:
> - identificador
> - identificador do funcionário associado

### Implementação:

Desenvolver o sistema conforme as especificações definidas durante o levantamento de requisitos e a modelagem.
Utilizar boas práticas de programação para garantir a qualidade do código.

### Validação:

Realizar testes unitários e de integração para validar o funcionamento de cada módulo.

Ao implementar este projeto, espera-se fornecer ao restaurante uma solução eficaz para gerenciamento e aprimoramento de suas operações, resultando em uma experiência aprimorada tanto para os clientes quanto para a equipe interna.

## Estrutura do Projeto
~~~
|-- GERENCIADOR_RESTAURANTE/
    |-- modulos
        |-- classes.py
        |-- funcoes.py
    |-- .gitignore
    |-- Diagrama_de_Classes.drawio
    |-- LICENSE
    |-- main.py
    |-- README.md
~~~


## Contribuições
Sinta-se à vontade para propor melhorias, adicionar novos tópicos ou esclarecer dúvidas. Abra uma ```issue``` ou envie um ```comentário```.

Esperamos que este projeto seja útil para o seu aprendizado em Python. Boa jornada de estudos! 

