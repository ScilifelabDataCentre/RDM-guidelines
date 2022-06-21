---
title: Sharing phase
menu:
    bottom_about:
        name: Share
        identifier: share
        weight: 10
toc: True
---

## Sharing

In the era of [FAIR](/topic/topic/fair-principles.md) (Findable, Accessible, Interoperable and Reusable) and [Open science](https://www.vr.se/english/mandates/open-science/open-access-to-research-data.html), datasets should be made available to the public. Whenever possible, domain-specific repositories should be used in order to increase the FAIRness of your research outputs.

<!-- Put the text below into selectable/expandable sections -->
<div id="dwbuttons"><button class="btn btn-secondary" type="button" data-toggle="collapse" data-target="#collapseExample" aria-expanded="False" aria-controls="collapseExample">
Genomics data
</button>
</div>
<div class="collapse" id="collapseExample">
  <div class="card card-body">
    <span><h3> <a href="https://www.ebi.ac.uk/ena">ENA</a> (European Nucleotide Archive)</h3>
The ENA hosts an instance of the Sequence Read Archive (SRA), the same archive that exists on NCBI. SRA accepts raw sequence data from any sequencing platform, generated in any research project.

There are several ways to <a href="https://www.ebi.ac.uk/ena/submit">submit</a> data to ENA, for more information see the <a href="https://ena-docs.readthedocs.io/en/latest/">documentation</a>.

 </span>
  </div>
</div>

### Genomics data
#### [ENA](https://www.ebi.ac.uk/ena) (European Nucleotide Archive)
The ENA hosts an instance of the Sequence Read Archive (SRA), the same archive that exists on NCBI. SRA accepts raw sequence data from any sequencing platform, generated in any research project.

There are several ways to [submit](https://www.ebi.ac.uk/ena/submit) data to ENA, for more information see the [documentation](https://ena-docs.readthedocs.io/en/latest/).

#### [ArrayExpress](https://www.ebi.ac.uk/arrayexpress/)
ArrayExpress is tighty integrated with ENA and similar to NCBI’s Gene Expression Omnibus database it can be used to archive experimental designs and analysis files based on the raw sequence reads.

ArrayExpress has its own [submission portal](https://www.ebi.ac.uk/arrayexpress/submit/overview.html) where information is available on what can be submitted and how.

#### [EGA](https://ega-archive.org/) (European Genome-phenome Archive)
NBIS is building a local federated version of the European Genome-phenome Archive (EGA) in Sweden (EGA-SE), allowing for the publication of sensitive personal data within a legal framework. Until local EGA is available, the dataset should remain in the secure analysis environment (eg at Bianca on Uppmax). We suggest to make a metadata-only record in the [SciLifeLab Data Repository](https://www.scilifelab.se/community-pages/systems-data/repository/) with contact details on how to get access, and for which a DOI (ie a persistent identifier) can be issued. The DOI can then be used in the article to refer to the dataset. Once the Swedish EGA is operational, and the dataset deposited there, the access information can be changed to point at the EGA ID. See <https://doi.org/10.17044/scilifelab.12292778>, for an example.

### Imaging data
Depending on the type of image data you have, different public repositories are available, please see the table at [BioImage Archive](https://www.ebi.ac.uk/bioimage-archive/).

### Metabolomics data
[MetaboLights](https://www.ebi.ac.uk/metabolights/) is a database for Metabolomics experiments and derived information. The database is cross-species, cross-technique and covers metabolite structures and their reference spectra as well as their biological roles, locations and concentrations, and experimental data from metabolic experiments.

### Proteomics data
[ProteomeXchange](http://www.proteomexchange.org/) Consortium provide globally coordinated standard data submission and dissemination pipelines involving the main proteomics repositories:

* [PRIDE](https://www.ebi.ac.uk/pride/) - admits protein and peptide identification/quantification data with the accompanying mass spectra evidence and any other related data types. Submission is done using the [PX Submission Tool](https://www.ebi.ac.uk/pride/markdownpage/pridesubmissiontool), see [tutorial](https://www.ebi.ac.uk/pride/static/markdown/submitdatapage/files/Submission_Tutorial.pdf).
* [PeptideAtlas](http://www.peptideatlas.org/) - for SRM/MRM data that does not fit into PRIDE (targeted datasets). Submission is done via [PASSEL](http://www.peptideatlas.org/passel/).

### Other repositories
For other domain-specific repositories, see e.g. [ELIXIR Deposition databases](https://elixir-europe.org/services/tag/elixir-deposition-databases), [Scientific Data recommended repositories](https://www.nature.com/sdata/policies/repositories), [EBI archive wizard](https://www.ebi.ac.uk/submission/) (help to find the right repository depending on data type), or [FAIRsharing](https://fairsharing.org/databases/) (the latter can also assist in finding metadata standards suitable for describing your datasets). For datasets that do not fit into domain-specific repositories, use a general repository e.g. [SciLifeLab Data Repository](https://www.scilifelab.se/community-pages/systems-data/repository/)), [Figshare](https://figshare.com/) and [Zenodo](https://zenodo.org/).
<!-- end of expandable section -->

## Resources
* [RDMkit on Sharing Data](https://rdmkit.elixir-europe.org/sharing)

## Training
* [Data publication module](https://nbisweden.github.io/module-data-publication-dm-practices/) in course [Introduction to data management practices](https://uppsala.instructure.com/courses/48087/pages/introduction-to-data-management-practices)
* Many of the repositories at EBI have instructive videos on how to do submission as well as documentation.