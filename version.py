import re
import sys

def get_current_version():
    with open('flask_metrics_visitors/__init__.py', 'r') as f:
        content = f.read()
        version_match = re.search(r"__version__ = ['\"]([^'\"]*)['\"]", content)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")

def update_version(version_type):
    current_version = get_current_version()
    major, minor, patch = map(int, current_version.split('.'))
    
    if version_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif version_type == 'minor':
        minor += 1
        patch = 0
    elif version_type == 'patch':
        patch += 1
    else:
        raise ValueError("Version type must be 'major', 'minor', or 'patch'")
    
    new_version = f"{major}.{minor}.{patch}"
    
    with open('flask_metrics_visitors/__init__.py', 'r') as f:
        content = f.read()
    
    content = re.sub(
        r"__version__ = ['\"]([^'\"]*)['\"]",
        f'__version__ = "{new_version}"',
        content
    )
    
    with open('flask_metrics_visitors/__init__.py', 'w') as f:
        f.write(content)
    
    return new_version

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ['major', 'minor', 'patch']:
        print("Usage: python version.py [major|minor|patch]")
        sys.exit(1)
    
    new_version = update_version(sys.argv[1])
    print(f"Version updated to: {new_version}") 