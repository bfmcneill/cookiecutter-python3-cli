tty:
	docker compose -f ./docker-compose.yml run --rm cli

clean:
	docker image rm $(docker image ls | grep new-py-proj | awk '{ print$3 }')

new: clean tty

