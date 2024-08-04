import xlwt
from datetime import datetime
import os

async def export_users_to_excel(users):
    """
    Экспорт данных пользователей в Excel файл.

    :param users: Список пользователей для экспорта.
    :return: Путь к созданному Excel файлу.
    """
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Список пользователей")
    
    headers = ["ID", "Username", "First Name", "Last Name", "User Photo ID", 
               "Registration Date", "Is Admin", "Is Blocked", "Blocked the Bot"]
    
    for col_num, header in enumerate(headers):
        sheet.write(0, col_num, header)
    
    for row_num, user in enumerate(users, start=1):
        sheet.write(row_num, 0, user['user_id'])
        sheet.write(row_num, 1, user.get('username', ''))
        sheet.write(row_num, 2, user['first_name'])
        sheet.write(row_num, 3, user.get('last_name', ''))
        sheet.write(row_num, 4, user.get('user_photo_id', ''))
        sheet.write(row_num, 5, str(user['registration_date']))
        sheet.write(row_num, 6, user['is_admin'])
        sheet.write(row_num, 7, user['is_blocked'])
        sheet.write(row_num, 8, user['blocked_the_bot'])
    
    filename = f"user_list_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xls"
    workbook.save(filename)
    return filename

async def remove_excel_file(filename):
    """
    Удаление Excel файла после отправки.

    :param filename: Имя файла для удаления.
    """
    try:
        os.remove(filename)
        print(f"File {filename} has been removed successfully")
    except OSError as e:
        print(f"Error occurred while deleting file {filename}: {e}")