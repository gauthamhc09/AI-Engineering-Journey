import os
import time
from multiprocessing import Pool

# 1. Define the worker function that will run on separate CPU cores
def process_data(item):
    """
    This function runs independently on a separate CPU core.
    Put your heavy math, image processing, or data cleaning logic here.
    """
    # Simulating a heavy task that takes 1 second
    time.sleep(1)
    
    # Example computation
    result = item * 2
    return result

# 2. The main gatekeeper block (MANDATORY for multiprocessing)
if __name__ == "__main__":
    # Detect available CPU cores automatically
    total_cores = os.cpu_count()
    print(f"🚀 Starting processing using all {total_cores} available CPU cores...")
    
    # Create sample data to process (e.g., 16 items)
    data_list = list(range(1, 17))
    
    start_time = time.time()
    
    # 3. Open the Pool. It automatically defaults to the total core count.
    # The 'with' statement ensures the pool closes safely even if errors happen.
    with Pool() as pool:
        # pool.map automatically splits data_list and distributes it to the cores
        results = pool.map(process_data, data_list)
        
    end_time = time.time()
    
    # 4. Display results
    print("\n✅ Processing Complete!")
    print(f"Original Input: {data_list}")
    print(f"Parallel Output: {results}")
    print(f"⏱️ Total Execution Time: {end_time - start_time:.2f} seconds")
