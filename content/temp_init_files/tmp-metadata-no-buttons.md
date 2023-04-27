---
title: Metadata
contributors: []
toc: True
---

# *Temporary file for exploring various ways of displaying metadata standards and file formats, with or without buttons*

# Metadata
Good documentation in research projects is essential in order to allow good quality data and transparent research. Describing how the datasets were created, how they are structured, and what they mean, is key for making your data understandable for others as well as your future self. Metadata provides such 'data about data'.
Metadata is needed at several levels to describe the study, the samples, the experiments, the analysis and so on. It may include information on the methodology and instrumentation used to collect the data, analytical and procedural information, definitions of variables, units of measurement, any assumptions made, the format and file type of the data and software used to collect and/or process the data.

Researchers are strongly encouraged to use community metadata standards where these are in place (see further down) and recommended doing so already from the beginning of the project. Data repositories may also provide guidance about appropriate metadata standards and requirements e.g. the European Nucleotide Archive (ENA) have [ENA sample checklists](https://www.ebi.ac.uk/ena/submit/checklists). We provide templates for some of these checklists, see further on [Sharing phase - ENA](/data-life-cycle/share/#genomics-data). Structuring the metadata in a way that conforms to the suitable repository from the beginning enables data submission without having to reformat the metadata.

## Ontologies

Ontologies, controlled vocabularies and data dictionaries are used to standardize the language used to describe the metadata. Think of the many ways to write that the organism is human (human, Human, homo sapiens, H. sapiens, Homo Sapiens, man, etc), using an ontology such as [NCBI taxonomy](https://www.ebi.ac.uk/ols/ontologies/ncbitaxon) unifies the language and makes it easier for both humans and machines to interpret and work with the data. While an ontology has a hierarchical structure (e.g. *homo sapiens* is a *mammalia* which is a *eukaryota*), a controlled vocabulary is an unstructured set of terms, but fills the same purpose, to standardize the language used. A [Data Dictionary](https://help.osf.io/hc/en-us/articles/360019739054-How-to-Make-a-Data-Dictionary) is a user-defined way of describing what all the variable names and values in the data really mean.

For a suggested list of ontologies appropriate for Life Science community please see [FAIRsharing.org](https://fairsharing.org/search?recordType=terminology_artefact&status=ready&subjects=life%2520science), filter on e.g. Domain.

Below are ontology resources, adapted from Table 2 in *Griffin PC, Khadake J, LeMay KS et al. Best practice data life cycle approaches for the life sciences. F1000Research 2018, 6:1618.* doi: [https://doi.org/10.12688/f1000research.12344.2](https://doi.org/10.12688/f1000research.12344.2):

* [Ontology Lookup Service](https://www.ebi.ac.uk/ols/) - Discover different ontologies and their contents.
* [OBO Foundry](https://obofoundry.org/) - Table of open biomedical ontologies with information on development status, license and content.
* [ZOOMA](https://www.ebi.ac.uk/spot/zooma/) - Assign ontology terms using curated mapping.
* [Ontobee](https://www.ontobee.org) - A linked data server that facilitates ontology data sharing, visualization, and use.

## Data types, file formats and metadata standards
Curated up-to-date guidance regarding file types and metadata standards is found at [FAIRsharing.org](https://fairsharing.org/search?fairsharingRegistry=Standard/). The most common ones, including links with data type specific FAIRsharing queries, is listed below. The information is adapted from _RDA COVID-19 Working Group. Recommendations and Guidelines on data sharing. Research Data Alliance. 2020._ doi: [https://doi.org/10.15497/rda00052](https://doi.org/10.15497/rda00052)

### Genomics data

A list of relevant data and metadata standards can be found in [FAIRsharing](https://fairsharing.org/search?q=sequence&fairsharingRegistry=Standard&status=ready&page=1), some specific examples are below.

**Gene expression - Transcriptomics**

* Preferred minimal metadata standard: [MINSEQE](https://doi.org/10.25504/FAIRsharing.a55z32) - Minimal Information about a high throughput SEQuencing Experiment
* Preferred file formats (sequencing-based):
  * Raw sequences: [.fastq](https://doi.org/10.25504/FAIRsharing.r2ts5t) (compression can be added with gzip)
  * Mapped sequences: [.sam](https://doi.org/10.25504/FAIRsharing.k97xzh) (compression with [.bam](https://doi.org/10.25504/FAIRsharing.hza1ec) or [.cram](https://doi.org/10.25504/FAIRsharing.f846bd)). Please ensure that the used reference sequence is also publically available and that the @SQ header is present and unambiguously describes the used reference sequence.
  * Transcripts per million (TPM): [.csv](https://tools.ietf.org/html/rfc4180)
  * Gene Structure: [.gtf](https://doi.org/10.25504/FAIRsharing.sggb1n)
  * Gene Features: [.gff](https://doi.org/10.25504/FAIRsharing.dnk0f6)
  * Variant calling: [.vcf](https://doi.org/10.25504/FAIRsharing.cfzz0h). Please ensure that the used reference sequence is also publically available and that it is unambiguously referenced in the header of the .vcf file, e.g. using the URL field of the ##contig field.
  
**Gene expression - Microarray-based**

* Preferred minimal metadata standard: [MIAME](https://doi.org/10.25504/FAIRsharing.32b10v) - Minimum Information About a Microarray Experiment
* Preferred file formats: tab-delimited text e.g. [MAGE-TAB](https://doi.org/10.25504/FAIRsharing.ak8p5g) and [ISA-TAB](https://doi.org/10.25504/FAIRsharing.53gp75), and raw data file formats from commercial microarray platforms ([Annotare accepted formats](https://www.ebi.ac.uk/fg/annotare/help/accepted_raw_ma_file_formats.html))

**Genome-wide association studies (GWAS)**

* Preferred minimal metadata standard: [MIxS](https://doi.org/10.25504/FAIRsharing.9aa0zp) - Minimum Information about any (x) Sequence
* Preferred file formats
  * for binary files: [.bim](https://doi.org/10.25504/FAIRsharing.b52795), [.fam](https://doi.org/10.25504/FAIRsharing.d0886a) and [.bed](https://doi.org/10.25504/FAIRsharing.mwmbpq)
  * for text-format files: [.ped](https://doi.org/10.25504/FAIRsharing.31385c) and [.map](https://doi.org/10.25504/FAIRsharing.53edcc)

**Metagenomics**

* [MIxS - MIGS/MIMS](https://doi.org/10.25504/FAIRsharing.va1hck) -
Minimum Information about a (Meta)Genome Sequence. The MIMS extension includes key environmental metadata. Developed by the Genomic Standards Consortium. Numerous adopters including NCBI/EBI/DDBJ databases. 
* [MIMARKS](https://doi.org/10.25504/FAIRsharing.zvrep1) -
Minimum Information about a MARKer gene Sequence. This is an extension of MIGS/MIMS for environmental sequences. Developed by the Genomic Standards Consortium. Numerous adopters including NCBI/EBI/DDBJ databases.  

### Imaging / Structural data

**X-ray diffraction**

There are no widely accepted standards for X-ray raw data files. Generally these are stored and archived in the Vendor’s native formats. Metadata is stored in CBF/[imgCIF](https://doi.org/10.25504/FAIRsharing.zr52g5) format (see: [catalogue of metadata resources for crystallographic applications](https://www.iucr.org/resources/data/dddwg/metadata-catalogue)).

Processed structural information is submitted to structural databases in the [PDBx/.mmCIF](https://doi.org/10.25504/FAIRsharing.fd28en) format.

**Electron microscopy**

* Data archiving and validation standards for cryo-EM maps and models are coordinated internationally by [EMDataResource](https://emdataresource.org/) (EMDR).
* Cryo-EM structures (map, experimental metadata, and optionally coordinate model) are deposited and processed through the [wwPDB OneDep system](https://deposit-2.wwpdb.org/), following the same annotation and validation workflow also used for X-ray crystallography and nuclear magnetic resonance (NMR) structures. EMDB holds all workflow metadata while PDB holds a subset of the metadata.
* Most electron microscopy data is stored in either raw data formats (binary, bitmap images, tiff, etc.) or proprietary formats developed by vendors (dm3, emispec, etc.).
* Processed structural information is submitted to structural resources as [PDBx/mmCIF](https://doi.org/10.25504/FAIRsharing.fd28en).
* Experimental metadata include information about the sample, specimen preparation, imaging, image processing, symmetry, reconstruction method, resolution and resolution method, as well as a description of the modeling/fitting procedures used and are described in [EMDR](https://emdataresource.org/), see also [Lawson et al 2020](https://aca.scitation.org/doi/10.1063/1.5138589).

**NMR**

* There are no widely accepted standards for NMR raw data files. Generally these are stored and archived in single FID/SER files.
* One effort for the standardization of NMR parameters extracted from 1D and 2D spectra of organic compounds to the proposed chemical structure is the [NMReDATA](https://doi.org/10.25504/FAIRsharing.8ae3d0) format.
* There is no universally accepted format, especially for crucial FID-associated metadata. [NMR-STAR](https://doi.org/10.25504/FAIRsharing.2chxxc) and its [NMR-STAR Dictionary](https://github.com/uwbmrb/nmr-star-dictionary) is the archival format used by the [Biological Nuclear Magnetic Resonance data Bank](https://bmrb.io/) (BMRB), the international repository of biomolecular NMR data and an archive of the [Worldwide Protein Data Bank](https://www.wwpdb.org/) (wwPDB).
* The [nmrML format specification](https://doi.org/10.25504/FAIRsharing.es03fk) (XML Schema Definition (XSD) and an accompanying controlled vocabulary called nmrCV) are an open mark up language and ontology for NMR data.
* Processed structural information is submitted in the [PDBx/mmCIF](https://doi.org/10.25504/FAIRsharing.fd28en/) format.

**Neutron scattering**

* ENDF/B-VI of Cross-Section Evaluation Working Group ([CSEWG](https://www.nndc.bnl.gov/csewg/)) and JEFF of OECD/NEA have been widely utilized in the nuclear community. The latest versions of the two nuclear reaction data libraries are [JEFF-3.3](https://doi.org/10.25504/FAIRsharing.4ed3fb) and ENDF/B-VIII.0 ([Brown et al., 2018](https://www.sciencedirect.com/science/article/pii/S0969804319301484#bib3)) with a significant upgrade in data for a number of nuclides ([Carlson et al., 2018](https://www.sciencedirect.com/science/article/pii/S0969804319301484#bib6)).
* Neutron scattering data are stored in the internationally-adopted [ENDF-6](https://www.oecd-nea.org/dbdata/data/manual-endf/endf102.pdf) format maintained by [CSEWG](https://www.nndc.bnl.gov/csewg/).
* Processed structural information is submitted in the [PDBx/mmCIF](https://doi.org/10.25504/FAIRsharing.fd28en/) format.

### Metabolomics data

For a curated list of relevant standards see [FAIRsharing](https://fairsharing.org) using the query ‘[metabolomics](https://fairsharing.org/search?q=metabolomics&fairsharingRegistry=Standard&page=1&status=ready)’.

* Core Information for Metabolomics Reporting [CIMR](https://doi.org/10.25504/FAIRsharing.exz30t) standard
* For identifying chemical compounds use [SMILES](https://doi.org/10.25504/FAIRsharing.qv4b3c) or [InChl](https://doi.org/10.25504/FAIRsharing.ddk9t9)
* To document Investigation/Study/Assay data, use the [ISA Abstract Model](https://isa-specs.readthedocs.io/en/latest/), also implemented as a tabular format, [ISA-Tab](https://doi.org/10.25504/FAIRsharing.53gp75) in [MetaboLights](https://www.ebi.ac.uk/metabolights). For an introduction to ISA, see ([Sansone S-A et al., 2012](https://doi.org/10.1038/ng.1054))
* Recommended formats for LC-MS data: [ANDI-MS](https://doi.org/10.25504/FAIRsharing.d7795c) specification, an analytical data interchange protocol for chromatographic data representation and/or [mzML](https://doi.org/10.25504/FAIRsharing.26dmba)
* Recommended formats for NMR data: [nmrCV](https://doi.org/10.25504/FAIRsharing.xm7tkj), [nmrML](https://doi.org/10.25504/FAIRsharing.es03fk)

### Lipidomics data

* Metadata should follow recommendations from the [CIMR standard](https://doi.org/10.25504/FAIRsharing.exz30t) by the Metabolomics Standards Initiative. It should be made available as tab or comma separated files (.tsv or .csv).
* Data can be stored in LC-MS file,  in tab (.tsv) or comma (.csv) separated formats.

### Proteomics data

For a curated list of relevant standards see [FAIRsharing](https://fairsharing.org) using the query ’[proteomics](https://fairsharing.org/search/?q=proteomics&fairsharingRegistry=Standard&page=1&status=ready)’, some examples are given below:

* Use the minimal information model specified in [MIAPE](https://doi.org/10.25504/FAIRsharing.8vv5fc) by the HUPO Proteomics Standards Initiative ([HUPO PSI](https://hupo.org/Proteomics-Standards-Initiative)), and fill the model using the controlled vocabularies specified by the Proteomics Standards Initiative: [PSI-MS CV](https://doi.org/10.25504/FAIRsharing.sxh2dp)
* Recommended formats:
  * For gel electrophoresis: [PSI gelML](https://doi.org/10.25504/FAIRsharing.rn9wzc)
  * For transition lists: [HUPO-PSI TraML](https://doi.org/10.25504/FAIRsharing.rz77m6)
  * For raw spectrometer output: [mzML](https://doi.org/10.25504/FAIRsharing.26dmba)
  * For reporting: [mzTab](https://doi.org/10.25504/FAIRsharing.c12tyk)
  * For protein quantisation data: [mzQuantML](https://doi.org/10.25504/FAIRsharing.fk6zhb)
  * For protein identification data: [mzIdentML](https://doi.org/10.25504/FAIRsharing.11889)
  * For metadata: [ISA-TAB](https://isa-tools.org/) with conversion to PRIDE format

## Resources
* [RDMkit on Metadata](https://rdmkit.elixir-europe.org/metadata_management)
* [Metadata module](https://nbisweden.github.io/module-metadata-dm-practices/) in course [Introduction to data management practices](https://uppsala.instructure.com/courses/48087/pages/introduction-to-data-management-practices)
