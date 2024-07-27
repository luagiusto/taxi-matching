import pandas as pd
import matplotlib.pyplot as plt

# Cargar los resultados
df_punto6 = pd.read_csv('/resultados_punto6.csv')

# Revisar la estructura del DataFrame
print(df_punto6.head())

# Analizar los resultados comparativos
def interpret_results(df):
    print("Análisis de Resultados Comparativos:")
    for percentil in df['Percentil'].unique():
        subset = df[df['Percentil'] == percentil]
        avg_mejora = subset['Mejora relativa'].mean()
        total_no_factibles = subset['Numero de asignaciones no factibles'].sum()
        print(f"Percentil {percentil}:")
        print(f"  - Promedio Mejora %: {avg_mejora:.2f}")
        print(f"  - Total Asignaciones No Factibles: {total_no_factibles}")

# Interpretar los resultados comparativos
interpret_results(df_punto6)

# Visualizar los resultados comparativos con matplotlib
def visualize_results(df):
    plt.figure(figsize=(14, 8))

    for percentil in df['Percentil'].unique():
        subset = df[df['Percentil'] == percentil]
        plt.bar(subset['Instancia'], subset['Numero de asignaciones no factibles'], label=f'Percentil {percentil}')

    plt.xlabel('Instancia')
    plt.ylabel('Numero de asignaciones no factibles')
    plt.title('Asignaciones no factibles por percentil')
    plt.legend()
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

# Visualizar los resultados
visualize_results(df_punto6)


