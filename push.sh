#!/bin/bash

# Upload to PyPI
python3 -m twine upload dist/*

echo "Package uploaded to PyPI successfully!" 