import os
from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class LabirintPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'
        super().__init__(web_driver, url)


# Локаторы для строки поиска
    LOCATOR_SEARCH_BAR = WebElement(id='search-field')
    LOCATOR_SEARCH_BAR_BTN = WebElement(class_name='b-header-b-search-e-btn')


# Локаторы тестов корзины
    # Локатор: Добавить в отложенное
    LOCATOR_LINK_POSTPONED = WebElement(class_name='fave')

    # Локатор счетчика отложено
    LOCATOR_COUNTER_POSTPONED = WebElement(css_selector='.b-header-b-personal-e-icon-count-m-putorder.basket-in-dreambox-a')

    # Локатор книги
    LOCATOR_BOOK_DEAD = WebElement(xpath='//img[@src="https://img4.labirint.ru/rc/6d6c66d9efe7891957aa3b979e308c60/'
                                         '363x561q80/books84/833976/cover.jpg?1637666730"]')
    # Кнопка: Добавить в корзину
    LOCATOR_BTN_ADD_TO_CART = WebElement(css_selector='.btn.btn-small.btn-primary.btn-buy')

    # Ссылка: Очистить корзину
    LOCATOR_LINC_CLEAR_TO_CART = WebElement(xpath='//a[@class="b-link-popup"]')

    # Ссылка: Восстановить удаленное
    LOCATOR_LINC_CLEAR_CART_BACK_UP = WebElement(css_selector='.b-link-popup.g-alttext-deepblue')

    # Локатор корзины
    LOCATOR_BTN_CART = WebElement(css_selector='.b-header-b-personal-e-list-item.have-dropdown.last-child')

    # Локатор счетчика корзины
    LOCATOR_COUNTER_CART = WebElement(css_selector='.b-header-b-personal-e-icon-count-m-cart.basket-in-cart-a')

    # Локатор пустой корзины
    LOCATOR_EMPTY_CART = WebElement(xpath='//span[@class="g-alttext-small g-alttext-grey g-alttext-head" and '
                                          'contains (text(), "Ваша корзина пуста. Почему?")]')


# Локаторы панели навигации в шапке сайта
    # Логотип Лабиринт
    LOCATOR_LOGO_LABIRINT = WebElement(class_name='b-header-b-logo-e-logo')

    # Верхняя панель навигации
    LOCATOR_UP_NAVIGATION_PANEL = WebElement(class_name='b-header-b-menu-e-list')

    # Ссылка: Доставка и оплата
    LOCATOR_DELIVERY_AND_PAYMENT = WebElement(xpath='//a[@href="/help/" and @class="b-header-b-sec-menu-e-link"]')

    # Ссылка: Сертификаты
    LOCATOR_CERTIFICATE_LINC = WebElement(xpath='//a[@href="/top/certificates/" and '
                                                '@class="b-header-b-sec-menu-e-link"]')
    # Ссылка: Рейтинги
    LOCATOR_RATING_LINC = WebElement(xpath='//a[@href="/rating/?id_genre=-1&nrd=1"]')

    # Ссылка: Новинки
    LOCATOR_NEWS_LINC = WebElement(xpath='//a[@href="/novelty/"]')

    # Ссылка: Скидки
    LOCATOR_SALE_LINC = WebElement(xpath='//a[@href="/sale/"]')

    # Ссылка телефонного номера
    LOCATOR_PHONE_NUMBER_LINC = WebElement(css_selector='.b-header-b-sec-menu-e-list-'
                                                        'item.have-dropdown.have-dropdown-clickable.analytics-click-js')
    # Кнопка вызова по телефону
    LOCATOR_PHONE_NUMBER_BTN = WebElement(xpath='//*[@id="_support_call_number"]/a')

    # Ссылка: Поддержка
    LOCATOR_SUPPORT_IN_FOOTER = WebElement(xpath='//a[@href="/support/" and @data-event-content="Поддержка"]')


# Локаторы иконок справа от строки поиска
    # Блок иконок
    LOCATOR_BLOCK_ICONS = WebElement(css_selector='.b-header-b-personal')

    # Иконка: Сообщения
    LOCATOR_ICON_MESSAGES = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.'
                                                    'have-dropdown-touchlink.top-link-main_notification')
    # Иконка: Мой лабиринт
    LOCATOR_ICON_MY_MAZE = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.'
                                                   'top-link-main_cabinet.js-b-autofade-wrap')
    # Иконка: Отложено
    LOCATOR_ICON_POSTPONED = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.top-link-main_putorder')

    # Кнопка сердечко Отложено
    LOCATOR_BTN_POSTPONED = WebElement(xpath='//a[@data-id_book="833976" and @data-hasqtip="4"]')

    # Локатор всплывающего окна сообщения
    LOCATOR_AUTH_WINDOW = WebElement(xpath='//div[@class="js-auth__title new-auth__title" and contains'
                                           ' (text(),"Полный доступ к Лабиринту")]')

# Локаторы блока видео
    LOCATOR_BLOCK_VIDEO = WebElement(xpath='//span[@onclick="return false;" and contains (text(),'
                                           ' "Буктрейлеры и видеорецензии недели")]')


# Локаторы всех элементов из поиска
    LOCATORS_SEARCH_BOOK_TITLE = ManyWebElements(css_selector='.product-title-link')
    LOCATORS_CERTIFICATE_TITLES = ManyWebElements(class_name='card-column')
    LOCATORS_RATING_BOOK_TITLE = ManyWebElements(css_selector='.product.need-watch')


# Локаторы номера страниц
    # Страница 6
    LOCATORS_PAGE_NUM_6 = WebElement(xpath='//a[@class="pagination-number__text" and @href="?stype=0&page=6"]')

