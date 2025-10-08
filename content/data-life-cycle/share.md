---
title: Sharing phase
phase: Share
tags: ["repository", "domain-specific repositories", "discipline-specific repositories","general-purpose repositories", "restricted access", "institutional repositories", "genomics data","imaging data", "metabolomics data", "proteomics data"]
toc: True
---

# Sharing
In the era of FAIR (Findable, Accessible, Interoperable and Reusable) and <a href="https://www.vr.se/english/mandates/open-science/open-access-to-research-data.html" target="_blank">Open science</a>, datasets should be made available to the public. Whenever possible, discipline-specific repositories (with or without controlled access) should be used in order to increase the FAIRness of your research outputs. If no such repository is available, there are general-purpose repositories.

<a class="link-teal" href="/topics/fair-principles"><b>Learn more about the FAIR principles <i class="bi bi-arrow-right-square"></i></b></a>
<br/><br/>

## Finding a suitable repository type

<br/>

  <img class="img-fluid" src="/img/illustrations/repository_overview_v5.png" alt="Repository overview">

&nbsp;&nbsp;

**Does your data contain personal or sensitive information that cannot be fully anonymised?**

There may be cases where openly sharing data is not feasible due to ethical or confidentiality considerations. Depending on what the ethical board approving your study said about data sharing, and the level of permission granted from participants, it may still be possible to make your data accessible to authenticated users via a controlled-access repository.

<a class="link-teal" href="/topics/sharing-human-data"><b>See more guidelines on sharing human data <i class="bi bi-arrow-right-square"></i></b></a>

**Is there a discipline specific repository for your dataset?**

Research data differs greatly across disciplines. Discipline-specific repositories offer specialist domain knowledge and curation expertise for particular data types. Using a discipline-specific repository makes your data visible to others in your community.

**Does your institutional repository accept data?**

Many institutions offer support to their employees for managing and depositing data. Institutional repositories that accept datasets provide stewardship, helping to ensure that your dataset is preserved and accessible.

**Answered no on all questions above?**

General-purpose data repositories accept datasets regardless of discipline or institution. These repositories support a wide variety of file types and are particularly useful where a discipline-specific repository does not exist.

## Recommended discipline-specific repositories

There are several repositories for life science data types (see e.g. <a href="https://elixir-europe.org/platforms/data/elixir-deposition-databases" target="_blank">ELIXIR Deposition Database list</a>), please find a selection of them below.

&nbsp;

### Genomics data
Click on the buttons below for specific information regarding suitable repositories for sharing genomics data.

