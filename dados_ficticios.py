"""Gera dados 100% fictícios, só para praticar — nenhum nome ou valor real aqui.

As proporções (quantos têm processo aberto, quantos têm OB solicitada) foram
calibradas para parecer com a distribuição real (a maioria ainda sem processo
e aguardando pagamento), mas todo nome, CPF e valor aqui é inventado.
"""
import random
from datetime import date, timedelta

PRIMEIROS_NOMES = [
    "Ana", "Bruno", "Carla", "Diego", "Elaine", "Fábio", "Gabriela", "Heitor",
    "Ivana", "João", "Kelly", "Leandro", "Marina", "Nelson", "Otávia", "Paulo",
    "Quitéria", "Rafael", "Sônia", "Tiago", "Úrsula", "Vitor", "Wanda", "Yara",
]
SOBRENOMES = [
    "Exemplo", "Modelo", "Fictício", "Teste", "Amostra", "Ilustrativo", "Placeholder",
    "Simulado", "Genérico", "Demonstração", "Rascunho", "Protótipo", "Referência",
]
UGS = ["40806", "40805", "40802"]
BANCOS = ["Banco do Brasil", "Caixa Econômica", "Santander", "Bradesco", "Itaú", "Banrisul", "Sicoob"]
MESES_ABREV = ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"]


def gerar_registros(quantidade=600, semente=42):
    random.seed(semente)
    hoje = date.today()
    registros = []
    for _ in range(quantidade):
        nome = f"{random.choice(PRIMEIROS_NOMES)} {random.choice(SOBRENOMES)} {random.choice(SOBRENOMES)}"
        ano = hoje.year - random.randint(0, 7)  # período de vários anos, como nos dados reais
        mes_idx = random.randint(0, 11)
        tem_processo = random.random() < 0.06   # ~6%, igual à proporção real
        tem_ob = random.random() < 0.04         # ~4%, igual à proporção real
        registros.append({
            "nome": nome,
            "ug": random.choice(UGS),
            "banco": random.choice(BANCOS),
            "valor": round(random.uniform(80, 15000), 2),
            "mes": f"{MESES_ABREV[mes_idx]}/{ano}",
            "ob_solicitada_em": (hoje - timedelta(days=random.randint(1, 400))) if tem_ob else None,
            "processo": f"14021.{random.randint(100000,999999)}/{ano}-{random.randint(10,99)}" if tem_processo else "",
        })
    return registros
