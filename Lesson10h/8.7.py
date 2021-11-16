def make_album(singer_name,*nazvanie):
    
    print(f"Исполнитель : {singer_name.title()}, альбом:")
    for i in nazvanie:
        print(f"- {i.title()}")
        
singer = str(input('Введите певца:'))
album = str(input('Введите альбом:'))
make_album(singer, album)
