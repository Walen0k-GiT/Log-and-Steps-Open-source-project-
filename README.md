# Log and Steps 🖥📊
___
## Ver 1.0.0
___
<div align="center">

Профессиональный просмотрщик системных логов Windows

Простота в использовании · Мощность в возможностях

🚀 Установка • 📖 Документация • 🎥 Демо
https://youtu.be/Q8f_Tf6Mlmk?si=icAbiUrhlpMPvODH
</div>

✨ Особенности

💡 Основные 🔧 Технические 🎯 Дополнительные
📊 Просмотр системных логов 🖥 Интеграция с Windows Event Log 💾 Экспорт в TXT
🛡 Логи безопасности ⚡ Мгновенная загрузка 🎨 Интуитивный интерфейс
📱 Логи приложений 🔒 Безопасность 📁 Авто-именование файлов

🎥 Демо

bash
# Запуск приложения
python main.py или 

🚀 Быстрый старт

📋 Требования

· ОС: Windows 10/11
· Python: 3.8+
· Права: Администратора (рекомендуется)

⚡ Установка

bash
# 1. Клонируйте репозиторий
git clone https://github.com/Walen0k-GiT/Log-and-Steps-Open-source-project-.git

# 2. Перейдите в папку проекта
cd log-and-steps

# 3. Запустите приложение
python main.py


Или просто скачайте и запустите:

bash
# Однострочный запуск
python -c "import urllib.request; urllib.request.urlretrieve('https://raw.githubusercontent.com/Walen0k/log-and-steps/main/main.py', 'main.py')" && python main.py


🛠 Использование

📊 Типы логов

Тип Описание Использование
System Системные события и ошибки Диагностика ОС
Application Логи приложений Отладка ПО
Security События безопасности Аудит безопасности

🎮 Кнопки управления

· 🔄 Load Logs - Загрузить последние 50 событий
· 🗑 Clear - Очистить поле просмотра
· 💾 Export - Сохранить логи в файл

📁 Пример экспорта

text
logs_20241219_143022.txt
├── Временная метка
├── Тип логов
├── Содержание событий
└── Форматирование


🏗 Архитектура

mermaid
graph TD
    A[GUI Tkinter] --> B[PowerShell Commands]
    B --> C[Windows Event Log]
    C --> D[Data Processing]
    D --> E[Display & Export]
    E --> F[Text File]


🔧 Технические детали

🖥 Компоненты

· Интерфейс: Tkinter (нативный Python)
· Логи: Windows Event Log via PowerShell
· Экспорт: Стандартные файловые операции
· Кодировка: UTF-8 / CP866

⚙ Команды PowerShell

powershell
# Системные логи
Get-EventLog -LogName System -Newest 50

# Логи приложений  
Get-EventLog -LogName Application -Newest 50

# Логи безопасности
Get-EventLog -LogName Security -Newest 50


📝 Примеры использования

🔍 Диагностика системы

python
# Автоматическая диагностика
1. Выберите 'System' логи
2. Нажмите 'Load Logs'
3. Ищите критические ошибки
4. Экспортируйте для анализа


🛡 Аудит безопасности

python
# Проверка безопасности
1. Выберите 'Security' логи  
2. Проанализируйте входы в систему
3. Проверьте попытки доступа
4. Сохраните отчет


🐛 Решение проблем

Проблема Решение
❌ "No Python interpreter" Установите Python с python.org
🔒 "Access denied" Запустите от имени администратора
📄 "No logs found" Проверьте службу "Журнал событий Windows"

🤝 Разработка

📦 Зависимости

python
# Только стандартные библиотеки
import tkinter      # GUI
import subprocess   # PowerShell
import datetime     # Временные метки

👨‍💻 Автор

<div align="">

### Walen0k 

</div>

---

<div align="center">

⭐ Если проект понравился - поставьте звезду!

"Простота - ключ к эффективности" 🗝

</div>
