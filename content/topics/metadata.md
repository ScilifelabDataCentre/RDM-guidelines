---
title: Metadata
category: Other
tags: ["ontologies", "ontology", "data types", "metadata standards", "metadata formats", "ENA checklists", "metadata templates", "data dictionaries", "cellular and molecular imaging data", "genomics data", "metabolomics and exposomics data", "proteomics data", "spatial omics data", "structural biology data"]
toc: True
---

# Metadata
Good documentation in research projects is essential in order to allow good quality data and transparent research. Describing how the datasets were created, how they are structured, and what they mean, is key for making your data understandable for others as well as your future self. Metadata provides such 'data about data'.
Metadata is needed at several levels to describe the study, the samples, the experiments, the analysis and so on (see also topic on [README](/topics/readme-files/) for documentation on different levels). It may include information on the methodology and instrumentation used to collect the data, analytical and procedural information, definitions of variables, units of measurement, any assumptions made, the format and file type of the data and software used to collect and/or process the data.

Researchers are strongly encouraged to use community metadata standards where these are in place (see further down) and are recommended doing so already from the beginning of the project. Data repositories may also provide guidance about appropriate metadata standards and requirements e.g. the European Nucleotide Archive (ENA) have sample checklists. We provide templates for some of these checklists, see further on [Data type guide - ENA Sample Checklists](/data-type-guide/?resource=ena-checklists). Structuring the metadata in a way that conforms to the suitable repository from the beginning enables data submission without having to reformat the metadata.


<a class="link-teal" href="https://www.ebi.ac.uk/ena/submit/checklists" target="_blank"><b>Browse ENA checklists <i class="bi bi-box-arrow-up-right"></i></b></a>

## Ontologies

Ontologies, controlled vocabularies and data dictionaries are used to standardize the language used to describe the metadata. Think of the many ways to write that the organism is human (human, Human, homo sapiens, H. sapiens, Homo Sapiens, man, etc), using an ontology such as <a href="https://www.ebi.ac.uk/ols/ontologies/ncbitaxon" target="_blank">NCBI taxonomy</a> unifies the language and makes it easier for both humans and machines to interpret and work with the data. While an ontology has a hierarchical structure (e.g. *homo sapiens* is a *mammalia* which is a *eukaryota*), a controlled vocabulary is an unstructured set of terms, but fills the same purpose, to standardize the language used. A data dictionary is a user-defined way of describing what all the variable names and values in the data really mean.

<a class="link-teal" href="https://help.osf.io/hc/en-us/articles/360019739054-How-to-Make-a-Data-Dictionary" target="_blank"><b>Learn more about Data Dictionaries <i class="bi bi-box-arrow-up-right"></i></b></a>

For a suggested list of ontologies appropriate for Life Science community please see FAIRsharing.org, filter on e.g. Domain.

Below are ontology resources, adapted from Table 2 in *Griffin PC, Khadake J, LeMay KS et al. Best practice data life cycle approaches for the life sciences. F1000Research 2018, 6:1618.* doi: <a href="https://doi.org/10.12688/f1000research.12344.2" target="_blank">10.12688/f1000research.12344.2</a>:

* <a href="https://www.ebi.ac.uk/ols/" target="_blank">Ontology Lookup Service</a> - Discover different ontologies and their contents.
* <a href="https://obofoundry.org/" target="_blank">OBO Foundry</a> - Table of open biomedical ontologies with information on development status, license and content.
* <a href="https://www.ebi.ac.uk/spot/zooma/" target="_blank">ZOOMA</a> - Assign ontology terms using curated mapping.
* <a href="https://www.ontobee.org" target="_blank">Ontobee</a> - A linked data server that facilitates ontology data sharing, visualization, and use.

## Metadata standards and formats
Communities within specific research domains have mutually agreed upon what pieces of information is needed in order to properly describe a research output. Metadata standards (in the form of reporting guidelines) provide a consistent set of fields and terms (schemas) to ensure everyone describes the same thing using the same labels (e.g. always using "Creator" instead of "Author" or "Writer"). Metadata formats on the other hand provides the technical implementation of the standards.

Please find links below to our **Data type guide** for a selection of the metadata standards and formats used by the ELIXIR deposition databases. For a global perspective, please visit <a href="https://fairsharing.org/databases/" target="_blank">FAIRsharing.org</a>.

<a class="btn btn-round btn-teal" href="/data-type-guide/?area=genomics&info=metadata"><b>Genomics data <i class="bi bi-arrow-right-square"></i></b></a><br>

<a class="btn btn-round btn-teal" href="/data-type-guide/?area=proteomics&info=metadata"><b>Proteomics data <i class="bi bi-arrow-right-square"></i></b></a><br>

<a class="btn btn-round btn-teal" href="/data-type-guide/?area=metabolomics-and-exposomics&info=metadata"><b>Metabolomics and Exposomics data <i class="bi bi-arrow-right-square"></i></b></a><br>

<a class="btn btn-round btn-teal" href="/data-type-guide/?area=spatial-omics&info=metadata"><b>Spatial Omics data <i class="bi bi-arrow-right-square"></i></b></a><br>

<a class="btn btn-round btn-teal" href="/data-type-guide/?area=cellular-and-molecular-imaging&info=metadata"><b>Cellular and Molecular Imaging data <i class="bi bi-arrow-right-square"></i></b></a><br>

<a class="btn btn-round btn-teal" href="/data-type-guide/?area=structural-biology&info=metadata"><b>Structural Biology data <i class="bi bi-arrow-right-square"></i></b></a><br>

Note that RDMkit provides a domain page with information about standard (meta)data formats for <a href="https://rdmkit.elixir-europe.org/bioimaging_data" target="_blank">Bioimagning data</a>. 

&nbsp;

## Resources
Please find below resources concerning metadata in form of training, guidance and/or tools.
{{< resources-per-page-topics >}}

