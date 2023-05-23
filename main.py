# теорія
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename= "logs.log",
                    filemode= "w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
logging.debug("debug")
logging.info("info")
logging.error("error")
logging.warning("warning")
logging.critical("critical")
try:
    print(10/0)
except Exception:
    logging.exception('gg bro')
def factorial(n):
    logging.info(f"ропочато обчислення факторіала числа {n}")
    result = 1
    for i in range(1,n+1):
        result *= i
    logging.info(f'завершення обчислення факторіалу числа {n} езультат {result}')
    return result
logging.basicConfig(level=logging.INFO)
print(factorial(5))
