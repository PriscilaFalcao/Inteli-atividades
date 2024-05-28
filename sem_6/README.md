# Ponderada

Crie um repositório no github chamado aplicando-testes e siga o passo a passo dos testes explicados no tutorial do autoestudo. Cada teste deverá estar versionado no github.

- Deverá haver um commit para cada teste implementado.

- O seu repositório deverá ter no arquivo readme uma seção para cada tipo de testes. Nessa seção, você irá detalhar de forma clara objetiva a aplicação do testes e fornecer dois cenários de exemplo.

- Na seção de cada teste, após as descrições, coloque um print do teste sendo executado.

- Lembre-se de seguir rigorosamente os itens do exercício e do tutorial.

Faça o exercício com capricho e dedicação.


# Teste de unidade

Essa abordagem consiste em testes automatizados que verificam o comportamento isolado de pequenas partes do código, conhecidas como unidades, geralmente métodos ou funções.

Para a aplicação desse tipo de teste, foi escolhido a solução xUnit. A xUnit é uma família de frameworks de teste de unidade, que permitem aos desenvolvedores criar e executar testes automatizados para verificar o comportamento correto de suas aplicações. 

O código do projeto era:

```
using System;

namespace Temperatura
{
    public static class ConversorTemperatura
    {
        public static double FahrenheitParaCelsius(double temperatura)
            //=> (temperatura - 32) / 1.8; // Simulação de falha
            => Math.Round((temperatura - 32) / 1.8, 2);
    }
}
```

Já o código do teste era similar a esse:

```
using System;
using Xunit;

namespace Temperatura.Testes
{
    public class TestesConversorTemperatura
    {
        [Theory]
        [InlineData(32, 0)]
        [InlineData(47, 8.33)]
        [InlineData(86, 30)]
        [InlineData(90.5, 32.5)]
        [InlineData(120.18, 48.99)]
        [InlineData(212, 100)]
        public void TestarConversaoTemperatura(
            double fahrenheit, double celsius)
        {
            double valorCalculado =
                ConversorTemperatura.FahrenheitParaCelsius(fahrenheit);
            Assert.Equal(celsius, valorCalculado);
        }
    }
}
```

Os resultados do teste foi conforme a imagem abaixo:

<img src='../assets/img1.png'>

# Mock Objects

Mocks permitem simular o comportamento de objetos em diferentes cenários, evitando que desenvolvedores criem implementações que certamente seriam descartadas/desativadas num ambiente de produção.

Para a aplicação deste teste foi usado a ferramenta Moq. A Moq é uma ferramenta de mocking muito popular, especialmente no ecossistema .NET. O mocking é uma técnica utilizada em testes de unidade para substituir dependências reais por objetos simulados (mocks) que permitem controlar e verificar o comportamento dessas dependências.

O código do projeto a ser testado era similar a esse:

```
﻿namespace ConsultaCredito
{
    public class AnaliseCredito
    {
        private readonly IServicoConsultaCredito _servConsultaCredito;

        public AnaliseCredito(IServicoConsultaCredito servConsultaCredito)
        {
            _servConsultaCredito = servConsultaCredito;
        }

        public StatusConsultaCredito ConsultarSituacaoCPF(string cpf)
        {
            try
            {
                var pendencias =
                    _servConsultaCredito.ConsultarPendenciasPorCPF(cpf);

                if (pendencias == null)
                    return StatusConsultaCredito.ParametroEnvioInvalido;
                else if (pendencias.Count == 0)
                    return StatusConsultaCredito.SemPendencias;
                else
                    return StatusConsultaCredito.Inadimplente;
            }
            catch
            {
                return StatusConsultaCredito.ErroComunicacao;
            }
        }
    }
}

```

Já o código do teste era similar a esse:

