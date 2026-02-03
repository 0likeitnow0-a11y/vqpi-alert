
ACOES = [
    "BBAS3", "BBDC4", "ITSA4", "CPFE3", "CSMG3",
    "UNIP3", "VULC3", "LEVE3", "SLCE3", "RANI3"
]

PESO_BASE = {acao: 1 / len(ACOES) for acao in ACOES}

MULTIPLICADORES = {
    "VERDE": 2.0,
    "AMARELA": 1.0,
    "VERMELHA": 0.3
}
