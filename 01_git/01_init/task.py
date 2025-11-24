# 1. Вернулся в ветку main командой:
#    git switch main
#
# 2. Создал файл notes.txt:
#    touch notes.txt
#
# 3. Добавил файл в staging:
#    git add .
#
# 4. Сделал коммит:
#    git commit -m "Mini-practice file git movement"
#
# 5. Создал ветку experiment:
#    git branch experiment
#
# 6. Переключился в ветку experiment:
#    git switch experiment
#
# 7. Изменил содержимое notes.txt вручную в редакторе.
#
# 8. Попробовал вернуться в main:
#    git switch main
#    Git предупредил о несохранённых изменениях (M notes.txt).
#
# 9. Добавил изменения в main:
#    git add .
#
# 10. Сделал коммит в main:
#     git commit -m "Forget to add note"
#
# 11. Переключился обратно в experiment:
#     git switch experiment
#
# 12. Проверил статус и увидел, что версия notes.txt отличается от main:
#     git status