```
using System;
using System.Collections.Generic;
using Xunit;
using Moq;
using FluentAssertions;

namespace ConsultaCredito.Testes
{
    public class TestesAnaliseCredito
    {
        private readonly Mock<IServicoConsultaCredito> mock;

        private const string CPF_INVALIDO = "123A";
        private const string CPF_ERRO_COMUNICACAO = "76217486300";
        private const string CPF_SEM_PENDENCIAS = "60487583752";
        private const string CPF_INADIMPLENTE = "82226651209";

        public TestesAnaliseCredito()
        {
            mock = new (MockBehavior.Strict);

            mock.Setup(s => s.ConsultarPendenciasPorCPF(CPF_INVALIDO))
                .Returns(() => null);

            mock.Setup(s => s.ConsultarPendenciasPorCPF(CPF_ERRO_COMUNICACAO))
                .Throws(new ("Testando erro de comunicação"));

            mock.Setup(s => s.ConsultarPendenciasPorCPF(CPF_SEM_PENDENCIAS))
                .Returns(() => new List<Pendencia>());

            Pendencia pendencia = new ()
            {
                CPF = CPF_INADIMPLENTE,
                NomePessoa = "Cliente Teste",
                NomeReclamante = "Empresas ACME",
                DescricaoPendencia = "Parcela não paga",
                VlPendencia = 900.50
            };
            List<Pendencia> pendencias = new ();
            pendencias.Add(pendencia);

            mock.Setup(s => s.ConsultarPendenciasPorCPF(CPF_INADIMPLENTE))
                .Returns(() => pendencias);
        }

        private StatusConsultaCredito ObterStatusAnaliseCredito(string cpf)
        {
            AnaliseCredito analise = new (mock.Object);
            return analise.ConsultarSituacaoCPF(cpf);
        }

        [Fact]
        public void TestarCPFInvalidoMoq()
        {
            StatusConsultaCredito status =
                ObterStatusAnaliseCredito(CPF_INVALIDO);
            status.Should().Be(StatusConsultaCredito.ParametroEnvioInvalido,
                "Resultado incorreto para um CPF inválido");
        }

        [Fact]
        public void TestarErroComunicacaoMoq()
        {
            StatusConsultaCredito status =
                ObterStatusAnaliseCredito(CPF_ERRO_COMUNICACAO);
            status.Should().Be(StatusConsultaCredito.ErroComunicacao,
                "Resultado incorreto para um erro de comunicação");
        }

        [Fact]
        public void TestarCPFSemPendenciasMoq()
        {
            StatusConsultaCredito status =
                ObterStatusAnaliseCredito(CPF_SEM_PENDENCIAS);
            status.Should().Be(StatusConsultaCredito.SemPendencias,
                "Resultado incorreto para um CPF sem pendências");
        }

        [Fact]
        public void TestarCPFInadimplenteMoq()
        {
            StatusConsultaCredito status =
                ObterStatusAnaliseCredito(CPF_INADIMPLENTE);
            status.Should().Be(StatusConsultaCredito.Inadimplente,
                "Resultado incorreto para um CPF inadimplente");
        }
    }
}
```

Os resultados do teste foi conforme a imagem abaixo:

<img src='../assets/img2.png'>


# SpecFlow

O SpecFlow é uma alternativa open source muito útil quando optamos por abordagens como BDD (Behavior Driven Development), possibilitando a execução de testes de validação de funcionalidades de um projeto através de user stories.

Utilizando a sintaxe Gherkin ("Dado", "Quando", "Então"), o SpecFlow mapeia as especificações em testes automatizados, criando uma ligação clara entre os requisitos de negócio e a implementação técnica.

O código do projeto a ser testado era similar a esse:

```
using System;

namespace APIFinancas
{
    public static class CalculoFinanceiro
    {
        public static double CalcularValorComJurosCompostos(
            double valorEmprestimo, int numMeses, double percTaxa)
        {
            return valorEmprestimo * Math.Pow(1 + (percTaxa / 100), numMeses); // Simulação de falha 
            //return Math.Round(
            //    valorEmprestimo * Math.Pow(1 + (percTaxa / 100), numMeses), 2);
        }
    }
}
```

Já o código do teste era similar a esse:

```
Funcionalidade: Cálculo de Juros Compostos

Cenário: SimulacaoJurosCompostos01
	Dado que o valor o valor do empréstimo é de R$ 10.000,00
	E que este empréstimo será por 12 meses
	E que a taxa de juros é de 2,00% ao mês
	Quando eu solicitar o cálculo do valor total a ser pago ao final do período
	Então o resultado será 12.682,42

Cenário: SimulacaoJurosCompostos02
	Dado que o valor o valor do empréstimo é de R$ 11.937,28
	E que este empréstimo será por 24 meses
	E que a taxa de juros é de 4,00% ao mês
	Quando eu solicitar o cálculo do valor total a ser pago ao final do período
	Então o resultado será 30.598,88

Cenário: SimulacaoJurosCompostos03
	Dado que o valor o valor do empréstimo é de R$ 15.000,00
	E que este empréstimo será por 36 meses
	E que a taxa de juros é de 6,00% ao mês
	Quando eu solicitar o cálculo do valor total a ser pago ao final do período
	Então o resultado será 122.208,78

Cenário: SimulacaoJurosCompostos04
	Dado que o valor o valor do empréstimo é de R$ 10.000,00
	E que este empréstimo será por 2 meses
	E que a taxa de juros é de 2,00% ao mês
	Quando eu solicitar o cálculo do valor total a ser pago ao final do período
	Então o resultado será 10.404,00

Cenário: SimulacaoJurosCompostos05
	Dado que o valor o valor do empréstimo é de R$ 20.000,00
	E que este empréstimo será por 36 meses
	E que a taxa de juros é de 6,00% ao mês
	Quando eu solicitar o cálculo do valor total a ser pago ao final do período
	Então o resultado será 162.945,04

Cenário: SimulacaoJurosCompostos06
	Dado que o valor o valor do empréstimo é de R$ 25.000,00
	E que este empréstimo será por 48 meses
	E que a taxa de juros é de 6,00% ao mês
	Quando eu solicitar o cálculo do valor total a ser pago ao final do período
	Então o resultado será 409.846,79

Cenário: SimulacaoJurosCompostos07
	Dado que o valor o valor do empréstimo é de R$ 30.000,00
	E que este empréstimo será por 3 meses
	E que a taxa de juros é de 3,00% ao mês
	Quando eu solicitar o cálculo do valor total a ser pago ao final do período
	Então o resultado será 32.781,81
```

Os resultados do teste foi conforme a imagem abaixo:

<img src='../assets/img3.png'>