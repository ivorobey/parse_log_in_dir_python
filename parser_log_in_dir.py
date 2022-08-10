"""
Дано директорію з лог-файлами.
Потрібно зробити для них ротацію. При цьому врахувати, що access.log заповнюється швидше, 
ніж інші, тому його потрібно очищати кожні 15 хв, тоді як інші файли достатньо раз на день у нічний час.
У зазначений час, файли повинні архівуватися та, для аудиту, зберігати останні 10 версій. При цьому назва повинна містити дату створення архіву.
Перед архівуванням, у файлах слід:
прибрати рядки, що містять "192.168.0.100" або "127.0.0.1"
замінити підрядки формату "$md5hash_of_record-date$username", де record-date у форматі ddmmyyyy, а username — "2-3symbols@domain.name", на "*****"
"""
import re
import os
import time

api_list=list()


regex_ip = re.compile( r'(\d{3}\.)([0]{1})')
#works for 192.168.0.100" and "127.0.0.1
regex_string_by_date_and_domain = re.compile(r'(\w([0-9]{2}.[0-9]{2}.[0-9]{4})).([\w.+-]+@[\w-]+\.[\w.-]+)')
#only string that contains date in dd.mm.yyyy format  AND normal domain format(sparrow@gmail.com)



def parser(path):
    #process each file in the directory according to the given regular expressions
    for filename in os.listdir(path):
        if filename != "access.log":
            with open(os.path.join(path, filename), 'r') as f:
                for line in f:
                    if regex_ip.search(line):
                        pass
                    elif regex_string_by_date_and_domain.search(line):
                        api_list.append("*****")
                    else:
                        api_list.append(line)
            #write the processing result to a new file
            with open(f'new_+{filename}','a') as f:
                for line in api_list:
                    f.write(line+"\n")
            #clear the temporary list so as not to store the information of previous files       
            api_list.clear()
   


if __name__=='__main__':
    print(parser("dir_with_log"))  

    
    



