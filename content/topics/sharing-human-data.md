---
title: Sharing human data
contributors: []
category: Human data
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


## Sharing non-personal data

If your data cannot be linked to a living person, there is nothing in GDPR that prohibits you from sharing the data publicly. Data may however be sensitive under other regulations, so make sure that you take all relevant legal aspects into account. If you are dealing with human data, you should of course also think about the ethical and societal implications of sharing the data.

<!--There are many repositories for sharing human-related data publicly. Here are a few examples:

European Nucleotide Archive (ENA)
: The [European Nucleotide Archive](https://www.ebi.ac.uk/ena/browser/home) is a public repository for nucleotide sequences hosted by the European Bioinformatics Institute (EMBL-EBI).

ArrayExpress
: [ArrayExpress](https://www.ebi.ac.uk/biostudies/arrayexpress) is a repository for functional genomics data hosted by the European Bioinformatics Institute (EMBL-EBI).

SciLifeLab Data Repository
: The [SciLifeLab Data Repository](https://figshare.scilifelab.se) is a an institutional repository hosted by SciLifeLab for depositing and describing data related to life science research. It is particularily useful for sharing files that are not suited for discipline-specific repositories. -->

<a href="/data-life-cycle/share/"><b>Learn more about data sharing and repositories <i class="bi bi-arrow-right-square-fill"></i></b></a>
<br/><br/>


## Sharing personal data

Data that needs to be protected from unauthorised access may be deposited in a *controlled access repository*. In these repositories access will typically only be granted after a formal application procedure. When submitting any personal data for archiving and sharing in a controlled access repository, you must be sure that you have the legal right to do so.

Here are some repositories for sharing and archiving data under controlled access:

### [European Genome-phenome Archive](https://ega-archive.org)
This is a service for sharing personally identifiable genetic and phenotypic data resulting from biomedical research projects. The repository is hosted by the European Bioinformatics Institute (EMBL-EBI) and the Centre for Genomic Regulation (CRG). Any data submitted to the repository is subject to controlled access, which means that access to the data only will be granted after a formal application procedure.

### [FEGA Sweden](https://fega.nbis.se/)
This is a repository for storing and sharing personally identifiable genetic and phenotypic data in Sweden in a way that meets the requirements of the General Data Protection Regulation (GDPR). It is part of the [Federated European Genome-phenome Archive](https://ega-archive.org/about/projects-and-funders/federated-ega/) (FEGA), which is a network consisting of several national nodes and the European Genome-phenome Archive (EGA). FEGA Sweden is currently transitioning into operational mode and researchers may express their interest in depositing data to the repository by filling in [a web form](https://fega.nbis.se/submission/submission-request.html).


### [AIDA Data Hub](https://datahub.aida.scilifelab.se/)
This platform is part of the [Analytic Imaging Diagnostics Arena (AIDA)](https://medtech4health.se/aida/) and NBIS/SciLifeLab. It provides Data Sharing, Policy Support, and Services for researchers in Swedish medical imaging AI, and facilitates sharing of FAIR medical imaging research data for Open Science. The [AIDA Data Sharing Policy](https://datahub.aida.scilifelab.se/sharing/) is a comprehensive resource developed by ~50 AIDA partners in healthcare, industry, and academia, which includes legal analyses, best practices, and practical instructions for how to carry out ethically and legally correct sharing of sensitive personal data such as medical images in Sweden and similar countries. The [AIDA Dataset Register](https://datahub.aida.scilifelab.se/datasets/) provides Digital Object Identifiers (DOI) and landing pages for the datasets that have been shared on the AIDA Data Hub.

## If data cannot be deposited in a repository

It is not always possible to deposit personally identifiable data in a controlled access repository. In that case, you could register a *metadata record* for the data. This record will serve multiple purposes: First, it will enable unambiguous identification of the data. Second, it will provide a description of the data so that others can understand what the data is about. Third, the metadata record may contain instructions on how to get access to the data.

Here are a few repositories where you can register metadata records:

### [SciLifeLab Data Repository](https://figshare.scilifelab.se)
SciLifeLab is hosting an institutional repository, SciLifeLab Data Repository, for publishing any kind of research-related data, e.g. documents, figures, or presentations. This repository is an instance of Figshare, which means that every item will get a unique DOI. You can read more in the [repository's guidelines](https://www.scilifelab.se/data/repository). If you need any help connected to the SciLifeLab Data Repository, please [contact us](../../contact/)!

### [BioStudies](https://www.ebi.ac.uk/biostudies/)
This database contains descriptions of biological studies and is especially suited for linking a study to datasets in different repositories. However, it can also be used to describe sensitive data that has not been uploaded to a repository. BioStudies is hosted by the European Bioinformatics Institute (EMBL-EBI).


## How can SciLifeLab help you sharing human data?

If you are a researcher at a Swedish academic institution working in the life sciences, you can get help from SciLifeLab Data Management support team.


### Submission support for FEGA Sweden

FEGA Sweden is not yet in production, but you can get help with preparations for a future submission to the repository. The FEGA Sweden Helpdesk is part of the larger data management support team at SciLifeLab. Visit the [FEGA Sweden website](https://fega.nbis.se) to learn more about how you can prepare a submission and how to get in contact with the FEGA Sweden Helpdesk.


### Data access management support

If your data is located on the Bianca server at UPPMAX (or in the future deposited in FEGA Sweden), we can help with handling data access requests.

<div class="alert alert-warning" role="alert">
Until FEGA Sweden is ready for both storing and sharing data, we can only support data sharing with principal investigators that are eligible for setting up a project on Bianca server at UPPMAX.
</div>

To let us handle access requests to your data, you need to take the following steps:

1. Store the data in your own project on Bianca at UPPMAX.
2. Adjust the Data Access Agreement and Data Access request forms (available from [datacentre@scilifelab.se](mailto:datacentre@scilifelab.se)) to suit your particular case.
3. Prepare a metadata record for the dataset in the SciLifeLab Data Repository. It is important to not upload the human data, but do provide as much descriptive metadata as possible to improve the findability. Set [datacentre@scilifelab.se](mailto:datacentre@scilifelab.se) as "access request email" and your own email address as "contact email".
4. In your manuscript add a section on Data Availability and make sure it includes information on where to go for requesting access to the data. You could for example write the following in your manuscript:
> The data is deposited on a secure Swedish server and has been assigned a DOI (XXX). Data access requests may be submitted to the Science for Life Laboratory Data Centre through the DOI link.
5. When a user applies for access to [datacentre@scilifelab.se](mailto:datacentre@scilifelab.se), the application will be vetted and you will be contacted by us. Then you can make a decision on access approved or denied. Ideally, you can (should) delegate this decision to an independent Data Access Committee (DAC).
6. When a user has been approved for access, SciLifeLab Data Centre will document the processing and arrange for the physical file access. Until FEGA Sweden is up and running, the physical file access will be that you, as a PI, copies the dataset from your Bianca project space, to the specified project space of the approved applicant. Because of NAISS user policy, only PIs at a Swedish academic institution can have a project at Bianca. So to share data with a collaborator outside Sweden, the PI in Sweden needs to have applied for a project at Bianca. Please see the [Bianca user guide](https://www.uppmax.uu.se/support/user-guides/bianca-user-guide/) for information on how to do this.
7. SciLifeLab Data Centre will keep track of current and expired approvals.

If you need any help connected to data submission, please [contact us](../../contact/)!

## Resources
Please find below resources concerning research involving human data in form of training, guidance and/or tools.

{{< resources-per-page-topics >}}
