import click

from .http import clipython
from .stats import Results

@click.command()
@click.option("--requests", "-r", default=500, help="Numero de requisicoes a se fazer")
@click.option("--concurrency", "-c", default=1, help="Numero de requisicoes concorrentes")
@click.option("--json-file", "-j", default=None, help="Exportar para um arquivo json no caminho especificado")
@click.argument("url")
def cli(requests, concurrency, json_file, url):

    total_time, requests_dict = clipython(url, requests, concurrency)
    results = Results(total_time, requests_dict)
    display(results, json_file)

def display(results, json_file):
    if json_file:
          # Write to a file
        json.dump(
        {
            "requisicoes_sucesso": results.successful_requests(),
            "mais_lenta": results.slowest(),
            "mais_rapida": results.fastest(),
            "tempo_total": results.total_time,
            "requisicoes_por_minuto": results.requests_per_minute(),
            "requisicoes_por_segundo": results.requests_per_second(),
        },
        json_file,
        )
        json_file.close()
        print(".... Feito!")
    else:
        print('...Feito!')
        print('--- Resultados ---')
        print(f"Requisicoes com sucesso\t{results.sucessful_requests}")
        print(f"Mais lenta             \t{results.slowest}")
        print(f"Mais rapida            \t{results.fastest}")
        print(f"Media                  \t{results.average}")
        print(f"Tempo total            \t{results.total_time}")
        print(f"Requisicoes por minuto \t{results.requests_per_minute}")
        print(f"Requisicoes por segundo\t{results.requests_per_second}")


