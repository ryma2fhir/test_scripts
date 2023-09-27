## {{page-title}}

This guides follows through the creation and checking of the UKCore Simplifier packages

### Prerequisites
Ensure that you have the following permissions:
- Simplifier Project – admin
- GitHub Repository – Either admin or part of the GitHub IOPs Development Team
- A non standard NHS machine (Virtual or Developers)

### Package Release

#### Prerequisites
Ensure the following has been checks have been completed:
-	All relevant Jira tickets are complete
-	Ensure all GitHub PR's are complete
-	Merge develop (hotfix) into relevant main (release)


#### Publishing a Package
Note that the following must be done within a virtual machine due to NHS firewall restrictions.

1.	Within the Simplifier Project reimport Github.
<br><br>
 {{render:igimport}}
 

2.	Within the same menu, check the GitHub repository settings. 
 
The Repository include/exclude textbox should be as the following:

```
#by default, everything is included 
#if some include statements are added, we will exclude everything by default 
#Simplifier imports only xml, json, images, css, yaml and markdown file types 

#Include examples: 
# FHIR/IG/** 
# *.xml 

#Exclude examples: 
# !FHIR/*.img 
# !*.cs 
# !FHIR/examples/* 

# Exclude all capability statement files: 
!CapabilityStatement/*
```
 

 
This ensures that the capability statement is not copied into the npm package.
If the textbox had to be updated open the file manager, search for “capability” and if there delete.
<br><br>
{{render:igfilemanager}}
<br><br>
{{render:igcapabilitystatement}}
 
--- 





### Creation of the NPM Package

1.	Create the new package for the relevant version
<br><br>
{{render:ignewpackage}}
<br><br>
2.	Enter the version number. This should be in the format of x.x.x(-aaa) where x denotes a number and (-aaa) denote an optional lowercase string. For example, 01.00.00-pre-release.
<br><br>
{{render:ignewpackageversion}}
<br><br>
For the release package the release notes should read
#### For the balloted release
```
This is a release of the FHIR assets for the x.x.x version of the UK Core.

**Please note: This npm package contains only the current active FHIR assets, and does not include retired assets, or ones in development which are not part of this formal release, and are therefore these are not in the associated Implementation Guide.**
```

#### For the non-balloted release
```
This is a release of the FHIR assets for the x.x.x version of the UK Core

**Please note: This npm package contains all current assets, including ones in devlopment which are not part of this formal release, and therefore theres are not in the associated Implementation Guide.**
```

3.	Within the content tab ensure the appropriate checkboxes are selected as below:
<br><br>
{{render:ignewpackageboxes}}
<br><br>
4.	Click Publish.
 <br><br>

The package has been created.

---

### Implementation Guide Release

#### Prerequisites
Once the package has been created the IG can be published. Within the IG editor:
1.	Click the hamburger. Click Settings
 <br><br>
 {{render:igsettings}}
 <br><br>
  a.	Add the title UK Core Implemetation Guide STUx Sequence, where x is the STU number. Add a description
  <br><br>
 {{render:igsettingstitle}}
 <br><br>

  b.	Change the scope to point to the newly created package and click save.
<br><Br>
 

2.	Select Edit Master Template.
 {{render:igmastertemplate}}

  a.	Comment out the blue banner information, lines 53 to 63, using
`<!-- [block of code] -->`
 {{render:igmastertemplatecomment}}

  b.	Update the details of the bottom banner, namely the Released date (line 113).
 

3.	Amend the Contact Us page 
  a.	Change the version on the first paragraph
  b.	Change the version for each email subject line to read
  c.	Subject=UK Core Release <version>"

 

4.	Amend the new package on the Downloads page
 



5.	Before publishing it is vital to check that:
  a.	All pages and links are rendered correctly
  b.	The IG has been run through spell-checking software
  c.	The IG has been run though a link checking software

---

#### Publishing a Guide

6.	Within the Guides portal select the burger bar next to the guide you want to publish and select versions.
<br><br>
{{render:igpublish}}
<br><br>

7.	Select the burger bar next to the version that you want publishing and select publish.

  a.	Enter the Version to that it aligns with the package version.
  b.	Ensure that:
- Status is set to Public
- Read-only is set to Read-only
-	Make default set to Yes 
<br><br>
{{render:igpublishversion}}
<br><br>
 
c. Select Publish

---
 
### Overwriting and Republishing a Guide
If there are any errors spotted after publishing the guide it is possible to overwrite and republish using the same version number.

1.	Within the Guides portal select the burger bar next to the guide you want to publish and select 'Make overwritable'.



2.	From the current burger bar select publish.
 <br><br>
 {{render:igoverwitepublish}}
 <br><br>
 

a.	Enter the same version number of the previous guide that you have just made overwritable. This may be different to the package version.
b.	Ensure that:
•	Status is set to Public
•	Read-only is set to Read-only
•	Make default set to Yes 
 
c. Select Publish.

---
 
### GitHub Release
Prequestites
1.	Download the Zip project
 <br><br>
{{render:IGZip}}
  <br><br>

2.	Unzip the downloaded file 
3.	Open Winrar and browse to .\hl7fhirukcorer4\guides
4.	Right-click on the newly publish guide and select ‘Add files to archive’ 
5.	Select within ‘Archive format’ the ‘ZIP’ button and select ‘OK’. This will zip the file into the current folder.
 

Creating a Release Within GitHub
6.	With the GiHub FHIR-R4-UKCORE-STAGING-MAIN repository. Select the Releases title on the right-hand side.
 <br><br>
{{render:IGGithubRelease}}
  <br><br>

7.	Select Draft a new release.
  
8.	Ensure target is set to main and create a tag the is the same as the package version.
 

9.	Add the following release notes, changing the information in <> as needed:
 


10.	Drag and drop the newly created zip file into the ‘Attach binary…’ area
 
11.	Set as latest release and publish.

---

Updating UK Core Publication (Version) History

1.	Within the GitHub release page right click on the zip file and ‘Copy Link’
 <br><br>
{{render:IGGithubZip}}
  <br><br>
2.	Edit the UK Core Publication (Version) History within Simplifier and add the following to the table.
 
---
 
### NHS IG Validation

Validating the NHS IG against the new package will help understand any ramifications when the package is officially released.
1.	Within the GiHub repository NHSDigital-FHIR-ImplementationGuide, create a new branch, use a similar name to the package.
  <br><br>
  {{render:ignhse}}
  <br><br>

2.	Within the new branch open the file named package.json
   <br><br>
  {{render:ignhsepackagejson}}
  <br><br>

3.	Under dependencies change the UKCore value to
 `"<package name>”: “<version name>”`
 For example, 
`"fhir.r4.ukcore.stu1": "1.0.0"`

4.	Commit changes
 

5.	By committing the change the validator will automatically run. Check the Actions tab to see if it validates. For each row the information given is status, commit message, branch name, when it was commits and how long the validator took to run.
Status:
  - An orange circle shows that it is still running, 
  - A green tick shows that it has successfully validated,
  - A red cross will mean that the valdation has failed. 
 

Clicking the action will give a summary of the validation. This will help understand why validation has failed.
  
Be aware that the fixes may not be UKCore specific but on the NHS side. A discussion may be needed to understand the implications and remedies.