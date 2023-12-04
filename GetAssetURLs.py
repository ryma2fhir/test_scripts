'''Retrieves all asset urls from a file named File.txt. This file is created using the bash command
find . -name "*.xml" > File.txt
'''
import xml.etree.ElementTree as ET

def GetURLs()
    AssetsList = []
    allAssets= open("File.txt")
    for asset in allAssets:
        '''open file to find element values'''
        try:
            tree = ET.parse(asset.rstrip())
        except ET.ParseError as e:
            print("\t",file,"- The XML code has an error that needs to be fixed before it can be checked:",e)
            error=True
            continue

        root = tree.getroot()
        AssetsLisroot.findall('.//{*}'+'url')[0].get('value'))