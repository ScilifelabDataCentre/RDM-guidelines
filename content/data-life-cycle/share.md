---
title: Sharing phase
toc: True
---

## Sharing

In the era of [FAIR](/topic/fair-principles) (Findable, Accessible, Interoperable and Reusable) and [Open science](https://www.vr.se/english/mandates/open-science/open-access-to-research-data.html), datasets should be made available to the public. Whenever possible, domain-specific repositories should be used in order to increase the FAIRness of your research outputs. Click on the buttons below for data type specific information regarding suitable repositories.

<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample1" role="button" aria-expanded="false" aria-controls="collapseExample1">
    Genomics data
  </a>
</p>
<div class="collapse" id="collapseExample1">
  <div class="card card-body">
  <span>
  <h5> <a href="https://www.ebi.ac.uk/ena">ENA</a> (European Nucleotide Archive)</h5>
  The ENA hosts an instance of the Sequence Read Archive (SRA), the same archive that exists on NCBI. SRA accepts raw sequence data from any sequencing platform, generated in any research project. There are several ways to <a href="https://www.ebi.ac.uk/ena/submit">submit</a> data to ENA, for more information see the <a href="https://ena-docs.readthedocs.io/en/latest/">documentation</a>. <br><br> For convenience, we have created templates for the most frequent data types and their corresponding <a href="https://www.ebi.ac.uk/ena/browser/checklists">ENA checklists</a>. The templates come with instructions on how to do an interactive submission, via the ENA Webin Portal, but even when doing a programmatic submission, the template can be useful for collecting all necessary descriptions / metadata.  Download an appropriate template, and fill in the sheets according to the instructions in the template:
  <ul>
    <li><a href="/meta-data-templates/metadata_template_default_ERC000011.xlsx">ERC000011 ENA default sample checklist</a></li>
    <li><a href="/meta-data-templates/metadata_template_virus_ERC000033.xlsx">ERC000033 ENA virus pathogen reporting standard checklist</a></li>
    <li><a href="/meta-data-templates/metadata_template_sewage_ERC000036.xlsx">ERC000036 ENA sewage checklist</a></li>
  </ul>

  <h5> <a href="https://www.ebi.ac.uk/arrayexpress/">ArrayExpress</a></h5>
  ArrayExpress is tighty integrated with ENA and similar to NCBI’s Gene Expression Omnibus database it can be used to archive experimental designs and analysis files based on the raw sequence reads. ArrayExpress has its own <a href="https://www.ebi.ac.uk/arrayexpress/submit/overview.html">submission portal</a> where information is available on what can be submitted and how.<br><br>

  <h5> <a href="https://ega-archive.org/">EGA</a> (European Genome-phenome Archive)</h5>
  NBIS is building a local federated version of the European Genome-phenome Archive (EGA) in Sweden (EGA-SE), allowing for the publication of sensitive personal data within a legal framework. Until local EGA is available, the dataset should remain in the secure analysis environment (e.g. at Bianca on Uppmax). We suggest to make a metadata-only record in the <a href="https://www.scilifelab.se/data/repository">SciLifeLab Data Repository</a> with contact details on how to get access, and for which a DOI (i.e. a persistent identifier) can be issued. The DOI can then be used in the article to refer to the dataset. Once the Swedish EGA is operational, and the dataset deposited there, the access information can be changed to point at the EGA ID. See <a href="https://doi.org/10.17044/scilifelab.12292778">https://doi.org/10.17044/scilifelab.12292778</a>, for an example.

  </span>
  </div>
</div>

<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample2" role="button" aria-expanded="false" aria-controls="collapseExample2">
    Imaging data
  </a>
</p>
<div class="collapse" id="collapseExample2">
  <div class="card card-body">
  <span>
  Depending on the type of image data you have, different public repositories are available, please see the table at <a href="https://www.ebi.ac.uk/bioimage-archive/">BioImage Archive</a>.
  </span>
  </div>
</div>

<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample3" role="button" aria-expanded="false" aria-controls="collapseExample3">
    Metabolomics data
  </a>
</p>
<div class="collapse" id="collapseExample3">
  <div class="card card-body">
  <span>
  <a href="https://www.ebi.ac.uk/metabolights/">MetaboLights</a> is a database for Metabolomics experiments and derived information. The database is cross-species, cross-technique and covers metabolite structures and their reference spectra as well as their biological roles, locations and concentrations, and experimental data from metabolic experiments.
  </span>
  </div>
</div>

<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample4" role="button" aria-expanded="false" aria-controls="collapseExample4">
    Proteomics data
  </a>
</p>
<div class="collapse" id="collapseExample4">
  <div class="card card-body">
  <span>
  The <a href="http://www.proteomexchange.org/">ProteomeXchange</a> Consortium provides globally coordinated standard data submission and dissemination pipelines involving the main proteomics repositories:
  <ul>
    <li> <a href="https://www.ebi.ac.uk/pride/">PRIDE</a> - admits protein and peptide identification/quantification data with the accompanying mass spectra evidence and any other related data types. Submission is done using the <a href="https://www.ebi.ac.uk/pride/markdownpage/pridesubmissiontool">PX Submission Tool</a>, see <a href="https://www.ebi.ac.uk/pride/static/markdown/submitdatapage/files/Submission_Tutorial.pdf">tutorial</a>.</li>
    <li><a href="http://www.peptideatlas.org/">PeptideAtlas</a> - for SRM/MRM data that does not fit into PRIDE (targeted datasets). Submission is done via <a href="http://www.peptideatlas.org/passel/">PASSEL</a>.</li>
  </ul>
  </span>
  </div>
</div>

<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample5" role="button" aria-expanded="false" aria-controls="collapseExample5">
    Other repositories
  </a>
</p>
<div class="collapse" id="collapseExample5">
  <div class="card card-body">
  <span>
  For other domain-specific repositories, see e.g. <a href="https://elixir-europe.org/services/tag/elixir-deposition-databases">ELIXIR Deposition databases</a>, <a href="https://www.nature.com/sdata/policies/repositories">Scientific Data recommended repositories</a>, <a href="https://www.ebi.ac.uk/submission/">EBI archive wizard</a> (help to find the right repository depending on data type), or <a href="https://fairsharing.org/databases/">FAIRsharing</a> (the latter can also assist in finding metadata standards suitable for describing your datasets). For datasets that do not fit into domain-specific repositories, use a general repository e.g. <a href="https://www.scilifelab.se/data/repository/">SciLifeLab Data Repository</a>, <a href="https://figshare.com/">Figshare</a> and <a href="https://zenodo.org/">Zenodo</a>.
  </span>
  </div>
</div>

## Resources & Training
* [RDMkit on Sharing Data](https://rdmkit.elixir-europe.org/sharing)
* [Data publication module](https://nbisweden.github.io/module-data-publication-dm-practices/) in course [Introduction to data management practices](https://uppsala.instructure.com/courses/48087/pages/introduction-to-data-management-practices)
* Many of the repositories at EBI have instructive videos on how to do submission as well as documentation, have a look at their [YouTube playlist](https://www.youtube.com/playlist?list=PL67E0627174F36FCF).
