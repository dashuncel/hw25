import os
import subprocess
import time

src_dir = os.path.join(os.path.dirname(__file__), 'Source')
file_list = [f for f in os.listdir(src_dir) if f.endswith('.jpg')]
file_list = list(map(lambda f: os.path.join(src_dir, f), file_list))
process = list('' for x in range(4))

dest_dir = os.path.join(os.path.dirname(__file__), 'Result')
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

for i, file in enumerate(file_list):
    idx = i % len(process) # индекс процесса, куда распределяем картинку
    if type(process[idx]) == subprocess.Popen:
        while process[idx].poll() is None:
            print("Process %s still working..." % idx)
            time.sleep(5)

    process[idx] = subprocess.Popen('convert {} -resize 200 {}'.format(file, os.path.join(dest_dir, os.path.basename(file))),
                                                  stdout=subprocess.PIPE,
                                                  stderr=subprocess.PIPE)


