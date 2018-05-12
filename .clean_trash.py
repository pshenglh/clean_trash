import os
import time
import shutil

TRASH_DIR = './.trash'
INTERVAL = 14 * 24 * 3600
CURRENT_TIME = time.time()

def clean():
    files = os.listdir(TRASH_DIR)
    for f in files:
        file_path = os.path.join(TRASH_DIR, f)
        mtime = os.path.getmtime(file_path)
        ctime = os.path.getctime(file_path)

        if CURRENT_TIME - mtime > INTERVAL:
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                shutil.rmtree(file_path)
            print time.strftime("%Y-%m-%d %H:%M:%S", CURRENT_TIME), 'remove file or dir: ', f

if __name__ == '__main__':
    clean()
