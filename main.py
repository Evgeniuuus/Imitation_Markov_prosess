import random
import matplotlib.pyplot as plt


def print_simulation_table(path_with_rand):
    print(f"{'День':<5} {'Случайное число':<18} {'Состояние':<30}")
    print("-" * 60)
    for day, rand_num, state in path_with_rand[1:]:
        print(f"{day:<5} {rand_num:<18.6f} {states[state]:<30}")


def simulate_student_path(start_state=1, max_days=1000):
    current_state = start_state
    path = [(0, None, current_state)]
    for day in range(1, max_days + 1):
        probs = transition_matrix[current_state - 1]
        rand_num = random.random()
        cum_prob = 0.0
        next_state = 1
        for i, prob in enumerate(probs):
            cum_prob += prob
            if rand_num < cum_prob:
                next_state = i + 1
                break
        current_state = next_state
        path.append((day, rand_num, current_state))
        if current_state == 4:
            break
    return path


states = {
    1: "Учится на очном отделении",
    2: "Переведен на заочное отделение",
    3: "В академическом отпуске",
    4: "Отчислен"
}

transition_matrix = [
    [0.7, 0.1, 0.1, 0.1],
    [0.2, 0.6, 0.1, 0.1],
    [0.5, 0.0, 0.5, 0.0],
    [0.0, 0.0, 0.0, 1.0]
]

results = []

for run in range(1, 11):
    print(f"\n--- Прогон #{run} ---")
    path = simulate_student_path()
    print_simulation_table(path)
    steps_to_S = path[-1][0]
    results.append(steps_to_S)

    if run == 1:
        days = [item[0] for item in path]
        state_numbers = [item[2] for item in path]
        plt.figure(figsize=(10, 6))
        plt.step(days, state_numbers, where='post', marker='o', linestyle='-', linewidth=2, markersize=6)
        plt.yticks(ticks=range(1, 5), labels=[states[i] for i in range(1, 5)])
        plt.xlabel('День')
        plt.ylabel('Состояние')
        plt.title('Временная диаграмма переходов студента (1-й прогон)')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

print("\n\nТаблица достижений Отчисления")
print("-" * 30)
print(f"{'Номер прогона':<15} {'Число шагов':<15}")
print("-" * 30)
for i, steps in enumerate(results, 1):
    print(f"{i:<15} {steps:<15}")

average_steps = sum(results) / len(results)
print(f"\nСреднее число дней до отчисления: {average_steps:.2f}")
