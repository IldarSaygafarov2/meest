from openpyxl import Workbook

fields = ['Трек номер', 'Ф.И.О', 'Серия паспорта', 'Номер паспорта', 'ПИНФЛ', 'Номер телефона']


def save_to_excel(filename, data):
    wb = Workbook()
    ws = wb.active

    for i in range(1, len(data) + 1):
        rows = ws[f'A{i}': f'F{i}']
        item = data[i-1]

        for row in rows:
            for idx, cell in enumerate(row):
                cell.value = item[idx]
            print('========')

    wb.save(filename)


