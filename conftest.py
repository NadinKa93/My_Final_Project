
import pytest
import allure
import uuid


@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')

    return chrome_options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Эта функция помогает определить, что какой-то тест не прошёл и передать эту информацию:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def web_browser(request, selenium):

    browser = selenium
    browser.set_window_size(1600, 1000)

    # Вернуть экзепляр браузера в тестовый пример:
    yield browser

    # Этот код будет выполняться после каждого теста:

    if request.node.rep_call.failed:
        # Сделать снимок экрана, если тест не пройден:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Сделать снимок экрана для локальной:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # Прикрепить скриншот к отчёту:
            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)

            # Для успешной отладки:
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass # игнорировать любые ошибки здесь


def get_test_case_docstring(item):
    """ Данная функция получает строку документа из тестового примера и форматирует её,
        чтобы показывать эту строку документа вместо имени тестового примера в отчётах.
    """

    full_name = ''

    if item._obj.__doc__:
        # Удалить лишние пробелы из строки документа:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Сгенерировать список параметров для параметризованных тестовых случаев:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Создать список на основе словаря:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Добавить словарь со всеми параметрами к имени теста:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ Данная функция изменяет имена тестовых случаев "on the fly" во время выполнения тест-кейсов.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ Данная функция изменяла имена тестовых случаев "on the fly",
        когда мы используем параметр --collect-only для pytest
        (чтобы получить полный список всех существующих тестов).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # Если в тестовом примере есть строка документа, нужно изменить её имя
            # это строка документа для отображения читаемых отчётов и
            # для автоматического импортирования тестовых случаев в систему управления тестированием.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Выполнено!')
