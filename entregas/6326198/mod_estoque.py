# =============================================================================
# Questao 3 - Modularizacao com Funcoes e Dicionarios (Aula 03)
#
# MOLDE DE ENTREGA (contrato). Copie para entregas/SEU_RA/ e IMPLEMENTE.
# Sem logica pronta, sem erros plantados: so as assinaturas e o que cada
# funcao deve fazer. A implementacao e sua.
#
# =============================================================================


def cadastrar_item(nome: str, quantidade: int, preco_unitario: float) -> dict:
    return {
        "nome": nome,
        "quantidade": quantidade,
        "preco_unitario": preco_unitario
    }

  
def calcular_valor_estoque(itens: list) -> float:
    total:float = 0
    
    for item in itens:
        total += item["quantidade"] * item["preco_unitario"]
    return total   


def listar_itens_em_falta(itens: list, minimo: int) -> list:
    falta = []
    
    for item in itens:
        if item["quantidade"] < minimo:
            falta.append(item)
    return falta        