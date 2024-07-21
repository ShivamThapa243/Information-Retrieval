import os
import preprocessing

directory_path = "text_files"
file_list = os.listdir(directory_path)

preprocessed_directory_path = "preprocessed_files"
os.makedirs(preprocessed_directory_path, exist_ok=True)

for filename in file_list:
    file_path = os.path.join(directory_path, filename)
    with open(file_path) as file:
        content = file.read()
        final_tokens = preprocessing.preprocessing_file(content)

    preprocessed_file_path = os.path.join(preprocessed_directory_path, f"preprocessed_{filename}")
    with open(preprocessed_file_path, 'w') as file:
        file.write(str(final_tokens))

# Printing contents of 5 sample files before and after performing each operation.
file_count = 0
for filename in file_list:
    if file_count >= 5:
        break

    file_path = os.path.join(directory_path, filename)
    with open(file_path) as file:
        content = file.read()
        print(f"Content of {filename} before preprocessing: ")
        print(content)
        print("Content of file after preprocessing:")
        print(preprocessing.preprocessing_file(content))
    print('\n')
    file_count += 1  