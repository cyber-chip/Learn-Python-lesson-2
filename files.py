with open('referat.txt', 'r', encoding='utf-8') as f:

    referat2 = open("referat2.txt", "w")
    
    for line in f:
        
        
        #Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
        print(len(line))
        #Результат записываем в файл 
        referat2.write(str(len(line))+ '\n')
        
        #Подсчитайте количество слов в тексте
        print(len(set(line.split())))
        #Результат записываем в файл 
        referat2.write(str(len(set(line.split())))+ '\n')
        
        #Замените точки в тексте на восклицательные знаки
        line = line.replace('.','!')
        print(line)
        #Результат записываем в файл 
        referat2.write(str(line)+ '\n')
#Закрываем файл
referat2.close()