<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample1" role="button" aria-expanded="false" aria-controls="collapseExample1">
    European Nucleotide Archive
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseExample1">
  <div class="card card-body">
  <span>
  The European Nucleotide Archive (ENA) hosts its own instance of the Sequence Read Archive (SRA), which uses the same data model at the SRA at NCBI. The SRA accepts raw sequencing data from any platform and from any type of research project. There are several ways to <a href="https://www.ebi.ac.uk/ena/submit" target="_blank">submit</a> data to ENA, for more information see the documentation. NBIS provides <a href="https://github.com/NBISweden/data-submission-documentation/tree/main/ENA" target="_blank">examples</a> of submissions to ENA, including standard operating procedures (SOPs). These are exemplified in our <a href="/topics/ena-submission-tutorial">ENA submission tutorial</a>.
  <br><br>
  We also recommend the following two specialised guidelines:
  <ul>
  <li><a href="https://biodiversitydata-se.github.io/mol-data/index.html" target="_blank">Guide for submission of metabarcoding data to ENA</a> provided by the Swedish Biodiversity Data Infrastructure (<a href="https://biodiversitydata.se/" target="_blank">SBDI</a>)</li>
    <li><a href="https://www.pathogens.se/support_services/tutorial_ena/tutorial_ena_intro/" target="_blank">Tutorial for SARS-CoV-2 genome data submission to ENA</a> provided by the Swedish Pathogens Portal</li>
  </ul>

  For convenience, we have created templates for the most frequent data types and their corresponding <a href="https://www.ebi.ac.uk/ena/browser/checklists">ENA checklists</a>. The templates come with instructions on how to do an interactive submission, via the ENA Webin Portal, but even when doing a programmatic submission, the template can be useful for collecting all necessary descriptions / metadata.  Download an appropriate template, and fill in the sheets according to the instructions in the template:
  <ul>
    <li>ERC000011 <a href="/files/meta-data-templates/metadata_template_default_ERC000011.xlsx">ENA default sample checklist </a>(Excel spreadsheet)</li>
    <li>ERC000015 <a href="/files/meta-data-templates/metadata_template_human-gut_ERC000015.xlsx">GSC MIxS human gut </a>(Excel spreadsheet)</li>
    <li>ERC000024 <a href="/files/meta-data-templates/metadata_template_GSC-MIxS-water_ERC000024.xlsx">GSC MIxS water </a>(Excel spreadsheet)</li>
    <li>ERC000033 <a href="/files/meta-data-templates/metadata_template_virus_ERC000033.xlsx">ENA virus pathogen reporting standard checklist </a>(Excel spreadsheet)</li>
    <li>ERC000036 <a href="/files/meta-data-templates/metadata_template_sewage_ERC000036.xlsx">ENA sewage checklist </a>(Excel spreadsheet)</li>
    <li>ERC000050 <a href="/files/meta-data-templates/metadata_template_ENA_binned_metagenome_ERC000050.xlsx">ENA binned metagenome checklist </a>(Excel spreadsheet)</li>
    <li>ERC000053 <a href="/files/meta-data-templates/metadata_template_tree-of-life_ERC000053.xlsx">Tree of Life Checklist </a>(Excel spreadsheet)</li>
  </ul>
  </span>
  <br>
  <a class="link-teal" href="https://www.ebi.ac.uk/ena" target="_blank"><b>Visit ENA <i class="bi bi-box-arrow-up-right"></i></b></a>

  <a class="link-teal" href="https://ena-docs.readthedocs.io/en/latest/" target="_blank"><b>Learn more about how to submit to ENA <i class="bi bi-box-arrow-up-right"></i></b></a>
  </div>
  <br>
</div>

<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample2" role="button" aria-expanded="false" aria-controls="collapseExample2">
    ArrayExpress
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseExample2">
  <div class="card card-body">
  <span>
  ArrayExpress is tightly integrated with ENA and similar to NCBI’s Gene Expression Omnibus database it can be used to archive experimental designs and analysis files based on the raw sequence reads. ArrayExpress has its own <a href="https://www.ebi.ac.uk/fg/annotare/login/" target="_blank">submission portal</a> where information is available on what can be submitted and how.<br>
  </span>
  <br>
  <a class="link-teal" href="https://www.ebi.ac.uk/arrayexpress/" target="_blank"><b>Visit ArrayExpress <i class="bi bi-box-arrow-up-right"></i></b></a>
  </div>
  <br>
</div>

<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample3" role="button" aria-expanded="false" aria-controls="collapseExample3">
    European Genome-phenome Archive
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseExample3">
  <div class="card card-body">
  <span>
  European Genome-phenome Archive (EGA) is a service for sharing personally identifiable <a href="/topics/gdpr-ethical-review-glossary/#genetic-data">genetic</a> and phenotypic data resulting from biomedical research projects. The repository is hosted by the European Bioinformatics Institute (EMBL-EBI) and the Centre for Genomic Regulation (CRG). Any data submitted to the repository is subject to controlled access, which means that access to the data only will be granted after a formal application procedure.
  </span>
  <br>
  <a class="link-teal" href="https://ega-archive.org/" target="_blank"><b>Visit EGA <i class="bi bi-box-arrow-up-right"></i></b></a>
  </div>
  <br>
