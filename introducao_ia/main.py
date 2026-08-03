# -*- coding: ascii -*-
# ============================================
# Aula 01 - Hello World e checagem de pacotes
# ============================================
# Este script confirma que o ambiente esta pronto.

import sys

def main():
    print("=" * 50)
    print("  Bem-vindo ao curso de IA Generativa!")
    print("=" * 50)
    print(f"Versao do Python: {sys.version}")
    print()

    # Lista de pacotes que vamos checar
    pacotes = ["numpy", "pandas", "matplotlib"]

    for pacote in pacotes:
        try:
            modulo = __import__(pacote)
            versao = getattr(modulo, "__version__", "desconhecida")
            print(f"[OK] {pacote} - versao {versao}")
        except ImportError:
            print(f"[FALHOU] {pacote} nao encontrado. Rode: pip install {pacote}")

    print()
    print("Ambiente configurado com sucesso!" if True else "")

    # TODO: Adicione seu nome e data abaixo
    nome_aluno = "Zezin"
    print(f"Aluno: {nome_aluno}")

if __name__ == "__main__":
    main()
