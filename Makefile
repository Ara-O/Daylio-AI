.PHONY: all ui backend start_ui start_backend run_with_ollama run_without_ollama clean

run_with_ollama: start_ui start_backend
	@echo "Starting Ollama..."
	ollama start &

all: start_ui start_backend

start_ui:
	@echo "Starting UI..."
	cd ui && make &

start_backend:
	@echo "Starting Backend..."
	cd backend && make &
