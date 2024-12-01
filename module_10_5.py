import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            all_data.append(line.strip())


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = datetime.datetime.now()
all_results = []
for name in filenames:
    result = read_info(name)
    all_results.append(result)
end = datetime.datetime.now()
print(end - start)

if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        all_results = pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)
