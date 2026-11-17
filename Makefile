build:
	docker build -t devsnippet-vault .

run:
	docker run -d -p 5000:5000 --name devsnippet-vault-app devsnippet-vault

stop:
	docker stop devsnippet-vault-app && docker rm devsnippet-vault-app
