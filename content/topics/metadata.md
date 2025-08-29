---
title: Metadata
category: Other
toc: True
---

# Metadata
Good documentation in research projects is essential in order to allow good quality data and transparent research. Describing how the datasets were created, how they are structured, and what they mean, is key for making your data understandable for others as well as your future self. Metadata provides such 'data about data'.
Metadata is needed at several levels to describe the study, the samples, the experiments, the analysis and so on (see also topic on [README](/topics/readme-files/) for documentation on different levels). It may include information on the methodology and instrumentation used to collect the data, analytical and procedural information, definitions of variables, units of measurement, any assumptions made, the format and file type of the data and software used to collect and/or process the data.

Researchers are strongly encouraged to use community metadata standards where these are in place (see further down) and are recommended doing so already from the beginning of the project. Data repositories may also provide guidance about appropriate metadata standards and requirements e.g. the European Nucleotide Archive (ENA) have sample checklists. We provide templates for some of these checklists, see further on [Sharing phase - ENA](/data-life-cycle/share/#genomics-data). Structuring the metadata in a way that conforms to the suitable repository from the beginning enables data submission without having to reformat the metadata.


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

## Data types, file formats and metadata standards
Curated up-to-date guidance regarding file types and metadata standards is found at FAIRsharing.org. The most common ones, including links with data type specific FAIRsharing queries, is listed below. The information is adapted from _RDA COVID-19 Working Group. Recommendations and Guidelines on data sharing. Research Data Alliance. 2020._ doi: <a href="https://doi.org/10.15497/rda00052" target="_blank">10.15497/rda00052</a>

<a class="link-teal" href="https://fairsharing.org/search?fairsharingRegistry=Standard/" target="_blank"><b>Visit FAIRsharing.org <i class="bi bi-box-arrow-up-right"></i></b></a>
<br/><br/>

### Genomics data

A list of relevant data and metadata standards can be found in FAIRsharing, some specific examples are below.

<p>
  <a class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample1" role="button" aria-expanded="false" aria-controls="collapseExample1">
    Gene expression - Transcriptomics
    <i class="bi bi-chevron-double-down p-2"></i>
  </a>
</p>
<div class="collapse" id="collapseExample1">
  <div class="card card-body">
  <span>
  <ul>
    <li>Preferred minimal metadata standard: <a href="https://doi.org/10.25504/FAIRsharing.a55z32" target="_blank">MINSEQE</a> - Minimal Information about a high throughput SEQuencing Experiment</li>
    <li> Preferred file formats (sequencing-based):
      <ul>
        <li> Raw sequences: <a href="https://doi.org/10.25504/FAIRsharing.r2ts5t" target="_blank">.fastq</a> (compression can be added with gzip)</li>
        <li> Mapped sequences: <a href="https://doi.org/10.25504/FAIRsharing.k97xzh" target="_blank">.sam</a> (compression with <a href="https://doi.org/10.25504/FAIRsharing.hza1ec" target="_blank">.bam</a> or <a href="https://doi.org/10.25504/FAIRsharing.f846bd" target="_blank">.cram</a>). Please ensure that the used reference sequence is also publically available and that the @SQ header is present and unambiguously describes the used reference sequence.</li>
        <li> Transcripts per million (TPM): <a href="https://tools.ietf.org/html/rfc4180" target="_blank">.csv</a></li>
        <li> Gene Structure: <a href="https://doi.org/10.25504/FAIRsharing.sggb1n" target="_blank">.gtf</a></li>
        <li> Gene Features: <a href="https://doi.org/10.25504/FAIRsharing.dnk0f6" target="_blank">.gff</a></li>
        <li> Variant calling: <a href="https://doi.org/10.25504/FAIRsharing.cfzz0h" target="_blank">.vcf</a>. Please ensure that the used reference sequence is also publically available and that it is unambiguously referenced in the header of the .vcf file, e.g. using the URL field of the ##contig field.</li>
      </ul>
    </li>
  </ul>
  </span>
  </div>
</div>

<p>
  <a class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample2" role="button" aria-expanded="false" aria-controls="collapseExample2">
    Gene expression - Microarray-based
    <i class="bi bi-chevron-double-down p-2"></i>
  </a>
</p>
<div class="collapse" id="collapseExample2">
  <div class="card card-body">
  <span>
  <ul>
    <li>Preferred minimal metadata standard: <a href="https://doi.org/10.25504/FAIRsharing.32b10v" target="_blank">MIAME</a> - Minimum Information About a Microarray Experiment</li>
    <li>Preferred file formats:
      <ul>
        <li>tab-delimited text e.g. <a href="https://doi.org/10.25504/FAIRsharing.ak8p5g" target="_blank">MAGE-TAB</a> and <a href="https://doi.org/10.25504/FAIRsharing.53gp75" target="_blank">ISA-TAB</a></li>
        <li>raw data file formats from commercial microarray platforms (see <a href="https://www.ebi.ac.uk/fg/annotare/help/accepted_raw_ma_file_formats.html" target="_blank">Annotare accepted formats</a>)</li>
      </ul>
  </ul>
  </span>
  </div>
</div>

<p>
  <a class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample3" role="button" aria-expanded="false" aria-controls="collapseExample3">
    Genome-wide association studies (GWAS)
    <i class="bi bi-chevron-double-down p-2"></i>
  </a>
</p>
<div class="collapse" id="collapseExample3">
  <div class="card card-body">
  <span>
  <ul>
    <li>Preferred minimal metadata standard: <a href="https://doi.org/10.25504/FAIRsharing.9aa0zp" target="_blank">MIxS</a> - Minimum Information about any (x) Sequence
    <li>Preferred file formats
      <ul>
        <li>for binary files: <a href="https://doi.org/10.25504/FAIRsharing.b52795" target="_blank">.bim</a>, <a href="https://doi.org/10.25504/FAIRsharing.d0886a" target="_blank">.fam</a> and <a href="https://doi.org/10.25504/FAIRsharing.mwmbpq" target="_blank">.bed</a></li>
        <li>for text-format files: <a href="https://doi.org/10.25504/FAIRsharing.31385c" target="_blank">.ped</a> and <a href="https://doi.org/10.25504/FAIRsharing.53edcc" target="_blank">.map</a></li>
      </ul>
    </li>
  </ul>
  </span>
  </div>
</div>

<p>
  <a class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample4" role="button" aria-expanded="false" aria-controls="collapseExample4">
    Metagenomics
    <i class="bi bi-chevron-double-down p-2"></i>
  </a>
</p>
<div class="collapse" id="collapseExample4">
  <div class="card card-body">
  <span>
  <ul>
    <li>Preferred metadata standards:
      <ul>
        <li><a href="https://doi.org/10.25504/FAIRsharing.va1hck" target="_blank">MIxS - MIGS/MIMS</a> -
        Minimum Information about a (Meta)Genome Sequence. The MIMS extension includes key environmental metadata. Developed by the Genomic Standards Consortium. Numerous adopters including NCBI/EBI/DDBJ databases. </li>
        <li><a href="https://doi.org/10.25504/FAIRsharing.zvrep1" target="_blank">MIMARKS</a> -
        Minimum Information about a MARKer gene Sequence. This is an extension of MIGS/MIMS for environmental sequences. Developed by the Genomic Standards Consortium. Numerous adopters including NCBI/EBI/DDBJ databases.</li>  
      </ul>
    </li>
  </ul>
  </span>
  </div>
</div>
&nbsp;

### Imaging / Structural data
Images and structural data cover a wide range of data types and thus metadata standards. Please find below guidance for a selection of them.
<p>
  <a class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample5" role="button" aria-expanded="false" aria-controls="collapseExample5">
    X-ray diffraction
    <i class="bi bi-chevron-double-down p-2"></i>
  </a>
</p>
<div class="collapse" id="collapseExample5">
  <div class="card card-body">
  <span>
      There are no widely accepted standards for X-ray raw data files. Generally these are stored and archived in the Vendor’s native formats. Metadata is stored in CBF/<a href="https://doi.org/10.25504/FAIRsharing.zr52g5" target="_blank">imgCIF</a> format (see: <a href="https://www.iucr.org/resources/data/dddwg/metadata-catalogue" target="_blank">catalogue of metadata resources for crystallographic applications</a>). <br><br>
      Processed structural information is submitted to structural databases in the <a href="https://doi.org/10.25504/FAIRsharing.fd28en" target="_blank">PDBx/.mmCIF</a> format.
    </span>
  </div>
  <br>
</div>

<p>
  <a class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample6" role="button" aria-expanded="false" aria-controls="collapseExample6">
    Electron microscopy
    <i class="bi bi-chevron-double-down p-2"></i>
  </a>
</p>
<div class="collapse" id="collapseExample6">
  <div class="card card-body">
  <span>
      <ul>
        <li>Data archiving and validation standards for cryo-EM maps and models are coordinated internationally by <a href="https://emdataresource.org/" target="_blank">EMDataResource</a> (EMDR).</li>
        <li>Cryo-EM structures (map, experimental metadata, and optionally coordinate model) are deposited and processed through the <a href="https://deposit-2.wwpdb.org/" target="_blank">wwPDB OneDep system</a>, following the same annotation and validation workflow also used for X-ray crystallography and nuclear magnetic resonance (NMR) structures. EMDB holds all workflow metadata while PDB holds a subset of the metadata.</li>
        <li>Most electron microscopy data is stored in either raw data formats (binary, bitmap images, tiff, etc.) or proprietary formats developed by vendors (dm3, emispec, etc.).</li>
        <li>Processed structural information is submitted to structural resources as <a href="https://doi.org/10.25504/FAIRsharing.fd28en" target="_blank">PDBx/mmCIF</a>.</li>
        <li>Experimental metadata include information about the sample, specimen preparation, imaging, image processing, symmetry, reconstruction method, resolution and resolution method, as well as a description of the modeling/fitting procedures used and are described in <a href="https://emdataresource.org/" target="_blank">EMDR</a>, see also <a href="https://aca.scitation.org/doi/10.1063/1.5138589" target="_blank">Lawson et al 2020</a>.</li>
      </ul>
  </span>
  </div>
</div>

<p>
  <a class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample7" role="button" aria-expanded="false" aria-controls="collapseExample7">
    NMR
    <i class="bi bi-chevron-double-down p-2"></i>
  </a>
</p>
<div class="collapse" id="collapseExample7">
  <div class="card card-body">
  <span>
      <ul>
        <li>There are no widely accepted standards for NMR (Nucleic Magnetic Resonance) raw data files. Generally these are stored and archived in single FID/SER files.</li>
        <li>One effort for the standardization of NMR parameters extracted from 1D and 2D spectra of organic compounds to the proposed chemical structure is the <a href="https://doi.org/10.25504/FAIRsharing.8ae3d0" target="_blank">NMReDATA</a> format.</li>
        <li>There is no universally accepted format, especially for crucial FID-associated metadata. <a href="https://doi.org/10.25504/FAIRsharing.2chxxc" target="_blank">NMR-STAR</a> and its <a href="https://github.com/uwbmrb/nmr-star-dictionary" target="_blank">NMR-STAR Dictionary</a> is the archival format used by the <a href="https://bmrb.io/" target="_blank">Biological Nuclear Magnetic Resonance data Bank</a> (BMRB), the international repository of biomolecular NMR data and an archive of the <a href="https://www.wwpdb.org/" target="_blank">Worldwide Protein Data Bank</a> (wwPDB).</li>
        <li>The <a href="https://doi.org/10.25504/FAIRsharing.es03fk" target="_blank">nmrML format specification</a> (XML Schema Definition (XSD) and an accompanying controlled vocabulary called nmrCV) is an open mark up language and ontology for NMR data.</li>
        <li>Processed structural information is submitted in the <a href="https://doi.org/10.25504/FAIRsharing.fd28en" target="_blank">PDBx/mmCIF</a> format.</li>
      </ul>
  </span>
  </div>
</div>

<p>
  <a class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseExample8" role="button" aria-expanded="false" aria-controls="collapseExample8">
    Neutron scattering
    <i class="bi bi-chevron-double-down p-2"></i>
  </a>
</p>
<div class="collapse" id="collapseExample8">
  <div class="card card-body">
  <span>
      <ul>
        <li>ENDF/B-VI of Cross-Section Evaluation Working Group (<a href="https://www.nndc.bnl.gov/csewg/" target="_blank">CSEWG</a>) and JEFF of OECD/NEA have been widely utilized in the nuclear community. The latest versions of the two nuclear reaction data libraries are <a href="https://doi.org/10.25504/FAIRsharing.4ed3fb" target="_blank">JEFF-3.3</a> and ENDF/B-VIII.0 (<a href="https://www.sciencedirect.com/science/article/pii/S0969804319301484#bib3" target="_blank">Brown et al., 2018</a>) with a significant upgrade in data for a number of nuclides (<a href="https://www.sciencedirect.com/science/article/pii/S0969804319301484#bib6" target="_blank">Carlson et al., 2018</a>).</li>
        <li>Neutron scattering data are stored in the internationally-adopted <a href="https://www.oecd-nea.org/dbdata/data/manual-endf/endf102.pdf" target="_blank">ENDF-6</a> (PDF) format maintained by <a href="https://www.nndc.bnl.gov/csewg/" target="_blank">CSEWG</a>.</li>
        <li>Processed structural information is submitted in the <a href="https://doi.org/10.25504/FAIRsharing.fd28en" target="_blank">PDBx/mmCIF</a> format.</li>
      </ul>
  </span>
  </div>
</div>
&nbsp;

### Metabolomics data

A selection of standards appropriate for metabolomics data are given below, for a more complete list please see FAIRsharing.org:

* Core Information for Metabolomics Reporting <a href="https://doi.org/10.25504/FAIRsharing.exz30t" target="_blank">CIMR</a> standard
* For identifying chemical compounds use <a href="https://doi.org/10.25504/FAIRsharing.qv4b3c" target="_blank">SMILES</a> or <a href="https://doi.org/10.25504/FAIRsharing.ddk9t9" target="_blank">InChl</a>
* To document Investigation/Study/Assay data, use the <a href="https://isa-specs.readthedocs.io/en/latest/" target="_blank">ISA Abstract Model</a>, also implemented as a tabular format, <a href="https://doi.org/10.25504/FAIRsharing.53gp75" target="_blank">ISA-Tab</a> in <a href="https://www.ebi.ac.uk/metabolights" target="_blank">MetaboLights</a>. For an introduction to ISA, see (<a href="https://doi.org/10.1038/ng.1054" target="_blank">Sansone S-A et al., 2012</a>)
* Recommended formats for LC-MS data: <a href="https://doi.org/10.25504/FAIRsharing.d7795c" target="_blank">ANDI-MS</a> specification, an analytical data interchange protocol for chromatographic data representation and/or <a href="https://doi.org/10.25504/FAIRsharing.26dmba" target="_blank">mzML</a>
* Recommended formats for NMR data: <a href="https://doi.org/10.25504/FAIRsharing.xm7tkj" target="_blank">nmrCV</a>, <a href="https://doi.org/10.25504/FAIRsharing.es03fk" target="_blank">nmrML</a>

<a class="link-teal" href="https://fairsharing.org/search?q=metabolomics&fairsharingRegistry=Standard&page=1&status=ready" target="_blank"><b>Browse metabolomics standards on FAIRsharing.org <i class="bi bi-box-arrow-up-right"></i></b></a>

&nbsp;

### Lipidomics data

* Metadata should follow recommendations from the <a href="https://doi.org/10.25504/FAIRsharing.exz30t" target="_blank">CIMR standard</a> by the Metabolomics Standards Initiative. It should be made available as tab or comma separated files (.tsv or .csv).
* Data can be stored in LC-MS file,  in tab (.tsv) or comma (.csv) separated formats.

&nbsp;

### Proteomics data
A selection of standards appropriate for proteomics data are given below, for a more complete list please see FAIRsharing.org:

* Use the minimal information model specified in <a href="https://doi.org/10.25504/FAIRsharing.8vv5fc" target="_blank">MIAPE</a> by the HUPO Proteomics Standards Initiative (<a href="https://hupo.org/Proteomics-Standards-Initiative-(PSI)" target="_blank">HUPO PSI</a>), and fill the model using the controlled vocabularies specified by the Proteomics Standards Initiative: <a href="https://doi.org/10.25504/FAIRsharing.sxh2dp" target="_blank">PSI-MS CV</a>
* Recommended formats:
  * For gel electrophoresis: <a href="https://doi.org/10.25504/FAIRsharing.rn9wzc" target="_blank">PSI gelML</a>
  * For transition lists: <a href="https://doi.org/10.25504/FAIRsharing.rz77m6" target="_blank">HUPO-PSI TraML</a>
  * For raw spectrometer output: <a href="https://doi.org/10.25504/FAIRsharing.26dmba" target="_blank">mzML</a>
  * For reporting: <a href="https://doi.org/10.25504/FAIRsharing.c12tyk" target="_blank">mzTab</a>
  * For protein quantisation data: <a href="https://doi.org/10.25504/FAIRsharing.fk6zhb" target="_blank">mzQuantML</a>
  * For protein identification data: <a href="https://doi.org/10.25504/FAIRsharing.11889" target="_blank">mzIdentML</a>
  * For metadata: <a href="https://isa-tools.org/" target="_blank">ISA-TAB</a> with conversion to PRIDE format

<a class="link-teal" href="https://fairsharing.org/search/?q=proteomics&fairsharingRegistry=Standard&page=1&status=ready" target="_blank"><b>Browse proteomics standards on FAIRsharing.org <i class="bi bi-box-arrow-up-right"></i></b></a>


&nbsp;

## Resources
Please find below resources concerning metadata in form of training, guidance and/or tools.
{{< resources-per-page-topics >}}
