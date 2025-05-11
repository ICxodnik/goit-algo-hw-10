import pulp

model = pulp.LpProblem("Production_Maximization", pulp.LpMaximize)

lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

model += lemonade + fruit_juice, "Total_Products"

model += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
model += lemonade <= 50, "Sugar"
model += lemonade <= 30, "Lemon_Juice"
model += 2 * fruit_juice <= 40, "Fruit_Puree"

model.solve()

print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Кількість лимонаду: {lemonade.varValue}")
print(f"Кількість фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість напоїв: {pulp.value(model.objective)}")
