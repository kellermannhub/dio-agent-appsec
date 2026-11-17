# DIO Agent + Análise de Vulnerabilidades

Evolução do [DIO Agent](https://github.com/digitalinnovationone/dio-agent) com uma nova especialização: **análise de vulnerabilidades**. Em vez de responder direto ("rode tal comando"), o agente passou a **entender o contexto, avaliar impacto, probabilidade e severidade e só então orientar a correção**.

## A especialização e por quê

O agente original é um mentor de estudos. Em segurança, uma resposta direta e sem contexto pode ser inútil ou até perigosa: o mesmo comando que ajuda num laboratório isolado pode causar estrago num servidor em produção, e a mesma falha tem gravidade diferente conforme a exposição e os dados envolvidos.

Por isso criei a skill `vulnerability-analysis`, um roteiro em Markdown com regras defensivas e sem respostas prontas:

1. Descobre o nível do estudante e o contexto (ativo, exposição, dados, controles), uma pergunta por vez
2. Identifica a falha e a causa raiz (CWE, OWASP)
3. Explica a exploração de forma conceitual e cita a técnica do MITRE ATT&CK
4. Avalia impacto, probabilidade e severidade
5. Orienta a correção, explicando o porquê
6. Valida com uma nova análise e confirma o aprendizado

O agente só atua de forma defensiva, em sistemas próprios, de laboratório ou autorizados. Não gera exploits nem malware.

## Arquivos criados e alterados

| Arquivo                                   | O que é                                                                                   |
| ----------------------------------------- | ----------------------------------------------------------------------------------------- |
| `skills/vulnerability-analysis/SKILL.md`  | **Novo.** O roteiro que o agente segue (com `name` e `description`)                       |
| `skills/vulnerability-analysis/README.md` | **Novo.** Explica a skill para pessoas                                                    |
| `agent/knowledge/security-basics.md`      | **Novo.** Vulnerabilidade, ameaça, risco, tríade CIA e boas práticas                      |
| `agent/persona.md`                        | **Alterado.** Nova seção "Postura em segurança"                                           |
| `AGENTS.md`                               | **Alterado.** Nova linha na tabela de skills e novo item na lista da base de conhecimento |
| `teste/app_vulneravel.py`                 | **Novo.** Login com SQL Injection proposital, só para laboratório                         |
| `teste/app_corrigido.py`                  | **Novo.** Versão com consulta parametrizada                                               |

## Como rodar o agente

1. Instale o Hermes seguindo a [documentação oficial](https://hermes-agent.nousresearch.com/docs).
2. Baixe o projeto:
   ```
   git clone https://github.com/kellermannhub/dio-agent-appsec.git
   ```
   (ou use **Code > Download ZIP** no GitHub e extraia a pasta)
3. Abra um terminal **dentro da pasta do projeto** e rode:
   ```
   cd dio-agent-appsec
   hermes
   ```
   Se o `hermes` for aberto em outro lugar, ele não encontra os arquivos do agente.
4. Converse. Exemplos:
   - `Analise o teste/app_vulneravel.py como especialista em AppSec. Encontre a falha, explique a exploração, cite a técnica do MITRE ATT&CK e reescreva o código.`
   - `Tenho um servidor Ubuntu de laboratório exposto na internet. O que devo verificar?`

## Teste realizado

1. **Código vulnerável:** `teste/app_vulneravel.py` monta o SQL juntando o que a pessoa digitou. O agente foi chamado como especialista em AppSec.
2. **Correção e validação:** troquei a consulta pela versão parametrizada (`teste/app_corrigido.py`) e pedi uma nova varredura para confirmar a mitigação do SQL Injection.
3. **Cenário de infraestrutura:** descrevi um servidor Ubuntu de laboratório exposto na internet e conferi se o agente **pergunta o contexto antes de sugerir qualquer comando**.

## Melhoria escolhida: formato de saída padronizado

Escolhi fazer a análise **sair sempre no mesmo formato**, com impacto, probabilidade e severidade, para permitir comparar casos diferentes. A skill define a escala, uma matriz de severidade e um modelo de resposta fixo:

```
## Resumo
## Contexto considerado
## A falha            (causa raiz, CWE/OWASP/ATT&CK, propriedade da tríade CIA)
## Como é explorada   (conceitual)
## Avaliação de risco (impacto, probabilidade, severidade)
## Como corrigir
## Validação          (e risco residual)
```

Assim, uma SQL Injection numa aplicação exposta e uma configuração insegura num servidor de laboratório podem ser lidas lado a lado.

## Próximos passos

- Skill de testes de segurança
- Skill de trilha de estudos em cibersegurança
- Mais cenários de teste (configuração insegura, problema de infraestrutura)
- Levar a revisão ao fluxo de desenvolvimento, analisando cada alteração antes da produção (DevSecOps)

## Aviso

Todos os testes usam apenas código e servidores próprios, de laboratório. O agente não deve ser usado contra sistemas de terceiros.
