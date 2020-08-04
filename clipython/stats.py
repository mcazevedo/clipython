from typing import List, Dict


class Results:
    """
    Results cacula as estatísticas de carga com base nas requisicoes feitas.
    Exemplo abaixo:

    Requisicoes com sucesso     3000
    Mais lenta                  0.010s
    Mais rapida                 0.001s
    Media                       0.003s
    Tempo total                 2.400s
    Requisicoes por minuto      90000
    Requisicoes por segundo     125
    """

    def __init__(self, total_time: float, requests: List[Dict]):
        self.total_time = total_time
        self.requests = requests

    def slowest(self) -> float:
        """
        Retorna a requisicao mais lenta

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.slowest()
        6.1
        """
        pass

    def fastest(self) -> float:
        """
        Retorna a requisicao mais rapida

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.fastest()
        1.04
        """
        pass

    def average_time(self) -> float:
        """
        Retorna a media do tempo de resposta

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.average_time()
        9.846666667
        """
        pass

    def total_time(self) -> float:
        pass

    def successful_requests(self) -> int:
        """
        Retorna as requisicoes com sucesso
        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.successful_requests()
        
        """
        pass