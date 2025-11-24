# 1. Перешёл в папку задачи:
#    cd ~/Git_sandbox/Stage-3-Git/01_git/02_git_basics
#
# 2. Создал новый файл experiment.py и добавил строку:
#    print("first version")
#
# 3. Проверил статус:
#    git status
#    Git показал файл в статусе modified.
#
# 4. Посмотрел изменения в рабочей директории:
#    git diff
#    Git показал строку, добавленную к пустому файлу.
#
# 5. Добавил файл в staging:
#    git add .
#
# 6. Проверил staged-изменения:
#    git diff --staged
#    Git показал diff из staging области (зелёные строки).
#
# 7. Сделал коммит:
#    git commit -m "Add first version of experiment.py"
#
# 8. Посмотрел историю:
#    git log
#    Коммит появился в истории корректно.
#
# 9. Посмотрел детали нескольких коммитов:
#    git show
#    git show 33e52f6
#    git show 5ae8a45
#    Git показал содержимое каждого конкретного коммита.