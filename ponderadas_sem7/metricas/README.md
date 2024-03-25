# Atividade ponderada

Realize o passo a passo do artigo e armazene o seu código em um repositório git. Crie um relatório em markdown com um resumo explicando a tecnologia, os conceitos aprendidos.
Adicione prints com o código em execução, contemplando todos os componentes de coleta de métrica (Prometheus, Jaegger, Grafana, etc) em execução. 

Contemple prints com os graficos gerados.

## Introdução

A observabilidade em um sistema distribuído envolve a capacidade de monitorar e analisar a telemetria de cada componente, detectando alterações de desempenho e diagnosticando suas causas. Isso é feito por meio de logs, métricas e rastreamento distribuído, que fornecem informações sobre operações individuais, medições de desempenho e rastreamento de solicitações e atividades entre os componentes. Esses três pilares da observabilidade permitem uma visão abrangente do sistema e podem incluir dados de telemetria do runtime do .NET, bibliotecas e código específico do aplicativo. 

## Tecnologias utilizadas

O OpenTelemetry (OTel) é um padrão aberto e multiplataforma para coleta e emissão de dados de telemetria. Ele oferece APIs para gravar dados telemétricos durante a execução do código, permitindo aos desenvolvedores configurar o envio, filtragem, armazenamento e transformação desses dados. O OTel também fornece convenções semânticas para orientar a nomenclatura e o conteúdo dos dados telemétricos, garantindo uma análise eficaz. Além disso, o OTel possui uma interface para exportadores, que são plug-ins para transmitir dados telemétricos em diferentes formatos para diversos sistemas de telemetria.

O OTel suporta o protocolo de ligação OTLP como opção de rede neutra do fornecedor para transmitir dados telemétricos, além de protocolos proprietários existentes. Isso possibilita a integração com uma ampla variedade de sistemas APM (Application Performance Monitoring), incluindo sistemas de código aberto como Prometheus e Grafana, bem como o Azure Monitor da Microsoft e outros fornecedores que são parceiros do OpenTelemetry.

O OpenTelemetry possui implementações disponíveis para a maioria das linguagens e plataformas, incluindo o .NET. Isso significa que os desenvolvedores podem aproveitar os recursos do OTel em seus aplicativos .NET para coletar e emitir dados de telemetria de forma padronizada e interoperável com outros sistemas de monitoramento e análise.

## Conceitos aprendidos

Os conceitos aprendidos na atividade desenvolvida estão intimamente correlacionados com o core do objetivo final: mensuração. Dessa forma, assim como já citado, uns dos conceitos aprendidos entram em: observabilidade, a própria tecnologia OpenTelemetry, além de métricas, logs e rastreamento distribuído.


- Observabilidade: no contexto de um sistema distribuído, é a capacidade de monitorar e analisar a telemetria sobre o estado de cada componente, observar alterações no desempenho e diagnosticar por que essas alterações ocorrem.
- O OpenTelemetry (OTel): é um padrão aberto e multiplataforma para coletar e emitir dados de telemetria.
- Logs, que registram operações individuais, como uma solicitação de entrada, uma falha em um componente específico ou um pedido sendo feito.
- Métricas, que são contadores de medição e medidores, como número de solicitações concluídas, solicitações ativas, widgets vendidos; ou um histograma da latência da solicitação.
- Rastreamento distribuído, que rastreia solicitações e atividades entre componentes em um sistema distribuído para que você possa ver onde o tempo é gasto e rastrear falhas específicas.

## Projeto executando

