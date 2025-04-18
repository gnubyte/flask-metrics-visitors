#!/bin/bash

# Check for required dependencies
if ! python3 -c "import twine" &> /dev/null; then
    echo "Error: 'twine' package is not installed. Please run: pip install twine"
    exit 1
fi

# Clean up any previous builds
rm -rf dist/ build/ *.egg-info/

# Build the package
python3 setup.py sdist bdist_wheel

if [ $? -eq 0 ]; then
    echo "Package built successfully!"
else
    echo "Error: Package build failed"
    exit 1
fi 