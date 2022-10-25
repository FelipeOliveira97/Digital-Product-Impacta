<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

<h1 align="center"> Digital-Product-Impacta </h1>
<h2> Colaboradores </h2>
<h4> Felipe Oliveira Cruz </h4>
<h4> Lucas Martins de Queiroz </h4>

## Objetivo
Mesclar a ideia de um projeto pessoal e util para o meu dia-a-dia com ensinamentos aprendidos no mba de cloud & devOps,
facilitar o acesso do usuário a consultar o status dos trens e metros de sp em tempo real via Telegram.

## Tarefas
As tarefas foram separadas em quatro epicos Desenvolvimento, PipeLine DevOps, Integração com Telegram, Documentação.
[Trello](https://trello.com/b/FPNtwsIM/digital-product-impacta)

![image](https://user-images.githubusercontent.com/52111260/197317992-e88579db-598c-4aa1-9b2a-b600a5e6f03b.png)

## Tecnologias Utilizadas
![image](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![image](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
![image](https://img.shields.io/badge/Git-E34F26?style=for-the-badge&logo=git&logoColor=white)
![image](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![image](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![image](https://img.shields.io/badge/Trello-0052CC?style=for-the-badge&logo=trello&logoColor=white)
![image](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![image](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)

## Definição de Done

 - Deploy da aplicação Python através de pipeline CI/CD no github actions, assim como, uma URL válida para a aplicação web após o deploy.
 - Integração com o Telegram para visualização de informações.

## Code/Test

Codificamos uma aplicação em Python [app.py](https://github.com/FelipeOliveira97/Digital-Product-Impacta/blob/main/app.py) utilizando o visual code, que tem como retorno os status das situações das linhas de trem/metros em SP.
tem como seus endpoints:

[https://state-train-sp.herokuapp.com](https://state-train-sp.herokuapp.com/)
   > **Nota:** retorna os status de todas as linhas de trem/metro de sp.
   
https://state-train-sp.herokuapp.com/status/1
   > **Nota:** retorna o status correspondente ao código da linha.

Nessa etapa após o desenvolvimento realizamos os testes [test.py](https://github.com/FelipeOliveira97/Digital-Product-Impacta/blob/main/test.py) e validamos o código.

## GitHub Actions 

Nossa [pipeline.yml](https://github.com/FelipeOliveira97/Digital-Product-Impacta/blob/main/.github/workflows/pipeline.yml) foi estruturada para usar o GithubActions como ferramenta de CI/CD.
![image](https://user-images.githubusercontent.com/52111260/197317604-dbf847f0-5628-4859-8901-e9357814c462.png)

## Docker
Utilizamos um arquivo [Dockerfile](https://github.com/FelipeOliveira97/Digital-Product-Impacta/blob/main/Dockerfile) para criação da conteinerização dos itens requiridos [requirements.txt](https://github.com/FelipeOliveira97/Digital-Product-Impacta/blob/main/requirements.txt).

## Deploy: Heroku

![image](https://user-images.githubusercontent.com/52111260/197317834-8ecf76d4-3c61-4bf5-b8b2-f9a727df14dc.png)

## Desenho de solução
![testeuml drawio](https://user-images.githubusercontent.com/56937166/197299234-6b965406-4ddf-40f5-bd05-301bd12e6826.png)

## Apresentação da funcionalidade
Foi utilizado o builder da [Take Blip](https://www.take.net/) Para o desenvolvimento do contato inteligente.
> **Nota:** Framework para desenvolvimento de contatos inteligentes.
> 
Caso tenha interesse em testar o contato inteligente no telegram [Thomas](http://t.me/thomasassistentebot)
  
![](https://cdn.discordapp.com/attachments/1026888485799473172/1034260230688755742/2022-10-24_21-02-07_720.gif)
