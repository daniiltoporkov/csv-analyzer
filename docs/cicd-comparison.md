# Сравнение GitHub Actions и GitLab CI/CD

| Критерий | GitHub Actions | GitLab CI/CD |
|----------|---------------|--------------|
| Настройка | 1 файл в .github/workflows, готовые actions | 1 файл .gitlab-ci.yml, stages |
| Сложность | Низкая | Средняя |
| Скорость | ~30 сек | ~20 сек |
| Артефакты | upload-artifact | artifacts |
| Защита веток | Branch protection rules | Protected branches |
| SAST | CodeQL, Secret scanning | Встроено в Ultimate |
| Применимость (учебный) | Очень удобен, быстрый старт | Мощнее, но требует больше конфигурации |

Вывод: для учебного проекта GitHub Actions проще, GitLab CI/CD ближе к промышленной разработке.