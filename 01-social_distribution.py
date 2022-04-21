population = list(map(int, input().split(', ')))
minimum_wealth = int(input())

while True:
    poorest = population.index(min(population))
    wealthiest = population.index(max(population))
    diff = minimum_wealth - population[poorest]
    if population[wealthiest] == minimum_wealth or population[poorest] == minimum_wealth:
        break
    if population[wealthiest] - diff >= minimum_wealth:
        population[wealthiest] -= diff
        population[poorest] = minimum_wealth
    else:
        population[poorest] += population[wealthiest] - minimum_wealth
        population[wealthiest] = minimum_wealth

if min(population) == minimum_wealth:
    print(population)
else:
    print('No equal distribution possible')
