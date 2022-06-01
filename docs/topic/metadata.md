# Metadata 
Good documentation in research projects, describing how the datasets were created, how they are structured, and what they mean, is essential for making your data understandable. Metadata provides such 'data about data', and may include information on the methodology used to collect the data, analytical and procedural information, definitions of variables, units of measurement, any assumptions made, the format and file type of the data and software used to collect and/or process the data.

Researchers are strongly encouraged to use community metadata standards where these are in place (see further down). Data repositories may also provide guidance about appropriate metadata standards and requirements e.g. [ENA sample checklists](https://www.ebi.ac.uk/ena/submit/checklists). It is highly recommended to, already from the beginning of the project, structure e.g. sample metadata in a way that enables sequence data submission without having to reformat the metadata.

## Ontologies

Ontologies, controlled vocabularies and data dictionaries are used to standardize the language used to describe the metadata. Think of the many ways to write that the organism is human (human, Human, homo sapiens, H. sapiens, Homo Sapiens, man, etc), using an ontology such as [NCBI taxonomy](https://www.ebi.ac.uk/ols/ontologies/ncbitaxon) unifies the language and makes it easier for both humans and machines to interpret and work with the data. While an ontology has a hierarchical structure, a controlled vocabulary is an unstructured set of terms. A [Data Dictionary](https://help.osf.io/hc/en-us/articles/360019739054-How-to-Make-a-Data-Dictionary) is a user-defined way of describing what all the variable names and values in your data really mean. 

For a suggested list of ontologies appropriate for Life Science community please see [FAIRsharing.org](https://fairsharing.org/standards/?q=&selected_facets=status:Ready&selected_facets=expanded_onto_disciplines_exact:%20Life%20Science&selected_facets=type_exact:terminology%20artifact), filter on e.g. Domain.

Below are ontology resources, adapted from Table 2 in *Griffin PC, Khadake J, LeMay KS et al. Best practice data life cycle approaches for the life sciences. F1000Research 2018, 6:1618.* doi: [10.12688/f1000research.12344.2](10.12688/f1000research.12344.2)

* [Ontology Lookup Service](http://www.ebi.ac.uk/ols/) - Discover different ontologies and their contents.
* [OBO Foundry](http://obofoundry.org/) - Table of open biomedical ontologies with information on development status, license and content.
* [Zooma](http://www.ebi.ac.uk/spot/zooma/) - Assign ontology terms using curated mapping.
* [Webulous](https://www.ebi.ac.uk/efo/webulous/) - Create new ontology terms easily.
* [Ontobee](http://www.ontobee.org) - A linked data server that facilitates ontology data sharing, visualization, and use.

## Data and metadata standards Genomics data
A list of relevant data and metadata standards can be found in [FAIRsharing](https://fairsharing.org/search/?q=genomics&content=standards), some specific examples are below.
### Gene expression
#### Transcriptomics:
* Preferred minimal metadata standard: [MINSEQE](http://www.fged.org/projects/minseqe/)
* Preferred file formats (sequencing-based):
  * Raw sequences: [.fastq](https://www.open-bio.org/2009/12/17/nar-fastq-format/) (compression can be added with gzip)
  * Mapped sequences: [.sam](https://github.com/samtools/samtools) (compression with [.bam](http://genome.ucsc.edu/goldenPath/help/bam.html) or [.cram](https://www.sanger.ac.uk/science/tools/cram)). Please ensure that the used reference sequence is also publically available and that the @SQ header is present and unambiguously describes the used reference sequence.
  * Transcripts per million (TPM): [.csv](https://tools.ietf.org/html/rfc4180)

* **Gene Structure:** [.gtf](https://doi.org/10.25504/FAIRsharing.sggb1n)
* **Gene Features:** [.gff](https://doi.org/10.25504/FAIRsharing.dnk0f6)
* **Variant calling:** [.vcf](https://doi.org/10.25504/FAIRsharing.cfzz0h). Please ensure that the used reference sequence is also publically available and that it is unambiguously referenced in the header of the .vcf file, e.g. using the URL field of the ##contig field.
* Also see [FAIRsharing using the query ‘transcriptomics’](https://fairsharing.org/standards/?q=transcriptomics)

#### Microarray-based gene expression data:
* Preferred minimal metadata standard: [MIAME](http://www.fged.org/projects/miame/)
* Preferred file formats: tab-delimited text eg [MAGE-TAB](http://fged.org/projects/mage-tab/) and [ISA-TAB](https://isa-tools.org/), and raw data file formats from commercial microarray platforms ([Annotare accepted formats](https://www.ebi.ac.uk/fg/annotare/help/accepted_raw_ma_file_formats.html))

### Genome-wide association studies (GWAS):
* Preferred minimal metadata standard: [MIxS](https://doi.org/10.25504/FAIRsharing.9aa0zp)
* Preferred file formats 
  *  for binary files: [.bim](https://www.cog-genomics.org/plink2/formats#bim), [.fam](https://www.cog-genomics.org/plink2/formats#fam) and [.bed](https://www.cog-genomics.org/plink2/formats#bed)
  *  for text-format files: [.ped](https://www.cog-genomics.org/plink2/formats#ped) and [.map](https://www.cog-genomics.org/plink2/formats#map)

### Metagenomics
* [MIxS - MIGS/MIMS](http://wiki.gensc.org/index.php?title=MIGS/MIMS)
Minimum Information about a (Meta)Genome Sequence. The  MIMS extension includes key environmental metadata. Developed by the Genomic Standards Consortium. Numerous adopters including NCBI/EBI/DDBJ databases.  

* [MIMARKS](http://wiki.gensc.org/index.php?title=MIMARKS)
Minimum Information about a MARKer gene Sequence. This is an extension of MIGS/MIMS for environmental sequences. Developed by the Genomic Standards Consortium. Numerous adopters including NCBI/EBI/DDBJ databases.  

### Functional Annotation of Animal Genomes Consortium (FAANG) standards
* [FAANG sample metadata specification](https://github.com/FAANG/faang-metadata/blob/master/docs/faang_sample_metadata.md)
Metadata specification for biological samples derived from animals (animals, tissue samples, cells or other biological materials). Complies with EBI database requirements and [BioSamples](https://www.ebi.ac.uk/biosamples/) database formats. 

* [FAANG experimental metadata specification](https://github.com/FAANG/faang-metadata/blob/master/docs/faang_experiment_metadata.md)
Metadata specification for sequencing and array experiments on animal samples.

## Data and metadata standards Proteomics
For a curated list of relevant standards see [FAIRsharing](https://fairsharing.org) using the query ’[proteomics](https://fairsharing.org/search/?q=proteomics&content=standard&name=&taxonomies=&organisations=&shortname=&description=&supportlinks=&licenses=&countries=&maintainers=&expanded_onto_domains=&expanded_onto_disciplines=&user_defined_tags=&record_id=&miriam_id=&search_state=hidden)’ 

* Use the minimal information model specified in [MIAPE](http://www.psidev.info/miape) by the HUPO Proteomics Standards
Initiative ([HUPO PSI](https://doi.org/10.1038/nbt1329)), and fill the model using the controlled vocabularies specified by the Proteomics Standards Initiative: [PSI CVs](http://www.psidev.info/groups/mass-spectrometry#controlled)
* Recommended formats: 
  * For gel electrophoresis [gelML](http://www.psidev.info/gelml/1.0))
  * For transition lists [TraML](http://www.psidev.info/traml)
  * For raw spectrometer output [mzML](http://www.psidev.info/mzml)
  * For reporting [mzTab](http://www.psidev.info/mztab)
  * For protein quantisation data [mzQuantML](http://www.psidev.info/mzquantml)
  * For protein identification data [mzIdentML](http://www.psidev.info/mzidentml)
  * For metadata [ISA-TAB](https://isa-tools.org/) with conversion to PRIDE format

## Data and metadata standards Metabolomics:
For a curated list of relevant standards see [FAIRsharing](https://fairsharing.org) using the query ‘[metabolomics](https://fairsharing.org/search/?q=metabolomics&content=standard&name=&taxonomies=&organisations=&shortname=&description=&supportlinks=&licenses=&countries=&maintainers=&expanded_onto_domains=&expanded_onto_disciplines=&user_defined_tags=&record_id=&miriam_id=&search_state=hidden)’.

* Core Information for Metabolomics Reporting [CIMR](https://github.com/MSI-Metabolomics-Standards-Initiative/CIMR/) standard
* For identifying chemical compounds use [SMILES](https://doi.org/10.25504/FAIRsharing.qv4b3c) or [InChl](https://doi.org/10.25504/FAIRsharing.ddk9t9)
* To document Investigation/Study/Assay data, use the [ISA Abstract Model](https://isa-specs.readthedocs.io/en/latest/), also implemented as
a tabular format, [ISA-Tab](https://doi.org/10.25504/FAIRsharing.53gp75) in [MetaboLights](https://www.ebi.ac.uk/metabolights). For an introduction to ISA, see ([Sansone S-A et al., 2012](https://doi.org/10.1038/ng.1054))

* Recommended formats for LC-MS data: [ANDI-MS](https://fairsharing.org/bsg-s001216/) specification, an analytical data interchange protocol for chromatographic data
representation and/or [mzML](http://www.psidev.info/mzML)
* Recommended formats for NMR data: [nmrCV](http://nmrml.org/cv/), [nmrML](http://nmrml.org/schema/)

## Data and metadata standards Lipidomics:

* Metadata should follow recommendations from the [CIMR standard](http://msi-workgroups.sourceforge.net/bio-metadata/) by the Metabolomics Standards Initiative. It should be made available as tab or comma separated files (.tsv or .csv).

* Data can be stored in LC-MS file,  in tab (.tsv) or comma (.csv) separated formats.

## Data and metadata standards Structural data / Imaging
**X-ray diffraction**
* There are no widely accepted standards for X-ray raw data files. Generally these are stored and archived in the Vendor’s native formats. Metadata is stored in CBF/[imgCIF](https://www.iucr.org/resources/cif) format (see: [catalogue of metadata resources for crystallographic applications](https://www.iucr.org/resources/data/dddwg/metadata-catalogue)). 
* Processed structural information is submitted to structural databases in the [PDBx/.mmCIF](http://mmcif.pdb.org/) format.

**Electron microscopy**
* Data archiving and validation standards for cryo-EM maps and models are coordinated internationally by [EMDataResource](http://emdataresource.org/) (EMDR).
* Cryo-EM structures (map, experimental metadata, and optionally coordinate model) are deposited and processed through the [wwPDB OneDep system](https://deposit-2.wwpdb.org/), following the same annotation and validation workflow also used for X-ray crystallography and nuclear magnetic resonance (NMR) structures. EMDB holds all workflow metadata while PDB holds a subset of the metadata.
* Most electron microscopy data is stored in either raw data formats (binary, bitmap images, tiff, etc.) or proprietary formats developed by vendors (dm3, emispec, etc.).
* Processed structural information is submitted to structural resources as [PDBx/mmCIF](http://mmcif.pdb.org/).
* Experimental metadata include information about the sample, specimen preparation, imaging, image processing, symmetry, reconstruction method,
resolution and resolution method, as well as a description of the modeling/fitting procedures used and are described in [EMDR](http://emdataresource.org/index.html), see also [Lawson et al 2020](https://aca.scitation.org/doi/10.1063/1.5138589).

**NMR**
* There are no widely accepted standards for NMR raw data files. Generally these are stored and archived in single FID/SER files.
* One effort for the standardization of NMR parameters extracted from 1D and 2D spectra of organic compounds to the proposed chemical structure is the [NMReDATA](http://nmredata.org/) format.
* There is no universally accepted format, especially for crucial FID-associated metadata. [NMR-STAR](http://www.bmrb.wisc.edu/formats.shtml) and its [NMR-STAR Dictionary](https://github.com/uwbmrb/nmr-star-dictionary) is the archival format used by the [Biological Nuclear Magnetic Resonance data Bank](http://www.bmrb.wisc.edu/) (BMRB), the international repository of biomolecular NMR data and an archive of the [Worldwide Protein Data Bank](http://www.wwpdb.org/) (wwPDB).
* The [nmrML format specification](http://nmrml.org/) (XML Schema Definition (XSD) and an accompanying controlled vocabulary called nmrCV) are an open mark up language and ontology for NMR data.
* Processed structural information is submitted in the [PDBx/mmCIF](http://mmcif.pdb.org/) format.

**Neutron scattering**
* ENDF/B-VI of Cross-Section Evaluation Working Group ([CSEWG](https://www.nndc.bnl.gov/csewg/)) and JEFF of OECD/NEA have been widely utilized in the nuclear community. The latest versions of the two nuclear reaction data libraries are [JEFF-3.3](https://www.oecd-nea.org/dbdata/jeff/) and ENDF/B-VIII.0 ([Brown et al., 2018](https://www.sciencedirect.com/science/article/pii/S0969804319301484#bib3)) with a significant upgrade in data for a number of nuclides ([Carlson et al., 2018](https://www.sciencedirect.com/science/article/pii/S0969804319301484#bib6)).
* Neutron scattering data are stored in the internationally-adopted [ENDF-6](https://www.oecd-nea.org/dbdata/data/manual-endf/endf102.pdf) format maintained by [CSEWG](https://www.nndc.bnl.gov/csewg/).
* Processed structural information is submitted in the [PDBx/mmCIF](http://mmcif.pdb.org/) format.

## Resources
* [RDMkit on Metadata](https://rdmkit.elixir-europe.org/metadata_management)

## Training
* [Metadata module](https://nbisweden.github.io/module-metadata-dm-practices/)