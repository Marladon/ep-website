from translator.translator import _

_software_friendly_names = {
    "documentation": _("Документация"),
    "driver": _("Драйвер"),
    "firmware": _("Прошивка"),
    "software": _("Софт")
}


def software_friendly_name(name: str) -> str:
    return _software_friendly_names.get(name, name)


version = _("Версия")
release_date = _("Дата выпуска")
size = _("Размер")
link = _("Ссылка")
download = _("Скачать")
