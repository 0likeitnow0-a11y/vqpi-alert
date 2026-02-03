
from dados import ACOES, PESO_BASE, MULTIPLICADORES
from market import get_prices
from dados_fundamentais import FUNDAMENTOS
from valuation import calcular_faixas
from vqpi import calcular_aportes
from alerts import check_zone_alerts
from telegram_alert import send_telegram_message


def executar_vqpi():
    print("🚀 Executando VQPI...")

    # 1️⃣ Preços atuais
    precos = get_prices(ACOES)

    # 2️⃣ Cálculo automático das faixas de preço justo
    faixas = calcular_faixas(FUNDAMENTOS)

    # 3️⃣ Cálculo dos aportes
    resultado = calcular_aportes(
        precos,
        faixas,
        500,
        PESO_BASE,
        MULTIPLICADORES
    )

    # 4️⃣ Verificação de mudança de zona
    zonas = {a: v["zona"] for a, v in resultado.items()}
    alerts = check_zone_alerts(zonas)

    if alerts:
        mensagem = "🔔 *VQPI – Mudança de Zona*\n\n"
        mensagem += "\n".join(alerts)
        send_telegram_message(mensagem)
        print("⚠️ Mudança de zona detectada.")
    else:
        print("✅ Nenhuma mudança de zona.")

    print("✅ Execução finalizada.")


if __name__ == "__main__":
    executar_vqpi()
  
