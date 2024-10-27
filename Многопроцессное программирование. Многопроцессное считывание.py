import multiprocessing
import time

# ------------Многопроцессный--------------

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line.strip())  # Убираем перенос строки

if __name__ == '__main__':
    start_time = time.time()

    # Создание списка имен файлов
    filenames = [f'Files/file {number}.txt' for number in range(1, 5)]

    # Создаем процессы для чтения файлов
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end_time = time.time()
    print(f'{end_time - start_time:.6f} (многопроцессный)')

# -------------Линейный-------------

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line.strip())  # Убираем перенос строки

if __name__ == '__main__':
    start_time = time.time()

    # Создание списка имен файлов
    filenames = [f'Files/file {number}.txt' for number in range(1, 5)]

    # Чтение информации из файлов
    for filename in filenames:
        read_info(filename)

    end_time = time.time()
    print(f'{end_time - start_time:.6f} (линейный)')