</div>

<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample4" role="button" aria-expanded="false" aria-controls="collapseExample4">
    FEGA Sweden
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseExample4">
  <div class="card card-body">
  <span>
  FEGA Sweden is a repository for storing and sharing personally identifiable <a href="/topics/gdpr-ethical-review-glossary/#genetic-data">genetic</a> and phenotypic data in Sweden in a way that meets the requirements of the <a href="/topics/gdpr-ethical-review-glossary/#gdpr-general-data-protection-regulation">General Data Protection Regulation GDPR</a>. It is part of the <a href="https://ega-archive.org/about/projects-and-funders/federated-ega/" target="_blank">Federated European Genome-phenome Archive</a>, which is a network consisting of several national nodes and the European Genome-phenome Archive (EGA). Researchers can create a submission request by filling in a form on the website.
  </span>
  <br>
  <a class="link-teal" href="https://fega.nbis.se/" target="_blank"><b>Visit FEGA Sweden <i class="bi bi-box-arrow-up-right"></i></b></a>
  </div>
  <br>
</div>
&nbsp;

### Imaging data
Depending on the type of image data you have, different public repositories are available, please see the table at BioImage Archive.
<br><br>
  <a class="link-teal" href="https://www.ebi.ac.uk/bioimage-archive/" target="_blank"><b>Visit BioImage Archive <i class="bi bi-box-arrow-up-right"></i></b></a>

<br>

### Metabolomics data
MetaboLights is a database for Metabolomics experiments and derived information. The database is cross-species, cross-technique and covers metabolite structures and their reference spectra as well as their biological roles, locations and concentrations, and experimental data from metabolic experiments.
<br><br>
  <a class="link-teal" href="https://www.ebi.ac.uk/metabolights/" target="_blank"><b>Visit MetaboLights <i class="bi bi-box-arrow-up-right"></i></b></a>

<br>


### Proteomics data
The <a href="http://www.proteomexchange.org/" target="_blank">ProteomeXchange</a> Consortium provides globally coordinated standard data submission and dissemination pipelines involving the main proteomics repositories.
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample6" role="button" aria-expanded="false" aria-controls="collapseExample6">
    PRIDE
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseExample6">
  <div class="card card-body">
  <span>
  PRIDE admits protein and peptide identification/quantification data with the accompanying mass spectra evidence and any other related data types. Submission is done using the <a href="https://www.ebi.ac.uk/pride/markdownpage/pridesubmissiontool" target="_blank">PRIDE Submission Tool</a>, see <a href="https://www.ebi.ac.uk/pride/markdownpage/documentationpage" target="_blank">How to submit data to PRIDE</a>.
  </span>
  <br>
  <a class="link-teal" href="https://www.ebi.ac.uk/pride/" target="_blank"><b>Visit PRIDE <i class="bi bi-box-arrow-up-right"></i></b></a>
  </div>
  <br>
</div>
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample7" role="button" aria-expanded="false" aria-controls="collapseExample7">
    PeptideAtlas
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseExample7">
  <div class="card card-body">
  <span>
  PeptideAtlas admits SRM/MRM data that does not fit into PRIDE (targeted datasets). Submission is done via <a href="http://www.peptideatlas.org/passel/" target="_blank">PASSEL</a>.
  </span>
  <br>
  <a class="link-teal" href="http://www.peptideatlas.org/" target="_blank"><b>Visit PeptideAtlas <i class="bi bi-box-arrow-up-right"></i></b></a>
  </div>
  <br>
</div>
&nbsp;

### Other data

Guidance on where to publish COVID-19 and Pandemic Preparedness research data, can be found on the <a href="https://pathogens.se/share-data/" target="_blank">Swedish Pathogens Portal</a>.

