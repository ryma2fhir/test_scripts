# xml to json

Copy xml_to_json.sh & validate_json_files.sh to the top repo dir.
run `find . -type f -name "*.xml" -exec basename {} .xml \; | sort > xml_filenames.txt` to find and save all xml filenames
Using Linux:
- run xml_to_json.sh using `chmod +x xml_to_json.sh` & `./xml_to_json.sh`
- run validate_json_files.sh using `chmod +x validate_json_files.sh` & `./validate_json_files.sh`
run `find . -type f -name "*.json" -exec basename {} .json \; | sort > json_filenames.txt` to find and save all json filenames
run `find . -type f -name "*.xml" -exec basename {} .xml \; | sort > xml_filenames.txt` to find the differences between the two filenames. If no FHIR assets are shown then all files have been cnverted and validated succussfully


