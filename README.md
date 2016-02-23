# Надо придумать название

Простой и человечный алертер для influxdb.

## Настройка

Заполните конфиг config.sh (есть пример config.sh.example)

## Метрики

Создайте метрику в папке metrics с названием series, которую мы хотим отслеживать, например:

	mkdir -p metrics
	cat > metrics/dieta.json << EOF
	{
		"alerts": {
			"to_my_mail": {
				"email": "user@example.com",
				"type": "email",
			}
		},
		"filter": "food='sosisochki'",
		"warning": "lambda value: value < 2",
		"error": "lambda value: value < 1",
		"db_name": "aleshenka"
	}
	EOF

## Запуск

Выполните:

	. export.sh
	python example.py
