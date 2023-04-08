import vars
import requests
from requests.exceptions import HTTPError
from xml.dom import minidom


def get_files_xml():

    for url in vars.links:

        fname_index = url.rfind('/')
        fname = url[fname_index:]

        try:
            r = requests.get(url)
            r.encoding = 'utf-8'
            content = r.text
            r.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            print(f'Содержимое ссылки загружено: {url}')

        with open('xml_files' + fname, 'w', encoding="utf-8") as f:
            f.write(content)


def get_full_link(file_name):
    fname_index = file_name.rfind('/')
    fname = file_name[fname_index:]

    for link in vars.links:
        if fname in link:
            return link


def save_offers_counter(content):
    with open(vars.counter_file, 'w', encoding="utf-8") as f:
        f.write(str(content))


def check_counter(number):

    with open(vars.counter_file, 'r', encoding="utf-8") as f:
        rez = f.read()

    if (int(rez) == 0):
        print('Происходит первый запуск скрипта')
        return True
    elif (int(rez) == number):
        print('Изменений в фиде не обнаружено')
        return False
    else:
        print('Обнаружены изменения в фиде')
        return True


def get_values_from_xml(file_name, offers_and_feeds):

    mydoc = minidom.parse(file_name)
    items = mydoc.getElementsByTagName('offer')

    for elem in items:
        # print(elem.attributes['id'].value)
        offers_and_feeds.append(
            (elem.attributes['id'].value, get_full_link(file_name)))


def generate_xml(offers_and_feeds):
    content = vars.xml_start

    for id, url in offers_and_feeds:
        content += f'''
        <offer>
            <promo_id>{vars.promo_id}</promo_id>
            <offer_id>{id}</offer_id>
            <feed_url>{url}</feed_url>
        </offer>
        '''
    content += vars.xml_end

    with open('promos.xml', 'w', encoding="utf-8") as f:
        f.write(content)
