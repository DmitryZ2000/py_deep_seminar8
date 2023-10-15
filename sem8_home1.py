# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle

def my_func(my_dir_name: str, out_file_name_json, out_file_name_csv, out_file_pickle):
    my_dict = {}
    for dir_path, dir_name, file_name in os.walk(my_dir_name):
        my_dict[dir_path] =  []
        my_dict[dir_path].append(os.getcwd() + dir_path[1:])
        my_dict[dir_path].append('dir')
        my_dict[dir_path].append(fun_get_dir_size(dir_path))
        for file in file_name:
            my_dict[file] =  []
            file_path = os.getcwd() + dir_path[1:]
            my_dict[file].append(file_path)
            my_dict[file].append('file')
            file_path_2 = file_path + '/' + file

            my_dict[file].append(os.path.getsize(file_path_2))
    # print(my_dict)
    
    with (
        open(out_file_name_json, 'w+', encoding='utf-8') as f_json
        ):      
        json.dump(my_dict, f_json, indent =1, ensure_ascii=False)
    
    with (
        open(out_file_name_csv, 'w+', newline='', encoding='utf-8') as f_csv
        ):
        csv_write = csv.DictWriter(f_csv, fieldnames=['object', 'path', 'type', 'size'], \
                                    dialect='excel', quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        all_data = []
        for key, value in my_dict.items():
            new_dict = {}
            new_dict['object'] = key
            new_dict['path'] = value[0]
            new_dict['type'] = value[1]
            new_dict['size'] = value[2]
            all_data.append(new_dict)
        csv_write.writerows(all_data)
    
    with (
        open(out_file_pickle, 'wb') as f_pickle
        ):    
        pickle.dump(my_dict, f_pickle)
    
    return    

    
        

def fun_get_dir_size(my_dir_name):
    res = 0
    for dir_path, dir_name, file_name in os.walk(my_dir_name, topdown=False):
        res += sum(os.path.getsize(os.path.join(dir_path, f)) for f in file_name)
    return res


if __name__ == '__main__':
    my_func('.', 'my_file_home.json', 'my_file_home.csv', 'my_pickle_file.bin')
    fun_get_dir_size('.')