import asyncio
import time
import os
import requests

def fetch(url):
    """ Faz as requisicoes HTTP e retorna o resultado """
    started_at = time.monotonic()
    response = requests.get(url)
    request_time = time.monotonic() - started_at
    return {"status_code": response.status_code, "request_time": request_time}

async def worker(name, queue, results):
    """ Funcao para fazer o trabalho, pegando requisicoes da fila """
    loop = asyncio.get_event_loop()
    while True:
        url = await queue.get()
        if os.getenv("DEBUG"):
            print(f"{name} - Fetching {url}")
    future_result = loop.run_in_executor(None, fetch, url)
    result = await future_result
    results.append(result)
    queue.task_done()

async def distribute_work(url, requests, concurrency, results):
    """ Divide a carga e agrega os resultados """
    queue = asyncio.Queue()

    # Adiciona um item a fila para cada requisicao
    for _ in range(requests):
        queue.put_nowait(url)

    # Criar workers para fazer match com a concorrencia
    tasks = []
    for i in range(concurrency):
        task = asyncio.create_task(worker(f"worker-{i+1}", queue, results))
        tasks.append(task)

    started_at = time.monotonic()
    await queue.join()
    total_time = time.monotonic() - started_at

    for task in tasks:
        task.cancel()


    print("----")
    print(f"{concurrency} workers levou um total de {total_time:.2f} segundos para completar {len(results)} requisições")


def clipython(url, requests, concurrency):
    """ Ponto de entrada das requisicoes """
    results = []
    asyncio.run(distribute_work(url, requests, concurrency, results))
    print(results)