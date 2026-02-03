def classificar_zona(preco, faixa_min, faixa_max):
    if preco <= faixa_min * 0.8:
        return "VERDE"
    elif preco >= faixa_max * 1.2:
        return "VERMELHA"
    else:
        return "AMARELA"


def calcular_aportes(precos, faixas, aporte_total, pesos, multiplicadores):
    aportes = {}

    for acao in precos:
        zona = classificar_zona(
            precos[acao],
            faixas[acao]["min"],
            faixas[acao]["max"]
        )

        aporte = (
            aporte_total *
            pesos[acao] *
            multiplicadores[zona]
        )

        aportes[acao] = {
            "zona": zona,
            "aporte_bruto": aporte
        }

    soma = sum(v["aporte_bruto"] for v in aportes.values())

    for acao in aportes:
        aportes[acao]["aporte_final"] = (
            aportes[acao]["aporte_bruto"] * aporte_total / soma
        )

    return aportes
  
