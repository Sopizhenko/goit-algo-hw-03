import json

def move_disk(n, source, target, auxiliary, state):
	if n == 1:
		# Якщо лише один диск, просто переміщаємо його зі стрижня source на стрижень target
		disk = state[source].pop()
		state[target].append(disk)
		print(f"Перемістити диск з {source} на {target}: {disk}")
		print(f"Проміжний стан: {json.dumps(state)}")
		return
	
	# Рекурсивно переміщаємо (n-1) дисків зі стрижня source на стрижень auxiliary,
	# використовуючи стрижень target як допоміжний
	move_disk(n - 1, source, auxiliary, target, state)
	
	# Переміщаємо найбільший диск зі стрижня source на стрижень target
	disk = state[source].pop()
	state[target].append(disk)
	print(f"Перемістити диск з {source} на {target}: {disk}")
	print(f"Проміжний стан: {json.dumps(state)}")
	
	# Рекурсивно переміщаємо (n-1) дисків зі стрижня auxiliary на стрижень target,
	# використовуючи стрижень source як допоміжний
	move_disk(n - 1, auxiliary, target, source, state)

def hanoi_towers(n):
	print(f"Початковий стан: {json.dumps({'A': list(range(n, 0, -1)), 'B': [], 'C': []})}")
	state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
	move_disk(n, 'A', 'C', 'B', state)
	print(f"Кінцевий стан: {state}")


def main():
	# Вхідне значення n - кількість дисків на стрижні A
	n = int(input("Введіть кількість дисків: "))
	
	# Викликаємо функцію для вирішення задачі Ханойських веж
	hanoi_towers(n)

if __name__ == "__main__":
	main()