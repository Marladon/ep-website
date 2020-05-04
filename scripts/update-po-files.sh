pygettext3 -d en -o locale/en_US/LC_MESSAGES/en.pot data/*.py
msgmerge locale/en_US/LC_MESSAGES/en.po locale/en_US/LC_MESSAGES/en.pot --update