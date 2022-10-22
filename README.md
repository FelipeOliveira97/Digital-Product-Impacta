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

## Definição de Done

 - Deploy da aplicação Python através de pipeline CI/CD no github actions, assim como, uma URL válida para a aplicação web após o deploy.
 - Integração com o Telegram para visualização de informações.

## Code/Test

Codificamos uma aplicação em Python utilizando o visual code, que tem como retorno os status das situações das linhas de trem/metros em SP.
tem como seus endpoints:

[https://state-train-sp.herokuapp.com](https://state-train-sp.herokuapp.com/)
   > **Nota:** retorna os status de todas as linhas de trem/metro de sp.
   
https://state-train-sp.herokuapp.com/status/1
> **Nota:** retorna o status correspondente ao código da linha.

Nessa etapa após o desenvolvimento realizamos os testes e validamos o código.

## GitHub Actions 

Nossa pipeline foi estruturada para usar o GithubActions como ferramenta de CI/CD.
![image](https://user-images.githubusercontent.com/52111260/197317604-dbf847f0-5628-4859-8901-e9357814c462.png)

## Docker
Utilizamos um arquivo **Dockerfile** para criação da imagens requeridas.

## Deploy: Heroku

![image](https://user-images.githubusercontent.com/52111260/197317834-8ecf76d4-3c61-4bf5-b8b2-f9a727df14dc.png)

## Desenho de solução
![testeuml drawio](https://user-images.githubusercontent.com/56937166/197299234-6b965406-4ddf-40f5-bd05-301bd12e6826.png)


