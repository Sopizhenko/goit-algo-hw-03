import os
import shutil
import argparse

def copy_files(source_dir, dest_dir):
	# Перевірка, чи існує директорія призначення, інакше створимо її
	if not os.path.exists(dest_dir):
		os.makedirs(dest_dir)

	# Читання вмісту вихідної директорії
	for item in os.listdir(source_dir):
		item_path = os.path.join(source_dir, item)

		if os.path.isdir(item_path):
			# Рекурсивно копіюємо вміст директорій
			copy_files(item_path, dest_dir)
		elif os.path.isfile(item_path):
			# Отримуємо розширення файлу
			_, extension = os.path.splitext(item)

			# Створюємо піддиректорію на основі розширення
			sub_dir = os.path.join(dest_dir, extension[1:])  # Виключаємо крапку з розширення

			if not os.path.exists(sub_dir):
				os.makedirs(sub_dir)

			# Копіюємо файл у відповідну піддиректорію
			shutil.copy2(item_path, sub_dir)

def main():
	# Парсинг аргументів командного рядка
	parser = argparse.ArgumentParser(description='Recursive file copy and sorting utility')
	parser.add_argument('source_dir')
	parser.add_argument('dest_dir')
	args = parser.parse_args()

	source_dir = args.source_dir
	dest_dir = args.dest_dir

	try:
		copy_files(source_dir, dest_dir)
		print(f'Files copied and sorted successfully from {source_dir} to {dest_dir}.')
	except Exception as e:
		print(f'An error occurred: {e}')

if __name__ == "__main__":
	main()
