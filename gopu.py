#!/usr/bin/env python3
import sys, requests, json

BASE = "https://gopuos.onrender.com"

def status():
    r = requests.get(f"{BASE}/status.json")
    print(json.dumps(r.json(), indent=2))

def infer(prompt):
    r = requests.post(f"{BASE}/inference", json={"prompt": prompt})
    print("🧠", r.json()["response"])

def token_generate():
    r = requests.post(f"{BASE}/token/generate", json={"role": "inference", "modules": ["inference", "status", "badge"]})
    print("🔐 Token créé :", r.json()["token"])

def token_verify(token):
    r = requests.post(f"{BASE}/token/verify", json={"token": token})
    print(json.dumps(r.json(), indent=2))

def db_test():
    r = requests.get(f"{BASE}/db-test")
    print("🗄️ MySQL time:", r.json()["mysql_time"])

def help():
    print("""
🔧 GopuOS CLI — Agent Terminal
Usage:
  gopu status               → Introspection CPU/GPU/modules
  gopu infer "prompt"       → Envoie un prompt à l’IA
  gopu token --generate     → Crée un token gp_...
  gopu token --verify TOKEN → Vérifie un token
  gopu db --test            → Teste la base MySQL
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
    elif sys.argv[1] == "status":
        status()
    elif sys.argv[1] == "infer":
        infer(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "token" and sys.argv[2] == "--generate":
        token_generate()
    elif sys.argv[1] == "token" and sys.argv[2] == "--verify":
        token_verify(sys.argv[3])
    elif sys.argv[1] == "db" and sys.argv[2] == "--test":
        db_test()
    else:
        help()
