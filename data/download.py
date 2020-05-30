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
                               description=_("Документация к продукту")),
              SoftwareCategory(name="driver", friendly_name=_("Драйвер"), icon="driver.png",
                               description=_("Драйвера для разных операционных систем")),
              SoftwareCategory(name="firmware", friendly_name=_("Прошивка"), icon="firmware.png",
                               description=_("Файлы прошивок для загрузки в устройство")),
              SoftwareCategory(name="software", friendly_name=_("Софт"), icon="software.png",
                               description=_("Программное обеспечение для ПК")))


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
