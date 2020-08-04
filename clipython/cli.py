import click

@click.command()
@click.option("--requests", "-r", default=500, help="Numero de requisicoes a se fazer")
@click.option("--concurrency", "-c", default=1, help="Numero de requisicoes concorrentes")
@click.option("--json-file", "-j", default=None, help="Exportar para um arquivo json no caminho especificado")
@click.argument("url")
def cli(requests, concurrency, json_file, url):
    print(f"Requisicoes: {requests}")
    print(f"Concorrencia: {concurrency}")
    print(f"Arquivo JSON: {json_file}")
    print(f"URL: {url}")

if __name__ == "__main__":
    cli()