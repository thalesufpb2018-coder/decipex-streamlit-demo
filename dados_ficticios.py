"""Gera dados 100% fictícios, só para praticar — nenhum nome ou valor real aqui."""
import random
from datetime import date, timedelta

NOMES = [
    "Ana Exemplo", "Bruno Modelo", "Carla Fictícia", "Diego Teste", "Elaine Amostra",
    "Fábio Ilustrativo", "Gabriela Placeholder", "Heitor Simulado", "Ivana Genérica",
    "João Demonstração", "Kelly Rascunho", "Leandro Protótipo",
]
UGS = ["40806", "40805", "40802"]
BANCOS = ["Banco do Brasil", "Caixa Econômica", "Santander", "Bradesco", "Itaú", "Banrisul"]
MESES_ABREV = ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"]


def gerar_registros(quantidade=60, semente=42):
    random.seed(semente)
    hoje = date.today()
    registros = []
    for _ in range(quantidade):
        mes_idx = random.randint(0, 11)
        ano = hoje.year if mes_idx <= hoje.month - 1 else hoje.year - 1
        tem_processo = random.random() < 0.3
        tem_ob = random.random() < 0.25
        registros.append({
            "nome": random.choice(NOMES),
            "ug": random.choice(UGS),
            "banco": random.choice(BANCOS),
            "valor": round(random.uniform(150, 9000), 2),
            "mes": f"{MESES_ABREV[mes_idx]}/{ano}",
            "ob_solicitada_em": (hoje - timedelta(days=random.randint(1, 90))) if tem_ob else None,
            "processo": f"14021.{random.randint(100000,999999)}/{ano}-{random.randint(10,99)}" if tem_processo else "",
        })
    return registros
