.PHONY: all ui backend start_ui start_backend run_with_ollama run_without_ollama clean

UI_PORT = 5173
BACKEND_PORT = 5000


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

# Stop all the processes that were started
stop:
	@echo "Stopping UI and Backend..."
	@PID_UI=$$(lsof -t -i:$(UI_PORT)) && if [ ! -z "$$PID_UI" ]; then kill -9 $$PID_UI; else echo "No process running on port $(UI_PORT)"; fi
	@PID_BACKEND=$$(lsof -t -i:$(BACKEND_PORT)) && if [ ! -z "$$PID_BACKEND" ]; then kill -9 $$PID_BACKEND; else echo "No process running on port $(BACKEND_PORT)"; fi
	@PID_OLLAMA=$$(ps aux | grep 'ollama start' | grep -v grep | awk '{print $$2}') && if [ ! -z "$$PID_OLLAMA" ]; then kill -9 $$PID_OLLAMA; else echo "Ollama is not running"; fi
