ACOES = [
    "BBAS3",
    "CSMG3"
]


PESO_BASE = {acao: 1 / len(ACOES) for acao in ACOES}

MULTIPLICADORES = {
    "VERDE": 2.0,
    "AMARELA": 1.0,
    "VERMELHA": 0.3
}
