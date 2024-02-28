#!/bin/bash

# Function to recursively search for JSON files in subdirectories
function post_json_files {
    local dir=$1
    local files=($(find "$dir" -mindepth 2 -type f -name "*.json"))
    for file in "${files[@]}"; do
        # Post the JSON file to the server
        response=$(curl -s -o /dev/null -w "%{http_code}" -X POST \
            -H "accept: application/fhir+json" \
            -H "Content-Type: application/fhir+json" \
            -d "@$file" \
            https://3cdzg7kbj4.execute-api.eu-west-2.amazonaws.com/poc/Conformance/FHIR/R4/\$validate)
        
        if [[ $response -eq 200 ]]; then
            echo "File $file posted successfully."
        else
            echo "File $file failed to post. Response code: $response"
        fi
    done
}

# Call the function for the current directory and all subdirectories
post_json_files .
