import threading
from time import sleep
import datetime
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count+1):
            sleep(0.1)
            f.write('Какое-то слово № '+str(i) + '\n')
        else:
            print('Завершилась запись в файл ' + file_name)

start = datetime.datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end = datetime.datetime.now()
print('Работа потоков ' + str(end - start))

start_1 = datetime.datetime.now()
threads = []
thread_args = [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]
for args in thread_args:
    t = threading.Thread(target=write_words, args=args)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_1 = datetime.datetime.now()

print('Работа потоков ' + str(end_1 - start_1))
