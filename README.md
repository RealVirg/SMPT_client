# SMPT_server
Запуск: smtp.py.
Первая строка config.txt - адреса на которые отправляются сообщения(через пробелы).
Вторая строка config.txt - тема сообщения.
Третья строка config.txt - названия фаилов находящихся в папке attach, которые нужно прикрепить к письму(через пробелы).
Содержимое фаила text.txt будет отправлено в виде самого письма.
Папка Attach должна содержать все фаилы, которые будут перечислены в третьей строке config.txt.


Пример config.txt:

1todomain@todomain.com 2todomain@todomain.com 3todomain@todomain.com

Test_Subject

image_test_1.png image_test_2.png image_test_3.png test_text_1.txt test_text_2.txt

Пример text.txt:
Test_Text

По указаному примеру будут отправлены письма по адресам: 1todomain@todomain.com, 2todomain@todomain.com, 3todomain@todomain.com, с темой: Test_Subject, с сообщением: Test_Text, c прикрепленными фаилами: image_test_1.png, image_test_2.png, image_test_3.png, test_text_1.txt, test_text_2.txt.
Автор: Исаков Юрий КН-201(МЕН-280206)
