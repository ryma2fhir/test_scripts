import xml.etree.ElementTree as ET
import os

paths = ['structuredefinitions','valuesets','codesystems']
for path in paths:
    files = os.listdir('./'+path)
    print(path)
    for file in files:
        '''open file to find element values'''
        tree = ET.parse("./"+path+"/"+file)
        root = tree.getroot()
        
        '''do not check retired assets'''
        try:
            if root.findall('.//{*}'+str('status'))[0].get('value') == 'retired':
                break
        except:
            print("active",root.findall('.//{*}'+str('status'))[0].get('value'))
            pass
        
        '''Check files are in correct folder '''
        if path == 'structuredefinitions' and (file.endswith("Example.xml") or (not file.startswith('Extension') and not file.startswith('UKCore'))):
            print("\tThe file '"+file+"' has either an incorrect prefix or in the wrong folder '"+path+"'.")
            break
        if path == 'valuesets' and not file.startswith('ValueSet'):
            print("\tThe file '"+file+"' has either an incorrect prefix or in the wrong folder '"+path+"'.")
            break
        if path == 'codesystems' and not file.startswith('CodeSystem'):
            print("\tThe file '"+file+"' has either an incorrect prefix or in the wrong folder '"+path+"'.")
            break

        '''check for missing elements'''
        elements = {'ID':'id','url':'url','name':'name','title':'title'}
        for key,value in elements.items():
            try:
                elements[key]=(root.findall('.//{*}'+str(value))[0].get('value'))
                print(elements)
            except:
                print("\tThe element '"+key+"' is missing")
                break
            
                '''check elements naming convention are correct'''
        fileName = file.replace('.xml','')
        warnings = []
        if path == 'codesystems' or path == 'valuesets':
            fileName = '-'.join(fileName.split('-')[1:])
        if not fileName == elements['ID']:
            warnings.append("\t\tThe 'id' element: "+elements['ID']+" is incorrect")
        if not fileName == elements['url'].split('/')[-1]:
            if not elements['url'].startswith('http://hl7.org/fhir/5.0/'): #passes any R5 extensions
                warnings.append("\t\tThe 'url' element: "+elements['url']+" is incorrect")
        if not ''.join(fileName.split('-')) == elements['name'].split('/')[-1]:
            warnings.append("\t\tThe 'name' element: "+elements['name']+" is incorrect")
        if not fileName.replace('-','') == elements['title'].replace(' ',''):
            warnings.append("\t\tThe 'title' element: "+elements['title']+" is incorrect")
        if warnings:
            print("\t"+file)
            for x in warnings:
                print(x)
                
'''check example filenames'''
examplesPath = os.listdir('./examples')
print('examples')
for examples in examplesPath:
    if not examples.endswith("Example.xml"):
        print("\t",examples," - The filename is does not have the suffix 'Example'")
              
print("\n\nCheck Complete!")
    
        
