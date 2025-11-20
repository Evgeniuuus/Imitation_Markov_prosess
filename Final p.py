import random


def monte_carlo_simulation(num_steps=10000):
    current_state = 1

    state_counts = {1: 0, 2: 0, 3: 0, 4: 0}

    for _ in range(num_steps):
        state_counts[current_state] += 1

        rand = random.random()

        if current_state == 1:
            if rand < 0.7:
                current_state = 1
            elif rand < 0.7 + 0.1:
                current_state = 2
            elif rand < 0.7 + 0.1 + 0.1:
                current_state = 3
            else:
                current_state = 4

        elif current_state == 2:
            if rand < 0.2:
                current_state = 1
            elif rand < 0.2 + 0.6:
                current_state = 2
            elif rand < 0.2 + 0.6 + 0.1:
                current_state = 3
            else:
                current_state = 4

        elif current_state == 3:
            if rand < 0.5:
                current_state = 1
            elif rand < 0.5 + 0.0:
                current_state = 2
            elif rand < 0.5 + 0.0 + 0.5:
                current_state = 3
            else:
                current_state = 4

        elif current_state == 4:
            current_state = 4

    final_probabilities = {
        state: count / num_steps for state, count in state_counts.items()
    }

    return final_probabilities


probabilities = monte_carlo_simulation(10000)

print("Финальные вероятности состояний (метод Монте-Карло):")
for state in sorted(probabilities.keys()):
    print(f"Состояние {state}: {probabilities[state]:.6f}")
