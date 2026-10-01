import os
import pickle
import sys

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def main():
    print("Iniciando Dummy Training...")

    try:
        df = pd.read_csv("dataset_processado.csv")

        X = df[["feature1", "feature2"]]
        y = df["target"]

        clf = DecisionTreeClassifier(max_depth=2)
        clf.fit(X, y)
        
        # Simulação de salvamento do modelo em disco (artefato binário)
        with open('modelo.pkl', 'wb') as f:
            pickle.dump(clf, f)
            
        # ==========================================
        # GOVERNANÇA: Integração com Model Registry
        # ==========================================
        commit_sha = os.environ.get("GITHUB_SHA", "Desconhecido")
        
        print("\n--- Integrando com o Model Registry ---")
        print("Enviando o arquivo modelo.pkl para o armazenamento central...")
        print(
            "ETIQUETA DE RASTREABILIDADE: "
            f"Modelo ligado ao commit Git: {commit_sha}"
        )
        print("SUCESSO: O modelo foi registrado.")

    except (FileNotFoundError, KeyError, ValueError, OSError) as error:
        print(f"ERRO DE COMPUTAÇÃO: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()