import random
import logging
logging.basicConfig(filename='info.tx11',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
def generate_numbers(file_path, num_numbers):
    try:
        with open(file_path, "w") as file:
            for i in range(num_numbers):
                random_number = random.randint(1, 10)
                file.write(str(random_number) + '\n')
                logging.info(f"рандомне число: {random_number}")
    except Exception as e:
        logging.error(f"Error: {e}")
file_path = "numbers.txt"
num_numbers = 2
generate_numbers(file_path, num_numbers)






