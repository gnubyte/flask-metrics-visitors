#!/bin/bash

# Check for required dependencies
if ! python3 -c "import twine" &> /dev/null; then
    echo "Error: 'twine' package is not installed. Please run: pip install twine"
    exit 1
fi

# Check if version type is provided
if [ -z "$1" ]; then
    echo "Error: Version type not specified. Usage: ./build.sh [major|minor|patch]"
    exit 1
fi

# Update version
echo "Updating version..."
python3 version.py "$1"
if [ $? -ne 0 ]; then
    echo "Error: Failed to update version"
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