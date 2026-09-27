import time
import requests

# Lien Webhook Discord
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1553572284852215858/4HpYc0PjtUcpkAOMOJ776_jnHDFgofbjxAsOowiMInbMsAhzmFfygT1tZW8Qy9yXZIYu"

def envoyer_discord(message):
    payload = {"content": message}
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5)
    except Exception as e:
        print(f"Erreur d'envoi Discord : {e}")

def demarrage_bot():
    msg = (
        "🚀 **BOT SUREBET EN LIGNE (DISCORD)**\n"
        "⚙️ **Statut :** Opérationnel sur le Cloud\n"
        "🧪 **Mode :** Simulation (0 Risk)\n"
        "----------------------------------------\n"
        "_Analyse continue des marchés en cours..._"
    )
    print("Démarrage du bot...")
    envoyer_discord(msg)

def scanner_et_miser():
    # Simulation d'un Surebet détecté
    cotes = {"bk1": 2.15, "bk2": 2.10}
    marge = (1 / cotes["bk1"]) + (1 / cotes["bk2"])
    
    if marge < 1.0:
        rendement = (1 - marge) * 100
        capital = 1000
        mise1 = round(capital / (cotes["bk1"] * marge))
        mise2 = capital - mise1
        benefice = round(mise1 * cotes["bk1"]) - capital
        
        rapport = (
            f"⚡ **SUREBET DÉTECTÉ ET EXÉCUTÉ !**\n"
            f"🏆 **Match :** Tennis Live (ATP)\n"
            f"📈 **Rendement :** +{rendement:.2f}%\n"
            f"🎯 **Bookmaker 1 :** {mise1} FCFA (Cote {cotes['bk1']})\n"
            f"🎯 **Bookmaker 2 :** {mise2} FCFA (Cote {cotes['bk2']})\n"
            f"💰 **Gain garanti :** +{benefice} FCFA"
        )
        envoyer_discord(rapport)

if __name__ == "__main__":
    demarrage_bot()
    while True:
        try:
            scanner_et_miser()
            time.sleep(3600)
        except Exception as e:
            print(f"Erreur : {e}")
            time.sleep(10)
