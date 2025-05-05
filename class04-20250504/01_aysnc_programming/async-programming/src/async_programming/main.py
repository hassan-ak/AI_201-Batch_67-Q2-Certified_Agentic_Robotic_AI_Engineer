import time
import random
import asyncio


# Simulate downloading a single file
def sync_download_file(file_name):
    print(f"Starting download: {file_name}")
    duration = random.randint(1, 5)
    time.sleep(duration)  # Blocking sleep
    print(f"Finished downloading: {file_name} in {duration} seconds")

# Main function
def sync_main():
    files = ['file1.zip', 'file2.mp4', 'file3.pdf', 'file4.jpg', 'file5.docx']
    
    for file in files:
        sync_download_file(file)
        

# Simulate downloading a single file
async def async_download_file(file_name):
    print(f"Starting download: {file_name}")
    duration = random.randint(1, 5)  # pretend it takes 1–5 seconds
    await asyncio.sleep(duration)
    print(f"Finished downloading: {file_name} in {duration} seconds")

# The main function to handle all downloads
async def async_main():
    files = ['file1.zip', 'file2.mp4', 'file3.pdf', 'file4.jpg', 'file5.docx']
    
    # Create a list of download tasks
    tasks = [async_download_file(file) for file in files]
    
    # Run all downloads at the same time
    await asyncio.gather(*tasks)

def run_async_main():
    asyncio.run(async_main())