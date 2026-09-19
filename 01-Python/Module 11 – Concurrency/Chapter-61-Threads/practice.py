import threading
import time

def task():
    print("Downloading...")
    time.sleep(2)
    print("Download complete")

thread = threading.Thread(target=task)

thread.start()
thread.join()


print("Now processing the document!")

import threading
import time

def download(document):
    print(f"Downloading {document}...")
    time.sleep(2)
    print(f"{document} downloaded!")

threads = []

for document in ["Doc 1", "Doc 2", "Doc 3"]:
    thread = threading.Thread(
        target=download,
        args=(document,)
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All documents are ready!")

def download(document):
    print("Download starts")
    time.sleep(2)
    print("Download finished")
    
threads = []

for doc in ["Doc1", "Doc2", "Doc3"]:
    thread = threading.Thread(target=download, args=(doc,))
    threads.append(thread)

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
    
print("All documents are ready!")