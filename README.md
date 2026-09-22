# SAST-bandit

# SAST: Análise Estática de Segurança no Desenvolvimento

Trabalho acadêmico com aplicação prática, demonstrando o funcionamento de uma
ferramenta de **SAST (Static Application Security Testing)** sobre um projeto
Python real, usando o **[Bandit](https://bandit.readthedocs.io/)**.

O repositório mostra a evolução de um mesmo script: código vulnerável →
código corrigido, sem nenhum alerta de segurança.

## 📌 O que é SAST

SAST é uma técnica de análise de segurança que examina o código-fonte,
bytecode ou binário de uma aplicação **sem executá-la**, buscando padrões que
indiquem vulnerabilidades (SQL Injection, uso de criptografia fraca, segredos
expostos, etc). É normalmente integrada cedo no ciclo de desenvolvimento
(*shift-left security*), dentro de pipelines de CI/CD.

## 📁 Estrutura do repositório

```
.
├── 1_app_vulneravel.py           # código com 6 vulnerabilidades propositais
├── 2_app_corrigida_final_v2.py   # código corrigido (0 issues no Bandit)
├── relatorio_bandit_antes.txt    # relatório do Bandit no código vulnerável
├── relatorio_v2_zero_issues.txt  # relatório do Bandit no código corrigido
├── COMO_APRESENTAR.txt           # roteiro passo a passo da demonstração
├── resumo_para_slides_SAST.txt   # resumo do tema para gerar slides
└── SAST_Trabalho_Aplicacao_Pratica.docx  # trabalho completo em Word
```

## 🐍 Vulnerabilidades demonstradas

| # | Vulnerabilidade | CWE |
|---|---|---|
| 1 | Credencial hardcoded no código | CWE-259 |
| 2 | SQL Injection (concatenação de string) | CWE-89 |
| 3 | Hash fraco (MD5) | CWE-327 |
| 4 | Execução de comando de SO via concatenação (`os.popen`) | CWE-78 |
| 5 | `subprocess` com `shell=True` | CWE-78 |
| 6 | Desserialização insegura (`pickle`) | CWE-502 |

## 🔧 Correções aplicadas

- Query SQL → parametrizada
- MD5 → `PBKDF2-HMAC-SHA256` com salt
- `subprocess(shell=True)` → lista de argumentos, sem shell
- Credencial → variável de ambiente
- `pickle` → `json`
- Comando externo (`ping`) → biblioteca nativa (`socket`)
- Entradas externas → validadas com whitelist (regex)

## 📊 Resultado (Bandit)

| Severidade | Vulnerável | Corrigido |
|---|---|---|
| High | 3 | 0 |
| Medium | 2 | 0 |
| Low | 3 | 0 |
| **Total** | **8** | **0** |

Resultado final: `No issues identified.`

## ▶️ Como executar

Pré-requisito: Python instalado.

```bash
pip install bandit
```

Rodar a análise em cada versão do código:

```bash
python -m bandit 1_app_vulneravel.py
python -m bandit 2_app_corrigida_final_v2.py
```

> No Windows, se o comando `bandit` não for reconhecido, use sempre
> `python -m bandit ...` (evita problema de PATH).

Para salvar o relatório em arquivo:

```bash
python -m bandit 1_app_vulneravel.py -f txt -o relatorio.txt
```

## 🛠️ Tecnologias

- Python 3
- [Bandit](https://bandit.readthedocs.io/) — ferramenta de SAST

## 📚 Referências

- BANDIT. *Bandit Documentation*. Disponível em: https://bandit.readthedocs.io
- OWASP. *Static Application Security Testing*. OWASP Foundation.
- MITRE. *Common Weakness Enumeration (CWE)*. Disponível em: https://cwe.mitre.org
