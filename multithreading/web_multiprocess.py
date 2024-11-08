import multiprocessing
import time
def download_file(file_url):
    print(f"Downloading file from {file_url}")
    time.sleep(10)
    print(f"Finished downloading {file_url}")

if __name__ == "__main__":
    urls = ["https://dev.to/lambdatest/web-scraping-with-python-tutorial-a-complete-guide-with-examples-34d8" , "https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/"]
    
    processes = []
    for url in urls:
        p = multiprocessing.Process(target=download_file, args=(url,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()  # Ensure all processes complete


