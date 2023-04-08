# То, что было выделено красным цветом в ТЗ
promo_id = 'promo_10'
cashback_value = 10
date_from = '28.06.2022'
date_to = '28.07.2022'

# Ссылки на страницы с файлами в формате xml
links = ['https://santehmark.ru/bitrix/catalog_export/export_turbo_nal_2.xml',
         'https://santehmark.ru/bitrix/catalog_export/export_sauny.xml',
         'https://santehmark.ru/bitrix/catalog_export/export_vanny.xml',
         # добавлять еще ссылки нужно тут. Каждая ссылка в кав
         ]

counter_file = 'offers_counter.txt'


xml_start = f'''<?xml version="1.0" ?>
<promo_info>
   <promos>
      <promo>
         <promo_id>{promo_id}</promo_id>
         <cashback>{cashback_value}</cashback>
         <date_from>{date_from}</date_from>
         <date_to>{date_to}</date_to>
      </promo>
   </promos>
   <offers>
'''

xml_end = '''
</offers>
</promo_info>
'''
