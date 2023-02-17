---
title: Sharing human data
contributors: []
toc: True
---

# Sharing human data

<div class="alert alert-warning" role="alert">
  <B><I>Disclaimer!</I></B> The PI, as well as everyone with access to sensitive personal data, is responsible for following current laws and regulations, and SciLifeLab will not assume legal responsibility for advice provided in these guidelines.
</div>

<!-- Generella riktlinjer för publicering av human data. Vilka olika nivåer finns.  
The recommendations on publishing human data varies depending on the nature of the human data in question. The principle "As open as possible, as closed as necessary" is of great importance when it comes to publishing human data. -->


<a href="/topics/research-involving-human-data"><b>See more guidelines on research involving human data <i class="bi bi-arrow-right-square-fill"></i></b></a>
<br/><br/>
<a href="/topics/gdpr-legal-reference.md"><b>See more guidelines on GDPR <i class="bi bi-arrow-right-square-fill"></i></b></a>
<br/><br/>

## Sharing non-personal data

If your data cannot be linked to a living person, there is nothing in GDPR that prohibits you from sharing the data publicly. Data may however be sensitive under other regulations, so make sure that you take all relevant legal aspects into account. If you are dealing with human data, you should of course also think about the ethical and societal implications of sharing the data.

There are many repositories for sharing human-related data publicly. Here are a few examples:

European Nucleotide Archive (ENA)
: The [European Nucleotide Archive](https://www.ebi.ac.uk/ena/browser/home) is a public repository for nucleotide sequences hosted by the European Bioinformatics Institute (EMBL-EBI).

ArrayExpress
: [ArrayExpress](https://www.ebi.ac.uk/biostudies/arrayexpress) is a repository for functional genomics data hosted by the European Bioinformatics Institute (EMBL-EBI). 

SciLifeLab Data Repository
: The [SciLifeLab Data Repository](https://figshare.scilifelab.se) is a an institutional repository hosted by SciLifeLab for depositing and describing data related to life science research. It is particularily useful for sharing files that are not suited for domain specific repositories.

Learn more about [data sharing and repositories](../../data-life-cycle/share/).


## Sharing personal data

Data that need to be protected from unauthorised access may be deposited in a *controlled access repository*. In these repositories will access typically only be granted after a formal application procedure. When submitting any personal data for archiving and sharing in a controlled access repository, you must be sure that you have the legal right to upload the data to the repository.

Here are two repositories for sharing and archiving data under controlled access:

European Genome-phenome Archive (EGA)
: [European Genome-phenome Archive](https://ega-archive.org) is a service for sharing personally identifiable genetic and phenotypic data resulting from biomedical research projects. The repository is hosted by the European Bioinformatics Institute (EMBL-EBI) and the Centre for Genomic Regulation (CRG). Any data submitted to the repository is subject to controlled access, which means that access to the data only will be granted after a formal application procedure.

FEGA Sweden
: [FEGA Sweden](https://fega.nbis.se/) is repository for storing and sharing personal identifiable genetic and phenotypic data in Sweden in a way that meets the requirements of the General Data Protection Regulation (GDPR). It is part of a federation of national nodes, [Federated European Genome-phenome Archive](https://ega-archive.org/federated), which is tightly connected to the European Genome-phenome Archive (EGA). FEGA Sweden is not yet operational, but researchers may express their interest in depositing data to the repository by filling in [a web form](https://nbis.se/support/supportform/index.php#sdaform).

<div class="alert alert-warning" role="alert">
<b>Do you plan to submit data to FEGA Sweden?</b> While waiting for the repository to become operational, you may want to create a metadata record in SciLifeLab Data Repository (see below). This will give you a DOI to put in your research article. Once your data has been released in FEGA Sweden, our data management support team will help you update your metadata record with apropriate information.
</div>


<!-- Uppdateras av Markus FEGA  -->

This is what you need to do:
1. Adjust the Data Access Agreement and Data Access request forms (available from datacentre@scilifelab.se) to suit your particular case.
2. Store your data in your own project account on Bianca at UPPMAX.
3. Prepare a metadata record for the dataset in the SciLifeLab Data Repository. o	It is important to not upload the human data, but do provide as much descriptive metadata as possible to improve the findability. Set datacentre@scilifelab.se as “access request email” and your own email address as “contact email”.
4. In the manuscript add a section on Data Availability and make sure it includes information on where to go for requesting access to the data. The section in the manuscript can include eg. : “The data is deposited on a secure Swedish server and has been assigned a DOI (XXX). Data access requests may be submitted to the Science for Life Laboratory Data Centre through the DOI link.”
5. When a user applies for access to datacentre@scilifelab.se, the application will be vetted and you will be contacted by us. Then you can make a decision on access approved or denied. Ideally, you can (should) delegate this decision to an independent Data Access Committee (DAC).
6. When a user has been approved for access, Data Centre will document the processing and arrange for the physical file access. Until FEGA Sweden is up and running, the physical file access will be that you, as a PI, copies the dataset from your Bianca project space, to the specified project space of the approved applicant. Because of SNIC user policy, only PIs at a Swedish academic institution can have a project at Bianca. So to share data with a collaborator outside Sweden, the PI in Sweden needs to have applied for a project at Bianca. Please see [here](https://www.uppmax.uu.se/support/user-guides/bianca-user-guide/) for information on how to do this.
7. Data Centre will keep track of current and expired approvals.



## Resources & Training
* [RDMkit on Human data](https://rdmkit.elixir-europe.org/human_data)
