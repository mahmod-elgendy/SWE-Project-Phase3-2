#!/usr/bin/env python
import os
import sys

# Add the 'src' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Debugging - Print sys.path to ensure src is included
print("Sys Path:", sys.path)

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CampusLink.settings")  # Point to the settings module in campuslink

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import CampusLink.settings
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH?"
            )
        raise
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
