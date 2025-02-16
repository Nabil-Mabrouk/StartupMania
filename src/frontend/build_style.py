import os
import subprocess
import sys
from pathlib import Path

# how to use this script: python build_style.py theme1

# Paths
BASE_DIR = Path(__file__).resolve().parent
THEME_DIR = BASE_DIR / "themes"
TAILWIND_CONFIG = BASE_DIR / "tailwind.config.js"
INPUT_CSS = BASE_DIR / "static/css/input.css"
OUTPUT_CSS = BASE_DIR / "../startupmania/landing/static/landing/css/style.css"
NPM_PATH = r"C:\Program Files\nodejs\npm.cmd"
NPX_PATH = r"C:\Program Files\nodejs\npx.cmd"

def main():
    # Get the selected theme from command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python build_style.py <theme_name>")
        sys.exit(1)

    selected_theme = sys.argv[1]
    theme_config_path = THEME_DIR / f"{selected_theme}.js"

    # Check if the theme configuration exists
    if not theme_config_path.exists():
        print(f"Error: Theme '{selected_theme}' not found.")
        sys.exit(1)

    # Create a temporary tailwind.config.js file
    try:
        with open(TAILWIND_CONFIG, "w") as config_file:
            config_file.write(f"module.exports = require('{theme_config_path.as_posix()}');\n")

        # Run TailwindCSS CLI to compile the styles
        subprocess.run(
            [
                NPX_PATH,
                "tailwindcss",
                "-i",
                INPUT_CSS.as_posix(),
                "-o",
                OUTPUT_CSS.as_posix(),
            ],
            check=True,
            env=os.environ
        )
        print(f"Styles compiled successfully for theme: {selected_theme}")
    except subprocess.CalledProcessError as e:
        print(f"Error during TailwindCSS compilation: {e}")
    finally:
        # Cleanup the temporary tailwind.config.js file
        if TAILWIND_CONFIG.exists():
            TAILWIND_CONFIG.unlink()

if __name__ == "__main__":
    main()
