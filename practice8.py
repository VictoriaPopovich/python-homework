def copy_contact(from_f, to_f):
    with open(from_f, 'r', encoding='UTF-8') as from_file:
        list_contacts = from_file.read().rstrip().split('\n')
        num_contacts = list(enumerate(list_contacts, 1))
        print(num_contacts)
        line_num = int(input('Enter a line number to copy:'))
        to_add = num_contacts[line_num-1]  # это кортеж, из котороого копируем.
                                            #нумерация строк в файле и в кортеже расходится на 1, поэтому корректируем
        print (to_add)

            
        with open(to_f, 'a', encoding='UTF-8') as to_file:
            to_file.writelines('\n')
            to_file.writelines(to_add[1]) #записываем только элемент кортежа с индексом 1
            


#copy_contact('file2.txt', 'file.txt')