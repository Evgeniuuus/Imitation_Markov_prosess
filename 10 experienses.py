import random
import matplotlib.pyplot as plt


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

experiment_averages = []

for experiment in range(1, 11):
    print(f"\n=== Эксперимент #{experiment} ===")
    run_results = []

    for run in range(1, 11):
        path = simulate_student_path()
        steps_to_absorption = path[-1][0]
        run_results.append(steps_to_absorption)

    avg_steps = sum(run_results) / len(run_results)
    experiment_averages.append(avg_steps)

    print(f"Среднее число дней до отчисления (эксперимент #{experiment}): {avg_steps:.2f}")


plt.figure(figsize=(8, 5))
experiments = list(range(1, 11))
plt.plot(experiments, experiment_averages, marker='o', linestyle='-', color='tab:blue', linewidth=2, markersize=6)
plt.xlabel('Номер эксперимента')
plt.ylabel('Среднее число дней до отчисления')
plt.title('График изменения среднего числа шагов до отчисления ')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(experiments)
plt.tight_layout()
plt.show()


overall_mean = sum(experiment_averages) / len(experiment_averages)
print(f"\nОбщее среднее (по всем 10 экспериментам по 10 прогонов): {overall_mean:.2f}")