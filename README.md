# Diagnóstico da Mecanização — Fazenda Canoas

Resumo: diagnóstico técnico-operacional da mecanização da Fazenda Canoas (Ponte Alta - SC). Contém o texto em LaTeX, figuras e scripts para gerar gráficos.

Como compilar
- Recomendado: use `latexmk -pdf` ou sequência `pdflatex -> bibtex -> pdflatex -> pdflatex`.

Regenerar figuras
- Scripts Python/R estão em `trabalho diagnostico/` (ver `grafico-*.py` e `*.r`). Crie um `requirements.txt` para facilitar (posso gerar um se quiser).

Observações
- Não versionamos arquivos temporários do LaTeX (já incluídos em `.gitignore`).
- Evite subir PDFs finais se você não quiser versionar binários; remova `*.pdf` do `.gitignore` nesse caso.

Contato
- Autor(es): Christian Roger Gaio, Eduardo Favretto
