# Central CLI or logic entry point if needed later

def route_command(command: str):
    if command == "monitor":
        from src.monitor.file_event_monitor import start_monitoring
        start_monitoring()
    elif command == "process":
        from src.fileflow.mover import run_full_pipeline
        run_full_pipeline()
    else:
        print(f"Unknown command: {command}")
# TODO
