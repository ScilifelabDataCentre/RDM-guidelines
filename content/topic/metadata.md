---
title: Metadata
menu:
    bottom_about:
        name: Metadata
        identifier: metadata
        weight: 10
toc: True
---

## Metadata 
Good documentation in research projects is essential in order to allow good quality data and transparent research. Describing how the datasets were created, how they are structured, and what they mean, is key for making your data understandable for others as well as your future self. Metadata provides such 'data about data'. 
Metadata is needed at several levels to describe the study, the samples, the experiments, the analysis and so on. It may include information on the methodology and instrumentation used to collect the data, analytical and procedural information, definitions of variables, units of measurement, any assumptions made, the format and file type of the data and software used to collect and/or process the data.

Researchers are strongly encouraged to use community metadata standards where these are in place (see further down) and recommended to do so already from the beginning of the project. Data repositories may also provide guidance about appropriate metadata standards and requirements e.g. the European Nucleotide Archive (ENA) have [ENA sample checklists](https://www.ebi.ac.uk/ena/submit/checklists). Structuring the metadata in a way that conforms to the suitable repository from the beginning enables data submission without having to reformat the metadata.

## Ontologies

Ontologies, controlled vocabularies and data dictionaries are used to standardize the language used to describe the metadata. Think of the many ways to write that the organism is human (human, Human, homo sapiens, H. sapiens, Homo Sapiens, man, etc), using an ontology such as [NCBI taxonomy](https://www.ebi.ac.uk/ols/ontologies/ncbitaxon) unifies the language and makes it easier for both humans and machines to interpret and work with the data. While an ontology has a hierarchical structure (e.g. *homo sapiens* is a *mammalia* which is a *eukaryota*), a controlled vocabulary is an unstructured set of terms, but fills the same purpose, to standardize the language used. A [Data Dictionary](https://help.osf.io/hc/en-us/articles/360019739054-How-to-Make-a-Data-Dictionary) is a user-defined way of describing what all the variable names and values in the data really mean. 

For a suggested list of ontologies appropriate for Life Science community please see [FAIRsharing.org](https://fairsharing.org/search?recordType=terminology_artefact&status=ready&subjects=life%2520science), filter on e.g. Domain.

Below are ontology resources, adapted from Table 2 in *Griffin PC, Khadake J, LeMay KS et al. Best practice data life cycle approaches for the life sciences. F1000Research 2018, 6:1618.* doi: [https://doi.org/10.12688/f1000research.12344.2](https://doi.org/10.12688/f1000research.12344.2):

* [Ontology Lookup Service](https://www.ebi.ac.uk/ols/) - Discover different ontologies and their contents.
* [OBO Foundry](https://obofoundry.org/) - Table of open biomedical ontologies with information on development status, license and content.
* [ZOOMA](https://www.ebi.ac.uk/spot/zooma/) - Assign ontology terms using curated mapping.
* [Ontobee](https://www.ontobee.org) - A linked data server that facilitates ontology data sharing, visualization, and use.

## Data and metadata standards 
Curated up-to-date guidance regarding file types and metadata standards is found at [FAIRsharing.org](https://fairsharing.org/search?fairsharingRegistry=Standard/). Click on the buttons below for data type specific information, queries and examples adapted from _RDA COVID-19 Working Group. Recommendations and Guidelines on data sharing. Research Data Alliance. 2020._ doi: (https://doi.org/10.15497/rda00052)[https://doi.org/10.15497/rda00052]

<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample1" role="button" aria-expanded="false" aria-controls="collapseExample1">
    Genomics data
  </a>
</p>
<div class="collapse" id="collapseExample1">
  <div class="card card-body">
  <span>
  A list of relevant data and metadata standards can be found in <a href="https://fairsharing.org/search?q=sequence&fairsharingRegistry=Standard&status=ready&page=1">FAIRsharing</a>, some specific examples are below.<br><br>
  <h5> Gene expression - Transcriptomics</h5>
  <ul>
    <li>Preferred minimal metadata standard: <a href="https://doi.org/10.25504/FAIRsharing.a55z32">MINSEQE</a></li>
    <li> Preferred file formats (sequencing-based):
      <ul>
        <li> Raw sequences: <a href="https://doi.org/10.25504/FAIRsharing.r2ts5t">.fastq</a> (compression can be added with gzip)</li>
        <li> Mapped sequences: <a href="https://doi.org/10.25504/FAIRsharing.k97xzh">.sam</a> (compression with <a href="https://doi.org/10.25504/FAIRsharing.hza1ec">.bam</a> or <a href="https://doi.org/10.25504/FAIRsharing.f846bd">.cram</a>). Please ensure that the used reference sequence is also publically available and that the @SQ header is present and unambiguously describes the used reference sequence.</li>
        <li> Transcripts per million (TPM): <a href="https://tools.ietf.org/html/rfc4180">.csv</a></li>
        <li> Gene Structure: <a href="https://doi.org/10.25504/FAIRsharing.sggb1n">.gtf</a></li>
        <li> Gene Features: <a href="https://doi.org/10.25504/FAIRsharing.dnk0f6">.gff</a></li>
        <li> Variant calling: <a href="https://doi.org/10.25504/FAIRsharing.cfzz0h">.vcf</a>. Please ensure that the used reference sequence is also publically available and that it is unambiguously referenced in the header of the .vcf file, e.g. using the URL field of the ##contig field.</li>
      </ul>
    </li>
  </ul>
  <h5> Gene expression - Microarray-based</h5>
  <ul>
    <li>Preferred minimal metadata standard: <a href="https://doi.org/10.25504/FAIRsharing.32b10v">MIAME</a></li>
    <li>Preferred file formats: tab-delimited text e.g. <a href="https://doi.org/10.25504/FAIRsharing.ak8p5g">MAGE-TAB</a> and <a href="https://doi.org/10.25504/FAIRsharing.53gp75">ISA-TAB</a>, and raw data file formats from commercial microarray platforms (<a href="https://www.ebi.ac.uk/fg/annotare/help/accepted_raw_ma_file_formats.html">Annotare accepted formats</a>)</li>
  </ul>
  <h5> Genome-wide association studies (GWAS):</h5>
  <ul>
    <li>Preferred minimal metadata standard: <a href="https://doi.org/10.25504/FAIRsharing.9aa0zp">MIxS</a>
    <li>Preferred file formats 
      <ul>
        <li>for binary files: <a href="https://doi.org/10.25504/FAIRsharing.b52795">.bim</a>, <a href="https://doi.org/10.25504/FAIRsharing.d0886a">.fam</a> and <a href="https://doi.org/10.25504/FAIRsharing.mwmbpq">.bed</a></li>
        <li>for text-format files: <a href="https://doi.org/10.25504/FAIRsharing.31385c">.ped</a> and <a href="https://doi.org/10.25504/FAIRsharing.53edcc">.map</a></li>
      </ul>
    </li>
  </ul>
  <h5> Metagenomics</h5>
  <ul>
    <li><a href="https://doi.org/10.25504/FAIRsharing.va1hck">MIxS - MIGS/MIMS</a> - 
    Minimum Information about a (Meta)Genome Sequence. The MIMS extension includes key environmental metadata. Developed by the Genomic Standards Consortium. Numerous adopters including NCBI/EBI/DDBJ databases. </li> 
    <li><a href="https://doi.org/10.25504/FAIRsharing.zvrep1">MIMARKS</a> - 
    Minimum Information about a MARKer gene Sequence. This is an extension of MIGS/MIMS for environmental sequences. Developed by the Genomic Standards Consortium. Numerous adopters including NCBI/EBI/DDBJ databases.</li>  
  </ul>
  <h5>Functional Annotation of Animal Genomes Consortium (FAANG) standards</h5>
  <ul>
    <li><a href="https://doi.org/10.25504/FAIRsharing.J1aPiC">FAANG sample metadata specification</a>:
    Metadata specification for biological samples derived from animals (animals, tissue samples, cells or other biological materials). Complies with EBI database requirements and <a href="https://www.ebi.ac.uk/biosamples/">BioSamples</a> database formats. </li>
    <li><a href="https://doi.org/10.25504/FAIRsharing.fztr98">FAANG experimental metadata specification</a>:
    Metadata specification for sequencing and array experiments on animal samples.</li>
  </ul>
  </span>
  </div>
</div>

<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample2" role="button" aria-expanded="false" aria-controls="collapseExample2">
    Imaging / Structural data
  </a>
</p>
<div class="collapse" id="collapseExample2">
  <div class="card card-body">
  <span>
      <h5>X-ray diffraction</h5>
      There are no widely accepted standards for X-ray raw data files. Generally these are stored and archived in the Vendor’s native formats. Metadata is stored in CBF/<a href="https://doi.org/10.25504/FAIRsharing.zr52g5">imgCIF</a> format (see: <a href="https://www.iucr.org/resources/data/dddwg/metadata-catalogue">catalogue of metadata resources for crystallographic applications</a>). <br><br>
      Processed structural information is submitted to structural databases in the <a href="https://doi.org/10.25504/FAIRsharing.fd28en">PDBx/.mmCIF</a> format.<br><br>
      <h5>Electron microscopy</h5>
      <ul>
        <li>Data archiving and validation standards for cryo-EM maps and models are coordinated internationally by <a href="https://emdataresource.org/">EMDataResource</a> (EMDR).</li>
        <li>Cryo-EM structures (map, experimental metadata, and optionally coordinate model) are deposited and processed through the <a href="https://deposit-2.wwpdb.org/">wwPDB OneDep system</a>, following the same annotation and validation workflow also used for X-ray crystallography and nuclear magnetic resonance (NMR) structures. EMDB holds all workflow metadata while PDB holds a subset of the metadata.</li>
        <li>Most electron microscopy data is stored in either raw data formats (binary, bitmap images, tiff, etc.) or proprietary formats developed by vendors (dm3, emispec, etc.).</li>
        <li>Processed structural information is submitted to structural resources as <a href="https://doi.org/10.25504/FAIRsharing.fd28en">PDBx/mmCIF</a>.</li>
        <li>Experimental metadata include information about the sample, specimen preparation, imaging, image processing, symmetry, reconstruction method, resolution and resolution method, as well as a description of the modeling/fitting procedures used and are described in <a href="https://emdataresource.org/">EMDR</a>, see also <a href="https://aca.scitation.org/doi/10.1063/1.5138589">Lawson et al 2020</a>.</li>
      </ul>
      <h5>NMR</h5>
      <ul>
        <li>There are no widely accepted standards for NMR raw data files. Generally these are stored and archived in single FID/SER files.</li>
        <li>One effort for the standardization of NMR parameters extracted from 1D and 2D spectra of organic compounds to the proposed chemical structure is the <a href="https://doi.org/10.25504/FAIRsharing.8ae3d0">NMReDATA</a> format.</li>
        <li>There is no universally accepted format, especially for crucial FID-associated metadata. <a href="https://doi.org/10.25504/FAIRsharing.2chxxc">NMR-STAR</a> and its <a href="https://github.com/uwbmrb/nmr-star-dictionary">NMR-STAR Dictionary</a> is the archival format used by the <a href="https://bmrb.io/">Biological Nuclear Magnetic Resonance data Bank</a> (BMRB), the international repository of biomolecular NMR data and an archive of the <a href="https://www.wwpdb.org/">Worldwide Protein Data Bank</a> (wwPDB).</li>
        <li>The <a href="https://doi.org/10.25504/FAIRsharing.es03fk">nmrML format specification</a> (XML Schema Definition (XSD) and an accompanying controlled vocabulary called nmrCV) are an open mark up language and ontology for NMR data.</li>
        <li>Processed structural information is submitted in the <a href="https://doi.org/10.25504/FAIRsharing.fd28en/">PDBx/mmCIF</a> format.</li>
      </ul>
      <h5>Neutron scattering</h5>
      <ul>
        <li>ENDF/B-VI of Cross-Section Evaluation Working Group (<a href="https://www.nndc.bnl.gov/csewg/">CSEWG</a>) and JEFF of OECD/NEA have been widely utilized in the nuclear community. The latest versions of the two nuclear reaction data libraries are <a href="https://doi.org/10.25504/FAIRsharing.4ed3fb">JEFF-3.3</a> and ENDF/B-VIII.0 (<a href="https://www.sciencedirect.com/science/article/pii/S0969804319301484#bib3">Brown et al., 2018</a>) with a significant upgrade in data for a number of nuclides (<a href="https://www.sciencedirect.com/science/article/pii/S0969804319301484#bib6">Carlson et al., 2018</a>).</li>
        <li>Neutron scattering data are stored in the internationally-adopted <a href="https://www.oecd-nea.org/dbdata/data/manual-endf/endf102.pdf">ENDF-6</a> format maintained by <a href="https://www.nndc.bnl.gov/csewg/">CSEWG</a>.</li>
        <li>Processed structural information is submitted in the <a href="https://doi.org/10.25504/FAIRsharing.fd28en/">PDBx/mmCIF</a> format.</li>
      </ul>
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
    For a curated list of relevant standards see <a href="https://fairsharing.org">FAIRsharing</a> using the query ‘<a href="https://fairsharing.org/search?q=metabolomics&fairsharingRegistry=Standard&page=1&status=ready">metabolomics</a>’.
    <ul>
      <li>Core Information for Metabolomics Reporting <a href="https://doi.org/10.25504/FAIRsharing.exz30t">CIMR</a> standard</li>
      <li>For identifying chemical compounds use <a href="https://doi.org/10.25504/FAIRsharing.qv4b3c">SMILES</a> or <a href="https://doi.org/10.25504/FAIRsharing.ddk9t9">InChl</a></li>
      <li>To document Investigation/Study/Assay data, use the <a href="https://isa-specs.readthedocs.io/en/latest/">ISA Abstract Model</a>, also implemented as a tabular format, <a href="https://doi.org/10.25504/FAIRsharing.53gp75">ISA-Tab</a> in <a href="https://www.ebi.ac.uk/metabolights">MetaboLights</a>. For an introduction to ISA, see (<a href="https://doi.org/10.1038/ng.1054">Sansone S-A et al., 2012</a>)</li>
      <li>Recommended formats for LC-MS data: <a href="https://doi.org/10.25504/FAIRsharing.d7795c">ANDI-MS</a> specification, an analytical data interchange protocol for chromatographic data representation and/or <a href="https://doi.org/10.25504/FAIRsharing.26dmba">mzML</a>
      <li>Recommended formats for NMR data: <a href="https://doi.org/10.25504/FAIRsharing.xm7tkj">nmrCV</a>, <a href="https://doi.org/10.25504/FAIRsharing.es03fk">nmrML</a></li>
    </ul>
  </span>
  </div>
</div>

<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample4" role="button" aria-expanded="false" aria-controls="collapseExample4">
    Lipidomics data
  </a>
</p>
<div class="collapse" id="collapseExample4">
  <div class="card card-body">
  <span>
  <ul>
    <li>Metadata should follow recommendations from the <a href="https://doi.org/10.25504/FAIRsharing.exz30t">CIMR standard</a> by the Metabolomics Standards Initiative. It should be made available as tab or comma separated files (.tsv or .csv).</li>
    <li>Data can be stored in LC-MS file,  in tab (.tsv) or comma (.csv) separated formats.</li>
  </ul>
  </span>
  </div>
</div>

<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample5" role="button" aria-expanded="false" aria-controls="collapseExample5">
    Proteomics data
  </a>
</p>
<div class="collapse" id="collapseExample5">
  <div class="card card-body">
  <span>
  For a curated list of relevant standards see <a href="https://fairsharing.org">FAIRsharing</a> using the query ’<a href="https://fairsharing.org/search/?q=proteomics&fairsharingRegistry=Standard&page=1&status=ready">proteomics</a>’ 

  <ul>
    <li>Use the minimal information model specified in <a href="https://doi.org/10.25504/FAIRsharing.8vv5fc">MIAPE</a> by the HUPO Proteomics Standards Initiative (<a href="https://hupo.org/Proteomics-Standards-Initiative">HUPO PSI</a>), and fill the model using the controlled vocabularies specified by the Proteomics Standards Initiative: <a href="https://doi.org/10.25504/FAIRsharing.sxh2dp">PSI-MS CV</a></li>
    <li>Recommended formats: 
      <ul>
        <li>For gel electrophoresis <a href="https://doi.org/10.25504/FAIRsharing.rn9wzc">PSI gelML</a></li>
        <li>For transition lists <a href="https://doi.org/10.25504/FAIRsharing.rz77m6">HUPO-PSI TraML</a></li>
        <li>For raw spectrometer output <a href="https://doi.org/10.25504/FAIRsharing.26dmba">mzML</a></li>
        <li>For reporting <a href="https://doi.org/10.25504/FAIRsharing.c12tyk">mzTab</a></li>
        <li>For protein quantisation data <a href="https://doi.org/10.25504/FAIRsharing.fk6zhb">mzQuantML</a></li>
        <li>For protein identification data <a href="https://doi.org/10.25504/FAIRsharing.11889">mzIdentML</a></li>
        <li>For metadata <a href="https://isa-tools.org/">ISA-TAB</a> with conversion to PRIDE format</li>
      </ul>
    </li>
  </ul>
  </span>
  </div>
</div>

## Resources & Training
* [RDMkit on Metadata](https://rdmkit.elixir-europe.org/metadata_management)
* [Metadata module](https://nbisweden.github.io/module-metadata-dm-practices/) in course [Introduction to data management practices](https://uppsala.instructure.com/courses/48087/pages/introduction-to-data-management-practices)
