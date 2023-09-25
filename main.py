import os, glob

files_path = os.getcwd()
txt_files = glob.glob(files_path + "/*.txt")

def file_result(file_path):
    file_data = open(file_path)
    lines = 0
    result_string = ""
    read_file_data = file_data.read()
    lines += read_file_data.count("\n")
    filename = os.path.basename(file_path)
    result_string += filename + "\n"
    result_string += str(lines) + "\n"
    result_string += read_file_data
    return [lines, result_string]

result = ""
all_texts = {}
for file in txt_files:
    line, text = file_result(file)
    all_texts[line] = text

sorted_keys = sorted(all_texts)
for key in sorted_keys:
    result += all_texts[key] + "\n"

print(result)