For other discipline-specific repositories, see e.g. <a href="https://elixir-europe.org/services/tag/elixir-deposition-databases" target="_blank">ELIXIR Deposition databases</a>, <a href="https://www.ebi.ac.uk/submission/" target="_blank">EBI archive wizard</a> (help to find the right repository depending on data type), or <a href="https://fairsharing.org/databases/" target="_blank">FAIRsharing</a> (the latter can also assist in finding metadata standards suitable for describing your datasets).

&nbsp;

## Institutional repositories
For datasets that do not fit into discipline-specific repositories, it is recommended to use an institutional repository if available. These repositories are often general-purpose repositories with the intention of only being used by researchers at that specific institution. See below a selection of available repositories offered by Swedish academic institutions operating in the life sciences. 

<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample8" role="button" aria-expanded="false" aria-controls="collapseExample8">
    KI Data Repository 
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseExample8">
  <div class="card card-body">
  <span>
  KI Data Repository is a data repository where Karolinska Institutet's (KI's) researchers can store, publish and share data.
  </span>
  <br>
  <a class="link-teal" href="https://kib.ki.se/en/publish-analyse/publish-and-share-research-data/doris-publish-and-share-your-research-data" target="_blank"><b>Visit KI Data Repository <i class="bi bi-box-arrow-up-right"></i></b></a>
  </div>
  <br>
</div>
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample5" role="button" aria-expanded="false" aria-controls="collapseExample5">
    KTH Data Repository
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseExample5">
  <div class="card card-body">
  <span>
  The KTH Data Repository is a general data repository offered as a service from KTH Royal Institute of Technology. The service offers a solution for depositing and preparing documentation and static versions of data and source code for your research project. Deposited data can be kept for internal archive or published as open data.
  </span>
  <br>
  <a class="link-teal" href="https://datarepository.kth.se" target="_blank"><b>Visit KTH Data Repository <i class="bi bi-box-arrow-up-right"></i></b></a>
  </div>
  <br>
</div>
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample9" role="button" aria-expanded="false" aria-controls="collapseExample9">
    KTH Royal Institute of Technology Zenodo community
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseExample9">
  <div class="card card-body">
  <span>
  The KTH Royal Institute of Technology Zenodo community is the official community for all researcher's at KTH Royal Institute of Technology who wants to deposit open research output via Zenodo, get support on the description and findability of data by the research data team  and obtain a DOI for that public research output.
  </span>
  <br>
  <a class="link-teal" href="https://zenodo.org/communities/kth/records?q=&l=list&p=1&s=10&sort=newest" target="_blank"><b>Visit KTH Zenodo community <i class="bi bi-box-arrow-up-right"></i></b></a>
  </div>
  <br>
</div>
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample10" role="button" aria-expanded="false" aria-controls="collapseExample10">
    SciLifeLab Data Repository
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseExample10">
  <div class="card card-body">
  <span>
  The SciLifeLab Data Repository, powered by Figshare and supported by SciLifeLab and the Knut and Alice Wallenberg foundation through the Data-Driven Life Science (DDLS) program, is a repository for publishing any kind of research-related data, e.g. documents, figures, or presentations. Figshare is an open data repository used by researchers in numerous disciplines. Through an agreement with Figshare, SciLifeLab offers researchers and units the opportunity to upload and publish their research data through a dedicated portal.
  </span>
  <br>
  <a class="link-teal" href="https://www.scilifelab.se/data/repository/" target="_blank"><b>Visit SciLifeLab Data Repository <i class="bi bi-box-arrow-up-right"></i></b></a>
  </div>
  <br>
</div>
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseExample11" href="#collapseExample11">
    Stockholm University Figshare
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseExample11">
  <div class="card card-body">
  <span>
  Stockholm University Figshare  is a repository for publishing any kind of research-related data, e.g. documents, figures, or presentations. Figshare is an open data repository used by researchers in numerous disciplines. Through an agreement with Figshare, Stockholm University offers researchers the opportunity to upload and publish their research data through a dedicated portal.
  </span>
  <br>
  <a class="link-teal" href="https://su.figshare.com/" target="_blank"><b>Visit Stockholm University Figshare <i class="bi bi-box-arrow-up-right"></i></b></a>
  </div>
  <br>
