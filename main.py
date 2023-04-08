import utils as ut
import os


offers_and_feeds = []

# Скачиваем файлы по ссылкам
ut.get_files_xml()

# Проходим по всем скачанным файлам
# забираем значения id из каждого тэга offer
directory = 'xml_files'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        ut.get_values_from_xml(f, offers_and_feeds)


# проверяем есть ли изменения в фидах
if ut.check_counter(len(offers_and_feeds)):
    print('Генерация promos.xml')
    ut.generate_xml(offers_and_feeds)

else:
    print('Генерация promos.xml не требуется. Остановка скрипта')
    exit()

# Сохраняем в отдельном файле количество offer
ut.save_offers_counter(len(offers_and_feeds))
