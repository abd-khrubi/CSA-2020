from constraint import *

names = ['Noether', 'Germain', 'Lovelace', 'Franklin', 'Curie']
pets = ['cat', 'dog', 'fish', 'rabbit', 'X']
food = ['burger', 'soup', 'chicken', 'salad', 'cake']
travel = ['foot', 'boat', 'train', 'bus', 'plane']
items = ['scales', 'abacus', 'pencil', 'telescope', 'laptop']

problem = Problem()

criteria = names + pets + food + travel + items
problem.addVariables(criteria, [1, 2, 3, 4, 5])

problem.addConstraint(AllDifferentConstraint(), names)
problem.addConstraint(AllDifferentConstraint(), pets)
problem.addConstraint(AllDifferentConstraint(), food)
problem.addConstraint(AllDifferentConstraint(), travel)
problem.addConstraint(AllDifferentConstraint(), items)

# Constraints
problem.addConstraint(lambda a, b: a == b, ['Noether', 'foot'])
problem.addConstraint(InSetConstraint({1}), ['Germain'])
problem.addConstraint(lambda a, b: abs(a - b) == 1, ['Germain', 'boat'])
problem.addConstraint(lambda a, b: a > b, ['plane', 'train'])
problem.addConstraint(lambda a, b: a == b, ['burger', 'train'])
problem.addConstraint(lambda a, b: a == b, ['bus', 'rabbit'])
problem.addConstraint(lambda a, b: abs(a - b) == 1, ['laptop', 'rabbit'])
problem.addConstraint(lambda a, b: a == b, ['Lovelace', 'pencil'])
problem.addConstraint(lambda a, b: a == b, ['dog', 'scales'])
problem.addConstraint(lambda a, b: abs(a - b) == 1, ['abacus', 'cat'])
problem.addConstraint(lambda a, b: a == b, ['abacus', 'soup'])
problem.addConstraint(lambda a, b: a == b, ['Franklin', 'salad'])
problem.addConstraint(lambda a, b: a == b, ['fish', 'cake'])
problem.addConstraint(InSetConstraint({3}), ['chicken'])
problem.addConstraint(lambda a, b: a == b, ['Curie', 'fish'])


def get_type(x):
	if x in names:
		return 'name'
	if x in pets:
		return 'pet'
	if x in food:
		return 'food'
	if x in travel:
		return 'travel'
	if x in items:
		return 'item'


def get_sol(sol):
	women = {i: {'name': '', 'pet': '', 'food': '', 'travel': '', 'item': ''} for i in range(1, 6)}
	for var in sol:
		i = sol[var]
		women[i][get_type(var)] = var
	return women


def format_sol(sol):
	s = []
	for i in range(1, 6):
		s.append(sol[i]['name'])
		s.append(sol[i]['item'])
	return ' '.join(s)


def main():
	solutions = problem.getSolutions()

	print(f'Found {len(solutions)} possible solutions')

	women = {i: {"name": set(), "pet": set(), "food": set(), "travel": set(), "item": set()} for i in range(1, 6)}

	for solution in solutions:
		sol = get_sol(solution)
		for i in range(1, 6):
			for t in sol[i]:
				women[i][t].add(sol[i][t])
		print(format_sol(sol))


if __name__ == '__main__':
	main()
