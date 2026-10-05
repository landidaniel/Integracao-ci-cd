import sys

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def main():
    print("Iniciando Dummy Training (Treinamento de Sanidade)...")

    try:
        df = pd.read_csv("dataset_processado.csv")

        X = df[["feature1", "feature2"]]
        y = df["target"]

        clf = DecisionTreeClassifier(max_depth=2)
        clf.fit(X, y)

        score = clf.score(X, y)

        print(
            "SUCESSO: Modelo treinado sem erros de sintaxe! "
            f"Acurácia no micro-dataset: {score}"
        )
        sys.exit(0)

    except (FileNotFoundError, KeyError, ValueError, OSError) as error:
        print("ERRO DE COMPUTAÇÃO: " f"O código do modelo falhou. Detalhes: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
