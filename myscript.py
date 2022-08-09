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

api_list=list()

regex_ip = re.compile( r'(\d{3}\.)([0]{1})')
#works for 192.168.0.100" and "127.0.0.1

regex_string_by_date_and_domain = re.compile(r'(\w([0-9]{2}.[0-9]{2}.[0-9]{4})).([\w.+-]+@[\w-]+\.[\w.-]+)')
#only string that contains date in dd.mm.yyyy format  AND normal domain format(sparrow@gmail.com)

def parser(filename):

    #парсим файл и добавляем в масив api_list
    with open(filename) as f:
        for line in f:
            if regex_ip.search(line):
                pass
            elif regex_string_by_date_and_domain.search(line):
                api_list.append("*****")
            else:
                api_list.append(line)
        
    
    #записываем масив в новый файл
    with open('parse_console.log','a') as f:
        for line in api_list:
            f.write(line+"\n")


if __name__=='__main__':
    parser('dir_with_log\seo.log')
    #name_time_parser('parse_console.log')



# import csv 
# import re

# intermediate_list=list()

# regex_email =re.compile( r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
# regex_number =re.compile( r'(\+380)')
# regex_website =re.compile( r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})')

# #encoding="utf8" because Python 3 opens your files with a default encoding that doesn't match the contents. 
# def fix():
#     """
#     change_data_set.csv - Includes all lines containing phone number or email or website
#     change_data_set2.csv - Includes all lines containing phone number, email and website
#     """

#     with open('dataset.csv',encoding="utf8") as f:
#         contents=csv.reader(f)
#         for row in contents:
#             for elem in row:
#                 if regex_number.search(elem) or regex_email.search(elem) or regex_website.search(elem):
#                     intermediate_list.append(row)


#     with open('change_data_set.csv','w',newline='',encoding="utf8") as f:
#         writer=csv.writer(f)
#         writer.writerows(intermediate_list)

# if __name__ == "__main__":
#     print(fix.__doc__)
#     fix()