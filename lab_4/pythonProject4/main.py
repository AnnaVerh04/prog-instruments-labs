import argparse
import func
import file_operations

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
    parser.add_argument('-p', '--num_of_processes', help='Максимальное количество процессов.')
    parser.add_argument('-j', '--save_to_json', help='Путь к json файлу, куда сохранится номер карты.', required=True)
    args = parser.parse_args()
    res = file_operations.read_json(args.settings)
    if args.plot_image == '1':
        args.plot_image = '1'
    else:
        args.plot_image = False
    card_numbers = func.get_plot(res['hash'], res['bins_list'], res['last_symbols'], args.num_of_processes,
                                 args.plot_image)
    for a in card_numbers:
        if not func.luna_alg_check_card_number(a):
            print(f'По алгоритму Луна номер карты {a} неверный.')
        if func.luna_alg_check_card_number(a):
            print(f'По алгоритму Луна номер карты {a} верный.')
    file_operations.write_card_numbers_to_json(args.save_to_json, card_numbers)


if __name__ == '__main__':
    main()
