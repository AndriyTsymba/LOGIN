import logging
def write_file(fill_path , data):
    try:
        with open(fill_path , "w") as file:
            file.write(data)
    except Exception as e:
        pass
logging.basicConfig(level = logging.DEBUG ,
                    filename = "info.txt" ,
                    filemode = "w" ,
                    format = '%(asctime)s - %(levelname)s - %(message)s')
write_file("info.txt" , input("Введіть будь що і я запиш це в кремий файл:"))





