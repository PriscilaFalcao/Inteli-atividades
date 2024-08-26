# Ponderada semana 3

"Este autoestudo ponderado direciona o estudante para criar um pacote em python que deverá fazer a ingestão dos dados para o banco de dados ou data lake da sua arquitetura

1 - Eficiência na Implementação em Python (30%): O aluno deverá fazer uma implementação solida abordando todos os requisitos funcionais e não funcionais do problema.

2 - Organização e Estrutura do Código (20%): O aluno deverá construir o código de forma organizada e com uma estrutura lógica clara e bem documentado.

3 - Manuseio de Exceções e Erros (15 pontos): O aluno deverá incluir um sistema de controel de erros e exceções robusto abordando o máximo de falhas do sistema.

4 - Testes com o Pytest (35 pontos): O aluno deverá definir, implementar e executar todos os testes necessários e eficazes para garantir o atendimento aos requisitos.

Maiores instruções estão presentes no arquivo:
[ponderada_aula5_ingestao.ipynp](./ponderada_aula_5_ingestao.ipynb)


## Resolução

> Inicialmente, vale destacar que parte da atividade foi feita em sala de aula juntamente com o professor, nesse sentido, entende-se que as práticas ensinadas atendem aos requisitos das orientações da ponderada. Ps: se nós não tivéssemos feito em sala de aula parte da atividade, apenas com as instruções da Adalove nunca saberia o que era para ser de fato feito.

Para a resolução da tarefa, foi feita a estrutura de pasta, conforme instrução, dessa forma, para encontrar o código, basta se direcionar para ```./meu-pacote```.

1) Escolha da API

Para a execução da atividade, foi escolhida a api de fatos sobre cachorros, disponível em:  https://dukengn.github.io/Dog-facts-API/

2) Desenvolvimento do pacote Python

Pode ser encntrado dentro da pasta ```./meu-pacote/data_pipeline```.

3) Armazenamento na nuvem

Não houve armazenamento na nuvem, especificamente. Para o armazenamento dos dados, foi utilizado o Minio (datalake) e o Clickhouse (datawarehouse).