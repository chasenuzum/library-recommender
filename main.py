import subprocess
import sys

def run_ingest():
    """Run the data collection ingest.py script."""
    try:
        subprocess.run(["python", "data_collection/ingest.py"], check=True)
        print("Ingest script completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error while running ingest.py: {e}")
        sys.exit(1)

def run_app():
    """Run the main app."""
    try:
        subprocess.run(["python", "app.py"], check=True)
        print("App script completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error while running app.py: {e}")
        sys.exit(1)

def main():
    """Main entry point for the application."""
    print("Starting data collection...")
    run_ingest()
    print("Starting main application...")
    run_app()

if __name__ == "__main__":
    main()