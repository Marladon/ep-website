from dataclasses import dataclass
from functools import lru_cache
from typing import Optional
from translator.translator import _


@dataclass
class SoftwareCategory:
    name: str
    friendly_name: str
    icon: str
    description: Optional[str] = None


categories = (SoftwareCategory(name="documentation", friendly_name=_("Документация"), icon="doc.png",
                               description=_("Руководства пользователей, паспорт продукта и т.п.")),
              SoftwareCategory(name="datasheet", friendly_name=_("Брошюры"), icon="brochure.png",
                               description=_("Информация по продукту")),
              SoftwareCategory(name="driver", friendly_name=_("Драйвера для Windows"), icon="driver.png",
                               description=_("Для остальных операционных систем драйвер не нужен.")),
              SoftwareCategory(name="firmware", friendly_name=_("Прошивка"), icon="firmware.png",
                               description=_("Обновление прошивки осуществляется с помощью кроссплатформенного "
                                             "ПО EPCBoot (ссылка на скачивание на этой странице).")),
              SoftwareCategory(name="software", friendly_name=_("Софт"), icon="software.png",
                               description=_("Программное обеспечение для ПК для поиска неисправностей на печатных "
                                             "платах с использованием аналоговых сигнатурных анализаторов EyePoint."
                                             "Для работы ПО требуется Python 3.6.8 (win32) с набором необходимых "
                                             "библиотек, а также Распространяемые пакеты Microsoft Visual C++ для "
                                             "Visual Studio 2013 (win32). Их можно скачать на этой странице.")),
              SoftwareCategory(name="debugger", friendly_name=_("IVM debugger"), icon="software.png",
                               description=_("Кроссплатформенно ПО для отладки сигнатурных анализаторов "
                                             "EyePoint и его исходные коды. Данное ПО позволяет вручную вызывать "
                                             "команды управления через автоматически сгенерированный "
                                             "интерфейс на библиотеке Qt и видеть распарсенные структуры ответов "
                                             "устройства.")),
              SoftwareCategory(name="epcboot", friendly_name=_("EPCBoot"), icon="software.png",
                               description=_("Кроссплатформенное ПО для обновления прошивок сигнатурных анализаторов "
                                             "EyePoint и его исходные коды. "
                                             "Репозиторий EPCBoot на GitHub: https://github.com/EPC-MSU/EPCboot")),
              SoftwareCategory(name="image", friendly_name=_("Прошивка встроенного компьютера"), icon="software.png",
                               description=_("Образы встроенной операционной системы для устройств серии EyePoint S. "
                                             "Обновление образа осуществляется посредством записи на SD карту. "
                                             "Подробнее см. руководство пользователя. "
                                             "Для записи образа на SD карту в в ОС Windows можно использовать "
                                             "Win32 Disk Imager.")),
              SoftwareCategory(name="API", friendly_name=_("Документация по протоколу программного управления (API)"),
                               icon="software.png"),
              SoftwareCategory(name="supporting_software", friendly_name=_("Стороннее вспомогательное ПО"),
                               icon="software.png",
                               description=_("Дополнительное стороннее программное обеспечение, "
                                             "которое может потребоваться при работе с устройствами EyePoint.")),
              SoftwareCategory(name="library", friendly_name=_("Библиотека для программного управления"),
                               icon="software.png",
                               description=_("Кроссплатформенная библиотека для работы с измерителями ВАХ EyePoint. "
                                             "Библиотека написана на языке C, распространяется в виде бинарных "
                                             "файлов (win32, win64, debian) и в виде исходных кодов.")),
              SoftwareCategory(name="SDK", friendly_name=_("Набор для разработчика (SDK)"),
                               icon="software.png",
                               description=_("Включает в себя примеры управления устройством в исходных кодах "
                                             "для языков Си, С#, Python 3, а также биндинги для двух последних."))
              )


@lru_cache(maxsize=128)
def software_category_by_name(name: str) -> SoftwareCategory:
    for category in categories:
        if category.name == name:
            return category
    return SoftwareCategory(name=name, friendly_name=name, icon="software.png")


version = _("Версия")
release_date = _("Дата выпуска")
size = _("Размер")
link = _("Ссылка")
download = _("Скачать")
