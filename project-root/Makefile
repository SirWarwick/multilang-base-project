build:
	cd rust/rustlib && cargo build
	cd backend/go-api && go build -o go-api
	cd backend/python-service && echo "Python handled via Flask dev"
	cd frontend/react-app && npm install

run:
	docker compose -f docker/docker-compose.yml up --build