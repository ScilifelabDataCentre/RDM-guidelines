---
title: Tutorial ENA submission
category: Other
toc: True
---

# Tutorial ENA submission

The aim of this tutorial is to provide guidance through the process of submitting genomics data to the <a href="https://https://www.ebi.ac.uk/ena/" target="_blank">European Nucleotide Archive</a> (ENA). By the end of this turorial you will:
* Understand the terminology used by ENA.
* Know how to properly describe and format your genomics data for submission.
* Know how to do a submission.
* Know where to get help for future submissions.

## Preparations
### Obtaining an ENA Webin Account

In order to do a submission, you need an account in ENA. To create an account, please go to the [ENA submission homepage](https://www.ebi.ac.uk/ena/submit/webin/), click on **Register**, and fill in the required details.

*Login page on the ENA submission homepage:*

<br>

<div class="text-center">
  <img src="/img/ena_tutorial/ENA_login_startpage.png" height="350" class="rounded">
</div>

<br>

*Enter account details to obtain an account in ENA:*

<br>

<div class="text-center">
  <img src="/img/ena_tutorial/ENA_login_detailspage.png" height="500" class="rounded">
</div>

<br>

Once you have filled in all of the required fields, you can log in to the submission service. You may wish to add contacts if you are working with other people to complete your submission. You can do this by logging into your account then selecting *Home > Manage account*. Any contacts that you add will be notified if there are any major changes to data submissions, and they will be listed as contacts on public data.

### Preparing the metadata

To ensure that sample data is registered with at least a minimum amount of metadata, ENA provides <a href="https://www.ebi.ac.uk/ena/browser/checklists" target="_blank">“Sample Checklists”</a> which are used during registration to tailor the sample descriptions to fit minimum standards. For convenience, we have created templates for the checklists we have used. The templates come with instructions on how to do an interactive submission, via the ENA Webin Portal, but even when doing a programmatic submission, the template can be useful for collecting all necessary descriptions / metadata.  Download an appropriate template, and fill in the sheets according to the instructions in the template:
  <ul>
    <li>ERC000011 <a href="/files/meta-data-templates/metadata_template_default_ERC000011.xlsx">ENA default sample checklist </a>(Excel spreadsheet)</li>
    <li>ERC000015 <a href="/files/meta-data-templates/metadata_template_human-gut_ERC000015.xlsx">GSC MIxS human gut </a>(Excel spreadsheet)</li>
    <li>ERC000024 <a href="/files/meta-data-templates/metadata_template_GSC-MIxS-water_ERC000024.xlsx">GSC MIxS water </a>(Excel spreadsheet)</li>
    <li>ERC000033 <a href="/files/meta-data-templates/metadata_template_virus_ERC000033.xlsx">ENA virus pathogen reporting standard checklist </a>(Excel spreadsheet)</li>
    <li>ERC000036 <a href="/files/meta-data-templates/metadata_template_sewage_ERC000036.xlsx">ENA sewage checklist </a>(Excel spreadsheet)</li>
    <li>ERC000050 <a href="/files/meta-data-templates/metadata_template_ENA_binned_metagenome_ERC000050.xlsx">ENA binned metagenome checklist </a>(Excel spreadsheet)</li>
    <li>ERC000053 <a href="/files/meta-data-templates/metadata_template_tree-of-life_ERC000053.xlsx">Tree of Life Checklist </a>(Excel spreadsheet)</li>
  </ul>
<!-- question is if we should link to VIB templates instead of ours, but that we can do in the future -->

The templates are divided into five sheets (each related to a type of metadata object), namely **study**, **sample**, **experiment**, **run** and **assemblies**. It is good practice to fill in all relevant sheets in the template, as having all the metadata collected in one place eases the submission process.

In the sample sheet, the first row contains the name of the checklist, the second row contains the field names, the third provides a description of the field, the fourth field indicates whether the field is mandatory, recommended or optional. Some fields have controlled vocabulary, which are available in the template as drop-down lists (the lists become visible when you click on a cell).

**Note**: It is *strongly* recommended that you provide as much information as possible in the metadata sheets. This will increase the [FAIRness](https://www.go-fair.org/fair-principles/) of your data, and thus the probability that it will be useful in future research efforts.

The sample metadata sheet can be submitted to ENA, however it must be in .tsv file format. For ease, the downloads on this page are provided in .xlsx, commonly known as Microsoft Excel, format. It is therefore necessary for you to convert the file format. If you are using Microsoft Excel to edit the metadata templates, click *File (or the Office Button) > Save As* and change 'save as file type' to 'Text (Tab delimited) (\*. tsv)'. Enter a file name and save the file. If you are using a Mac, you can change the file type by right-clicking on the .xlsx file in Finder, selecting *rename* and typing '.tsv' at the end of your file name.

#### **An example**

In this scenario we have used the Tree of life checklist. A completed template is found in [Alectoris-graeca-metadata.xlsx](/static/files/ena_tutorial/Alectoris-graeca-metadata.xlsx), adapted from a real submission made under the <a href="https://biodiversitygenomics.eu/" target="_blank">Biodiversity Genomics Europe</a> (BGE) project organised by the <a href="" target="_blank">European Reference Genome Atlas</a> (ERGA) initiative. The task is to submit 4 datasets (one PacBio HiFi WGS, 2 Illumina HiC, and one Illumina RNAseq), including 4 samples, in one study, and a chromosome level assembly in another study, and finally group these two projects together under an umbrella study.

## Submission methods

ENA describes [three methods](https://ena-docs.readthedocs.io/en/latest/submit/general-guide.html) of submission, none of which can be used in isolation to complete all parts of a submission:

* **Interactive Submission Method** - involves filling out web forms directly in the browser and downloading template spreadsheets that can be completed off-line and uploaded later to ENA. This is the easiest method to use when getting started, but quickly becomes time-consuming with bulk submission (> 50 records). It is possible to submit **studies**, **samples**, and **raw reads** this way.

* **Command-Line Submission Method** - uses ENA’s **Webin-CLI program**. Submissions require the preparation of text (manifest) files that are validated before submissions are completed. It is possible to submit **raw reads** and **assemblies**, this way. Actually, for assemblies, this is the **only** way to submit.

* **Programmatic Submission Method** - requires the preparation of XML documents that are sent to ENA using cURL or the Webin Portal of ENA. It is possible to submit **studies**, **samples**, and **raw reads** this way. This is the **only** way to submit **umbrella** studies.

Hence, in order to do a submission of both raw reads and assemblies, and group 2 studies together under an umbrella study, you need to use a combination of methods described below.


### Interactive submission
<!-- instructions on how to submit using as little command-line as possible -->
<!-- Study, sample and raw reads -->

### Programmatic submission
<!-- instructions on how to submit using as much command-line as possible -->
<!-- Study, sample and raw reads -->

### Assembly submission
<!-- walk through how to install and use Webin-CLI -->

### Umbrella submission
<!-- walk through how to programmatically submit an umbrella -->

## Terminology

### Data types

* **'Raw' sequence data** - Sequence data that is obtained directly from a sequencing instrument (typically in FASTQ or BAM file format). 

* **Analysed sequence data** - Sequence data that has been processed in some way after being obtained from a sequencing instrument. Such data has been normalised, and perhaps also subject to other processing (e.g. removal of outliers, calculation of expression measurements, and statistical analyses). Another example of analysed data is genome assemblies.

* **Metadata** - Description of the data that gives, at a minimum, sufficient information to reproduce the data collection method (e.g. description of how the source material was obtained and details about the sequencing process, such as library preparation and the instruments used). 

### Metadata objects

ENA recognises multiple 'levels'/'types' of metadata related to sequencing projects. These different 'levels'/'types' of metadata are represented by different metadata objects:

* **Study** - A study (project) object is used to group together all data submitted to ENA about a given study and to control its release date. A study accession number is typically used to cite data submitted to ENA. Note that all data and metadata associated with a study are made public together with the study when it is released.

* **Sample** - A sample object contains information about the sequenced source material. Checklists are in place to define which fields should be filled when annotating samples. Note that a taxonomic classification system is used to refer to biological organisms; the accepted organism name and classification hierarchy are used, see [here](https://www.gbif.org/dataset/6b6b2923-0a10-4708-b170-5b7c611aceef) for further details.

* **Experiment** - An experiment object contains all the details about the metholodology used for sequencing, including library and instrument details.

* **Run** - A run object is part of an experiment object. It refers to data files that contain 'raw' sequence reads.

* **Analysis** - An analysis object contains secondary analysis results. These results are derived from 'raw' sequence reads (e.g. a genome assembly).

The different metadata objects relate to different stages of the sequencing process. 
<!-- likely should include the classic metadata model, or an updated version of it -->

<!-- ## Resources
Please find below resources concerning --add title/topic--- in form of training, guidance and/or tools.

{{< resources-per-page-topics >}}
 -->
