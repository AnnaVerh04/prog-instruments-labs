import argparse
import logging

import file_operations
import func

from logger import configure_logging

configure_logging()

"""
Модуль для выполнения основной логики программы.

Данный модуль содержит функцию main, которая выполняет основную логику программы.
Программа считывает данные из JSON файла, строит график зависимости времени выполнения от количества процессов,
проверяет номера карт по алгоритму Луна и сохраняет правильные номера в другой JSON файл.
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--settings', help="Путь к json файлу с данными.", required=True)
    parser.add_argument('-i', '--plot_image', help="Сохранять ли изображения графики зависимостей.")
    parser.add_argument('-p', '--num_of_processes', help='Максимальное количество процессов.', type=int)
    parser.add_argument('-j', '--save_to_json', help='Путь к json файлу, куда сохранится номер карты.', required=True)
    args = parser.parse_args()

    logging.info("Чтение данных из файла: %s", args.settings)
    res = file_operations.read_json(args.settings)

    if args.plot_image == '1':
        args.plot_image = True
        logging.info("Изображения графиков будут сохранены.")
    else:
        args.plot_image = False
        logging.info("Изображения графиков не будут сохранены.")

    logging.info("Запуск функции get_plot с параметрами: hash=%s, bins_list=%s, last_symbols=%s, num_of_processes=%s",
                 res['hash'], res['bins_list'], res['last_symbols'], args.num_of_processes)

    card_numbers = func.get_plot(res['hash'], res['bins_list'], res['last_symbols'], args.num_of_processes,
                                 args.plot_image)

    for a in card_numbers:
        if not func.luna_alg_check_card_number(a):
            logging.warning("По алгоритму Луна номер карты %s неверный.", a)
        else:
            logging.info("По алгоритму Луна номер карты %s верный.", a)

    logging.info("Сохранение правильных номеров карт в файл: %s", args.save_to_json)
    file_operations.write_card_numbers_to_json(args.save_to_json, card_numbers)


if __name__ == '__main__':
    main()