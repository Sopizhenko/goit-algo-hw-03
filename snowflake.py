import turtle

def draw_koch_snowflake(level, length):
	# Функція для малювання однієї сторони сніжинки Коха
	def draw_koch_side(level, length):
		if level == 0:
			turtle.forward(length)
		else:
			draw_koch_side(level - 1, length / 3)
			turtle.left(60)
			draw_koch_side(level - 1, length / 3)
			turtle.right(120)
			draw_koch_side(level - 1, length / 3)
			turtle.left(60)
			draw_koch_side(level - 1, length / 3)

	# Малюємо три сторони сніжинки Коха для створення однієї гілки
	for _ in range(3):
		draw_koch_side(level, length)
		turtle.right(120)

def main():
	# Введення рівня рекурсії від користувача
	level = int(input("Enter the recursion level for Koch Snowflake: "))
	if level < 0:
		print("Recursion level must be a non-negative integer.")
		return

	# Ініціалізація вікна та черепахи
	turtle.speed(0)  # Налаштовуємо максимальну швидкість малювання
	turtle.penup()
	turtle.goto(-100, 100)
	turtle.pendown()

	# Малюємо сніжинку Коха
	draw_koch_snowflake(level, 300)

	# Завершуємо роботу
	turtle.done()

if __name__ == "__main__":
	main()
