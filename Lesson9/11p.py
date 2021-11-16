def get_formatted_name (first_name, last_name):
 "" "full_name = f" {first_name} {last_name} "return full_name.title () while True: print (" \ nПожалуйста, скажите мне ваше имя: ")
 print ("(введите 'q' в любое время, чтобы выйти)")
 f_name = input ("Имя:") if f_name == 'q':
     break
    l_name = input ("Фамилия:")
    if l_name == ' q ':
        break
 formatted_name = get_formatted_name (f_name, l_name)
print (f "\ nHello, {formatted_name}!")
