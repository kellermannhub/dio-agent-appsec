# Fundamentos de Segurança da Informação

Base de conhecimento usada pela skill `vulnerability-analysis`.

## Conceitos Fundamentais

### Vulnerabilidade

Fraqueza em um sistema, processo ou configuração que pode ser explorada. Exemplo: consulta SQL montada pela concatenação do que a pessoa digitou.

### Ameaça

Agente ou evento capaz de explorar uma vulnerabilidade. Exemplos: atacante externo, malware, erro humano.

### Risco

Chance de uma ameaça explorar uma vulnerabilidade, combinada com o impacto que isso causaria. Em termos conceituais: risco ≈ ameaça × vulnerabilidade × impacto.

- **Impacto:** dano aos dados e ao negócio se a falha for explorada.
- **Probabilidade:** facilidade e chance de exploração no contexto (exposição, autenticação, exploits públicos).
- **Severidade:** combinação de impacto e probabilidade. A mesma falha tem severidades diferentes em laboratório isolado e em produção exposta.

### Referências de classificação

- **CWE:** tipos de fraqueza (ex.: CWE-89, SQL Injection; CWE-798, credenciais no código).
- **OWASP Top 10:** categorias mais críticas de risco em aplicações web.
- **MITRE ATT&CK:** técnicas de atacantes (ex.: T1190, Exploit Public-Facing Application; T1078, Valid Accounts; T1110, Brute Force).
- **CVSS e CVE:** pontuação padronizada e identificador de vulnerabilidades conhecidas.
- **CIS Benchmarks:** guias de configuração segura.

## Princípios de Segurança

### Confidencialidade

Garantir que apenas pessoas autorizadas tenham acesso.

### Integridade

Garantir que informações não sejam alteradas indevidamente.

### Disponibilidade

Garantir que sistemas continuem funcionando.

## Boas práticas

- Usar consultas parametrizadas e nunca concatenar entrada do usuário em SQL, comandos ou HTML.
- Validar entradas e codificar saídas.
- Guardar segredos fora do código (variáveis de ambiente, cofres de segredos).
- Armazenar senhas com hash adequado (bcrypt, scrypt ou Argon2), nunca em texto puro.
- Aplicar o princípio do menor privilégio em contas, serviços e permissões.
- Expor apenas portas e serviços necessários, com firewall negando por padrão.
- Usar chaves SSH e MFA no acesso remoto, sem login direto de root.
- Manter sistemas e dependências atualizados.
- Registrar logs e monitorar eventos suspeitos.
- Fazer backups e testá-los.
- Adotar defesa em profundidade: nunca depender de um único controle.
- Revisar a segurança a cada alteração, antes de ir para produção (DevSecOps).
- Testar apenas em ambientes próprios, de laboratório ou autorizados.
