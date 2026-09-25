import json
import pandas as pd
from pathlib import Path

PASTA_DADOS = Path(__file__).resolve().parent.parent / "data"


def _ler_json(nome):
    with open(PASTA_DADOS / nome, "r", encoding="utf-8") as f:
        return json.load(f)


def montar_contexto() -> str:
    """Lê todos os arquivos e monta o texto que vai no prompt."""
    perfil = _ler_json("perfil_investidor.json")
    produtos = _ler_json("produtos_financeiros.json")
    transacoes = pd.read_csv(PASTA_DADOS / "transacoes.csv")
    atendimentos = pd.read_csv(PASTA_DADOS / "historico_atendimento.csv")

    gastos = (
        transacoes[transacoes["tipo"] == "saida"]
        .groupby("categoria")["valor"].sum()
    )

    linhas = [
        "=== PERFIL DO CLIENTE ===",
        f"Nome: {perfil['nome']} | Idade: {perfil['idade']}",
        f"Profissão: {perfil['profissao']} | Renda: R$ {perfil['renda_mensal']:.2f}",
        f"Perfil investidor: {perfil['perfil_investidor']}",
        f"Aceita risco: {'Sim' if perfil['aceita_risco'] else 'Não'}",
        f"Reserva atual: R$ {perfil['reserva_emergencia_atual']:.2f}",
        "Metas:",
    ]
    for m in perfil["metas"]:
        linhas.append(f"  - {m['meta']}: R$ {m['valor_necessario']:.2f} até {m['prazo']}")

    linhas.append("\n=== GASTOS DO MÊS (por categoria) ===")
    for cat, val in gastos.items():
        linhas.append(f"  - {cat}: R$ {val:.2f}")

    total_saidas = transacoes[transacoes["tipo"] == "saida"]["valor"].sum()
    total_entradas = transacoes[transacoes["tipo"] == "entrada"]["valor"].sum()
    linhas.append(f"  Total saídas: R$ {total_saidas:.2f}")
    linhas.append(f"  Total entradas: R$ {total_entradas:.2f}")
    linhas.append(f"  Sobrou no mês: R$ {total_entradas - total_saidas:.2f}")

    linhas.append("\n=== PRODUTOS DISPONÍVEIS (base oficial) ===")
    for p in produtos:
        linhas.append(
            f"  - {p['nome']} | {p['categoria']} | risco {p['risco']} | "
            f"{p['rentabilidade']} | mín R$ {p['aporte_minimo']:.2f} | "
            f"indicado para: {p['indicado_para']}"
        )

    linhas.append("\n=== HISTÓRICO DE ATENDIMENTOS ===")
    for _, row in atendimentos.tail(5).iterrows():
        linhas.append(f"  - {row['data']} ({row['canal']}): {row['tema']} — {row['resumo']}")

    return "\n".join(linhas)