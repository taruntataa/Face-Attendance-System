import argparse, subprocess, sys, os

SCRIPTS = {
    "train": "train.py",
    "recognize": "facerecog.py",
    "detect": "facedetec.py",
    "insert": "insert.py"
}

def run_script(name):
    script = SCRIPTS.get(name)
    if not script:
        print(f"Unknown script: {name}")
        return 1
    path = os.path.join(os.path.dirname(__file__), script)
    return subprocess.call([sys.executable, path])

def main():
    parser = argparse.ArgumentParser(description="Face Attendance project CLI")
    parser.add_argument("command", choices=list(SCRIPTS.keys()) + ["all"], help="Command to run")
    args = parser.parse_args()

    if args.command == "all":
        for cmd in ["train", "recognize"]:
            code = run_script(cmd)
            if code != 0:
                break
    else:
        run_script(args.command)

if __name__ == "__main__":
    main()
