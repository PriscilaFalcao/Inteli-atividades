# Ponderada semana 10

Realize o passo a passo do artigo e armazene o seu código em um repositório git. Crie um relatório em markdown com um resumo explicando a tecnologia, os conceitos aprendidos. Adicione prints com o código em execução e dos componentes que foram criados na núvem (instancia de EC2 criada por meio do pipeline).


# Relatório - Automação do Terraform com GitHub Actions

O tutorial "Automate Terraform with GitHub Actions" do HashiCorp Developer explora a integração do Terraform com o GitHub Actions para automatizar o processo de construção, teste e implantação de software.

## Tecnologia

- **Terraform**: É uma ferramenta de infraestrutura como código (IaC) desenvolvida pela HashiCorp. O Terraform permite definir e provisionar recursos de infraestrutura de forma declarativa, utilizando arquivos de configuração.

- **GitHub Actions**: É uma plataforma de automação integrada ao GitHub. Permite criar fluxos de trabalho (workflows) personalizados para automatizar tarefas relacionadas ao desenvolvimento de software, como construção, teste e implantação.

## Conceitos Aprendidos

O tutorial aborda os seguintes conceitos:

1. **Integração do Terraform Cloud com GitHub Actions**: A HashiCorp fornece ações do GitHub Actions que se integram com a API do Terraform Cloud. Essas ações permitem criar fluxos de trabalho personalizados para atender às necessidades da organização.

2. **Criação de um fluxo de trabalho (workflow)**: O tutorial mostra como criar um fluxo de trabalho completo utilizando as ações do GitHub Actions e o Terraform Cloud. Esse fluxo de trabalho é responsável por implantar um servidor web acessível publicamente dentro de um espaço de trabalho do Terraform Cloud.

3. **Configuração de um ambiente de desenvolvimento**: O tutorial orienta na configuração de um ambiente de desenvolvimento que inclui uma conta no GitHub, uma conta no Terraform Cloud e uma conta na AWS.

4. **Configuração do Terraform Cloud**: O tutorial explica como conectar o GitHub Actions ao Terraform Cloud, incluindo a criação de um espaço de trabalho no Terraform Cloud, a configuração das credenciais da AWS e a geração de um token de API do Terraform Cloud.

5. **Configuração de um repositório do GitHub**: O tutorial guia na criação de um novo repositório no GitHub e na configuração de segredos e variáveis de ambiente necessários para o fluxo de trabalho do Terraform.

6. **Revisão dos workflows do Terraform**: O tutorial fornece uma visão geral dos arquivos principais do fluxo de trabalho, incluindo os arquivos `terraform-plan.yml` e `terraform-apply.yml`. Esses arquivos definem as etapas necessárias para executar o planejamento e a aplicação das configurações do Terraform.

7. **Execução dos workflows**: O tutorial orienta como executar os workflows criados, incluindo a execução de um pull request para testar o fluxo de trabalho e a execução de um push para a branch principal para aplicar as configurações do Terraform.

## Conclusão

O tutorial "Automate Terraform with GitHub Actions" mostra como integrar o Terraform ao GitHub Actions para automatizar o processo de infraestrutura como código. Através dessa integração, é possível criar fluxos de trabalho personalizados que seguem as melhores práticas de configuração, promovem a colaboração entre os membros da equipe e automatizam o fluxo de trabalho do Terraform. A combinação do Terraform e do GitHub Actions oferece uma solução poderosa para automatizar a implantação e o gerenciamento de infraestrutura em projetos de desenvolvimento de software.