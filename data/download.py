from dataclasses import dataclass
from functools import lru_cache
from translator.translator import _


@dataclass
class SoftwareCategory:
    name: str
    friendly_name: str
    # description: str
    icon: str


categories = (SoftwareCategory(name="documentation", friendly_name=_("Документация"), icon="doc.png"),
              SoftwareCategory(name="driver", friendly_name=_("Драйвер"), icon="driver.png"),
              SoftwareCategory(name="firmware", friendly_name=_("Прошивка"), icon="firmware.png"),
              SoftwareCategory(name="software", friendly_name=_("Софт"), icon="software.png"))


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
