# Clipython

CLI para teste de carga de requisições.

## Instalação

Use `pip`

```bash
pip install clipython
```

## Uso

A maneira mais simples é apenas chamar a URL

```bash
clipython https://exemplo.com.br
...Feito!
--- Resultados ---
Requisicoes com sucesso     500
Mais lenta                  0.010s
Mais rapida                 0.001s
Media                       0.003s
Tempo total                 0.620s
Requisicoes por minuto      48360
Requisicoes por segundo     806
```


Adicione concorrência com a flag `-c` , and we can use a flag `-r` para direcionar a quantidade de requisiçoes

```
$ clipython -r 3000 -c 10 https://exemplo.com.br

Para carregar o resultado em json use a opção `-j`

$ clipython -r 3000 -c 10 -j output.json https://exemplo.com.br