#!/bin/bash

source venv/bin/activate  # Assuming your virtual environment is named 'venv'
site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
deactivate

for package in $(pip list | awk '{print $1}'); do
  location="$site_packages/$package"
  size=$(du -h "$location")
  echo "$package: $size"
done