</div>
&nbsp;

## General-purpose data repositories 
A general-purpose data repository is an appropriate choice only if the data does not need to be published in a controlled-access repository, a discipline-specific repository does not exist for the discipline and if there are no institutional repositories available. See below a selection of general-purpose data repositories.
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample12" role="button" aria-expanded="false" aria-controls="collapseExample12">
    SND DORIS
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseExample12">
  <div class="card card-body">
  <span>
  In DORIS (the Swedish National Data Service's (SND) Data Organisation and Information System) you can describe and share research data from all disciplines. By using DORIS, well-documented data are shared in a way that fulfils the FAIR principles.
  </span>
  <br>
  <a class="link-teal" href="https://snd.se/en/doris-researchers/describe-and-share-data-doris" target="_blank"><b>Visit DORIS <i class="bi bi-box-arrow-up-right"></i></b></a>
  </div>
  <br>
</div>
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample13" role="button" aria-expanded="false" aria-controls="collapseExample13">
    Figshare
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseExample13">
  <div class="card card-body">
  <span>
  Figshare is an open data, general-purpose, repository used by researchers in numerous disciplines. It can be used for sharing basically any kind of data, but also for just describing data stored elsewhere. 
  </span>
  <br>
  <a class="link-teal" href="https://figshare.com" target="_blank"><b>Visit Figshare <i class="bi bi-box-arrow-up-right"></i></b></a>
  </div>
  <br>
</div>
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample14" role="button" aria-expanded="false" aria-controls="collapseExample14">
    Zenodo
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseExample14">
  <div class="card card-body">
  <span>
  Zenodo is an open data, general-purpose, repository operated by CERN. It can be used for sharing basically any kind of data, but also for just describing data stored elsewhere. Zenodo doesn't enforce standardised descriptions of data, so datasets described there might be more difficult to find than those described in the two repositories mentioned above.
  </span>
  <br>
  <a class="link-teal" href="https://zenodo.org/" target="_blank"><b>Visit Zenodo <i class="bi bi-box-arrow-up-right"></i></b></a>
  </div>
  <br>
</div>
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample15" role="button" aria-expanded="false" aria-controls="collapseExample15">
    EUDAT B2SHARE
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseExample15">
  <div class="card card-body">
  <span>
  B2SHARE is a user-friendly, reliable and trustworthy way for researchers, scientific communities and citizen scientists to store, publish and share research data in a FAIR way. B2SHARE is a solution that facilitates research data storage, guarantees long-term persistence of data and allows data, results or ideas to be shared worldwide.
  </span>
  <br>
  <a class="link-teal" href="https://eudat.eu/service-catalogue/b2share-0" target="_blank"><b>Visit EUDAT B2SHARE <i class="bi bi-box-arrow-up-right"></i></b></a>
  </div>
  <br>
</div>
&nbsp;

## How can SciLifeLab help you sharing data?

If you are a researcher at a Swedish academic institution operating in the life sciences, you can get help from SciLifeLab Data Management support team. This support team can help you describe and deposit your data. Here are a few examples of the support that is offered:

* Plan data submission
* Identify suitable repositories
* Assist during the submission process when publishing data and code
* Assist in the creation of metadata records in SciLifeLab Data Repository
* Advice on what needs to be done when working with sensitive human data
* Advice on describing data with proper metadata

If you need any help connected to data submission, please contact us!

<a class= "link-teal" href="/contact/"><b>Contact form to get support <i class="bi bi-arrow-right-square"></i></b></a>

## Resources
Please find below resources concerning the research data life cycle phase share in form of training, guidance and/or tools.

{{< resources-per-page-phases >}}
