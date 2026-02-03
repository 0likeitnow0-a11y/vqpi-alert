def preco_justo_fcf(fcf, multiplo, acoes):
    return (fcf * multiplo) / acoes


def preco_justo_multiplo(lpa, pl_medio):
    return lpa * pl_medio


def preco_justo_dividendos(dividendo_anual, yield_justo):
    return dividendo_anual / yield_justo


def faixa_preco_justo(valores):
    return {
        "min": round(min(valores), 2),
        "max": round(max(valores), 2)
    }


def calcular_faixas(FUNDAMENTOS):
    faixas = {}

    for acao, d in FUNDAMENTOS.items():
        valores = [
            preco_justo_fcf(d["fcf"], d["multiplo_fcf"], d["acoes"]),
            preco_justo_multiplo(d["lpa"], d["pl_medio"]),
            preco_justo_dividendos(d["dividendo"], d["yield_justo"])
        ]
        faixas[acao] = faixa_preco_justo(valores)

    return faixas
  
