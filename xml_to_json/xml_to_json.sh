#!/bin/bash

# Function to recursively search for XML files
function post_xml_files {
    local dir=$1
    local files=($(find "$dir" -type f -name "*.xml"))
    for file in "${files[@]}"; do
        # Post the XML file to the server and save the response as JSON
        curl -X 'POST' \
        'https://3cdzg7kbj4.execute-api.eu-west-2.amazonaws.com/poc/Conformance/FHIR/R4/$convert' \
        -H 'accept: application/fhir+json' \
        -H 'Content-Type: application/fhir+xml' \
        -d @"$file" -o "${file%.xml}.json"
        echo "File $file posted and response saved as ${file%.xml}.json"
        
        # Delete the XML file after successful post
        rm "$file"
        echo "File $file deleted"
    done
}

# Call the function for the current directory and all subdirectories
post_xml_files .




