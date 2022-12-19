# Workflow for publishing a new version

1. Install Python requirements
    ```
    pip3 install --user -r requirements.txt
    ```
1. Run the Python script 
    ```
    python3 scripts/convert_json_to_table.py
    ```
1. Do git work
    ```
    git add 
    git commit -m "Text goes here"
    git push
    git tag -a X.Y.Z -m "X.Y.Z - Text goes here"
    git push origin X.Y.Z
    ```