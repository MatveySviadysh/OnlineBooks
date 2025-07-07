IMAGE_NAME=telegram-bot

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm --env-file .env $(IMAGE_NAME)
