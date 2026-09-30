# Ficha de Avaliação de Processo (PDD) — Questão 5

**Cenário escolhido:** A

1. **Nome do processo e descrição resumida:**
   * Importação e consolidacao de notas fiscais atraves de planilhas CSV para o sistema de controle financeiro.

2. **Volume / frequência estimados:**
   * Cerca de 100 documentos processados diariamente, executado de segunda a sexta-feira.

3. **As entradas são estruturadas?** (sim/não + justificativa)
   * Sim, pois os dados chegam em formato padronizado (arquivos CSV com colunas definidas de nota, cliente e valor), permitindo leitura direta pelo sistema sem ambiguidade.

4. **As regras são claras e determinísticas?** (sim/não + justificativa)
   * Sim, o fluxo segue um padrao logico fixo: ler o arquivo, validar se o arquivo não esta vazio, somar os valores das notas e gerar logs de controle sem depender de interpretaçao humana.

5. **Veredito — o processo é elegível a RPA?** (justifique com base em regras claras, dados estruturados e repetibilidade)
   * Sim, é elegivel. O processo possui alta repetibilidade, utiliza dados estruturados e é guiado por regras estritamente logicas, o que o torna ideal para ser totalmente automatizado por um robô.