import os
import time

def delete_non_txt_files(directory_path):
    deleted_files_count = 0  # To count the number of deleted files
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if not file.endswith('.txt'):
                os.remove(os.path.join(root, file))
                deleted_files_count += 1
    return deleted_files_count

# Request the folder path from the user
directory_path = input('Enter the folder path: ')

start_time = time.time()  # Start time of the operation
deleted_files_count = delete_non_txt_files(directory_path)
end_time = time.time()  # End time of the operation

# Calculate the time taken and display the results
elapsed_time = end_time - start_time
print(f'Total files deleted: {deleted_files_count}')
print(f'Time taken: {elapsed_time:.2f} sec.')
input("Press enter to exit...")
