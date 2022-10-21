# Digital-Product-Impacta
## Integrantes: Felipe Oliveira Cruz / Lucas Martins de Queiroz

## Objetivo
Facilitar o acesso do usuário a consultar o status dos trens e metros de sp.

## Tarefas
https://trello.com/b/FPNtwsIM/digital-product-impacta

## Tecnologias Utilizadas 

 -  **Python**
 -   **Heroku**
  -  **Git**
  -  **Docker**
  -  **Github Actions**
   -  **TerraForm**

## Definição de Done

 - Deploy da aplicação Python através de pipeline CI/CD no github actions, assim como, uma URL válida para a aplicação web após o deploy.

## Code/Test

Codificamos uma aplicação em Python utilizando o visual code, que tem como retorno os status das situações das linhas de trem/metros em SP.
tem como seus endpoints:

[https://state-train-sp.herokuapp.com](https://state-train-sp.herokuapp.com/)
   > **Nota:** retorna os status de todas as linhas de trem/metro de sp.
   
https://state-train-sp.herokuapp.com/status/1
> **Nota:** retorna o status correspondente ao código da linha.

Nessa etapa após o desenvolvimento realizamos os testes e validamos o código.

## GitHub Actions 

 nossa pipeline foi estruturada para usar o GithubActions como ferramenta de CI/CD.

## Docker

## Deploy: Heroku
![image](https://user-images.githubusercontent.com/52111260/197298902-8b659e4c-7c15-4971-9518-e319b0d1dd98.png)

## Desenho de solução
https://user-images.githubusercontent.com/56937166/197298150-c826369d-9a40-4a5f-b33f-bb2efd7861c4.png
