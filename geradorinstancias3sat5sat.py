import random
import matplotlib.pyplot as plt

def generate_sat_instance(n, m, k):
    clauses = set()

    while len(clauses) < m:
        variables = random.sample(range(1, n + 1), k)
        clause = tuple(sorted(literal if random.random() < 0.5 else -literal for literal in variables))

        clauses.add(clause)

    return list(clauses)

def plot_instance(n, m):
    alpha = m / n
    plt.figure(figsize=(6, 4))
    plt.scatter(n, alpha, color='blue', label=f'α = {alpha:.2f}')
    plt.axhline(y=alpha, color='r', linestyle='--', alpha=0.6)
    plt.ylabel('Razão α = m/n')
    plt.xlabel('Número de Variáveis (n)')
    plt.title('Proporção de Cláusulas por Variável')
    plt.legend()
    plt.ylim(0, max(5, alpha + 1))
    plt.grid(True)
    plt.show()

n = int(input("Digite o número de variáveis (n): "))
m = int(input("Digite o número de cláusulas (m): "))
k = int(input("Digite o valor de k (3 para 3-SAT, 5 para 5-SAT): "))

if k not in [3, 5]:
    print("Valor de k inválido! Escolha 3 ou 5.")
else:
    instance = generate_sat_instance(n, m, k)
    print("\nInstância gerada:")
    for clause in instance:
        formatted_clause = " ∨ ".join(f"¬x{abs(lit)}" if lit < 0 else f"x{lit}" for lit in clause)
        print(f"({formatted_clause})")

    plot_instance(n, m)
