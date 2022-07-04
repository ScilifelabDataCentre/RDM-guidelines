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
Good documentation in research projects, describing how the datasets were created, how they are structured, and what they mean, is essential for making your data understandable. Metadata provides such 'data about data', and may include information on the methodology used to collect the data, analytical and procedural information, definitions of variables, units of measurement, any assumptions made, the format and file type of the data and software used to collect and/or process the data.

Researchers are strongly encouraged to use community metadata standards where these are in place (see further down). Data repositories may also provide guidance about appropriate metadata standards and requirements e.g. [ENA sample checklists](https://www.ebi.ac.uk/ena/submit/checklists). It is highly recommended to, already from the beginning of the project, structure e.g. sample metadata in a way that enables sequence data submission without having to reformat the metadata.

For convenience, we have created templates for the most frequent data types and their corresponding ENA checklists. The templates come with instructions on how to do an interactive submission, via the ENA Webin Portal, but even when doing a programmatic submission, the template can be useful for collecting all necessary descriptions / metadata. Download an appropriate template, and fill in the sheets according to the instructions in the template:
* [ERC000011 ENA default sample checklist](/meta-data-templates/metadata_template_default_ERC000011.xlsx)
* [ERC000033 ENA virus pathogen reporting standard checklist](/meta-data-templates/metadata_template_virus_ERC000033.xlsx)
* [ERC000036 ENA sewage checklist](/meta-data-templates/metadata_template_sewage_ERC000036.xlsx)

## Ontologies

Ontologies, controlled vocabularies and data dictionaries are used to standardize the language used to describe the metadata. Think of the many ways to write that the organism is human (human, Human, homo sapiens, H. sapiens, Homo Sapiens, man, etc), using an ontology such as [NCBI taxonomy](https://www.ebi.ac.uk/ols/ontologies/ncbitaxon) unifies the language and makes it easier for both humans and machines to interpret and work with the data. While an ontology has a hierarchical structure, a controlled vocabulary is an unstructured set of terms. A [Data Dictionary](https://help.osf.io/hc/en-us/articles/360019739054-How-to-Make-a-Data-Dictionary) is a user-defined way of describing what all the variable names and values in your data really mean. 

For a suggested list of ontologies appropriate for Life Science community please see [FAIRsharing.org](https://fairsharing.org/standards/?q=&selected_facets=status:Ready&selected_facets=expanded_onto_disciplines_exact:%20Life%20Science&selected_facets=type_exact:terminology%20artifact), filter on e.g. Domain.

Below are ontology resources, adapted from Table 2 in *Griffin PC, Khadake J, LeMay KS et al. Best practice data life cycle approaches for the life sciences. F1000Research 2018, 6:1618.* doi: [10.12688/f1000research.12344.2](10.12688/f1000research.12344.2)

* [Ontology Lookup Service](http://www.ebi.ac.uk/ols/) - Discover different ontologies and their contents.
* [OBO Foundry](http://obofoundry.org/) - Table of open biomedical ontologies with information on development status, license and content.
* [Zooma](http://www.ebi.ac.uk/spot/zooma/) - Assign ontology terms using curated mapping.
* [Webulous](https://www.ebi.ac.uk/efo/webulous/) - Create new ontology terms easily.
* [Ontobee](http://www.ontobee.org) - A linked data server that facilitates ontology data sharing, visualization, and use.

<!-- should be in expandable sections -->
## Data and metadata standards 
Click on the buttons below for data type specific information regarding file types and metadata standards.

<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample1" role="button" aria-expanded="false" aria-controls="collapseExample1">
    Genomics data
  </a>
</p>
<div class="collapse" id="collapseExample1">
  <div class="card card-body">
  <span>
  A list of relevant data and metadata standards can be found in <a href="https://fairsharing.org/search/?q=genomics&content=standards">FAIRsharing</a>, some specific examples are below.<br><br>
  <h5> Gene expression - Transcriptomics</h5>
  <ul>
    <li>Preferred minimal metadata standard: <a href="http://www.fged.org/projects/minseqe/">MINSEQE</a></li>
    <li> Preferred file formats (sequencing-based):
      <ul>
        <li> Raw sequences: <a href="https://www.open-bio.org/2009/12/17/nar-fastq-format/">.fastq</a> (compression can be added with gzip)</li>
        <li> Mapped sequences: <a href="https://github.com/samtools/samtools">.sam</a> (compression with <a href="http://genome.ucsc.edu/goldenPath/help/bam.html">.bam</a> or <a href="https://www.sanger.ac.uk/science/tools/cram">.cram</a>). Please ensure that the used reference sequence is also publically available and that the @SQ header is present and unambiguously describes the used reference sequence.</li>
        <li> Transcripts per million (TPM): <a href="https://tools.ietf.org/html/rfc4180">.csv</a></li>
        <li> Gene Structure: <a href="https://doi.org/10.25504/FAIRsharing.sggb1n">.gtf</a></li>
        <li> Gene Features: <a href="https://doi.org/10.25504/FAIRsharing.dnk0f6">.gff</a></li>
        <li> Variant calling: <a href="https://doi.org/10.25504/FAIRsharing.cfzz0h">.vcf</a>. Please ensure that the used reference sequence is also publically available and that it is unambiguously referenced in the header of the .vcf file, e.g. using the URL field of the ##contig field.</li>
      </ul>
    </li>
    <li> Also see <a href="https://fairsharing.org/standards/?q=transcriptomics">FAIRsharing using the query ‘transcriptomics’</a></li>
  </ul>
  <h5> Gene expression - Microarray-based</h5>
  <ul>
    <li>Preferred minimal metadata standard: <a href="http://www.fged.org/projects/miame/">MIAME</a></li>
    <li>Preferred file formats: tab-delimited text e.g. <a href="http://fged.org/projects/mage-tab/">MAGE-TAB</a> and <a href="https://isa-tools.org/">ISA-TAB</a>, and raw data file formats from commercial microarray platforms (<a href="https://www.ebi.ac.uk/fg/annotare/help/accepted_raw_ma_file_formats.html">Annotare accepted formats</a>)</li>
  </ul>
  <h5> Genome-wide association studies (GWAS):</h5>
  <ul>
    <li>Preferred minimal metadata standard: <a href="https://doi.org/10.25504/FAIRsharing.9aa0zp">MIxS</a>
    <li>Preferred file formats 
      <ul>
        <li>for binary files: <a href="https://www.cog-genomics.org/plink2/formats#bim">.bim</a>, <a href="https://www.cog-genomics.org/plink2/formats#fam">.fam</a> and <a href="https://www.cog-genomics.org/plink2/formats#bed">.bed</a></li>
        <li>for text-format files: <a href="https://www.cog-genomics.org/plink2/formats#ped">.ped</a> and <a href="https://www.cog-genomics.org/plink2/formats#map">.map</a></li>
      </ul>
    </li>
  </ul>
  <h5> Metagenomics</h5>
  <ul>
    <li><a href="http://wiki.gensc.org/index.php?title=MIGS/MIMS">MIxS - MIGS/MIMS</a> - 
    Minimum Information about a (Meta)Genome Sequence. The MIMS extension includes key environmental metadata. Developed by the Genomic Standards Consortium. Numerous adopters including NCBI/EBI/DDBJ databases. </li> 
    <li><a href="http://wiki.gensc.org/index.php?title=MIMARKS">MIMARKS</a> - 
    Minimum Information about a MARKer gene Sequence. This is an extension of MIGS/MIMS for environmental sequences. Developed by the Genomic Standards Consortium. Numerous adopters including NCBI/EBI/DDBJ databases.</li>  
  </ul>
  <h5>Functional Annotation of Animal Genomes Consortium (FAANG) standards</h5>
  <ul>
    <li><a href="https://github.com/FAANG/faang-metadata/blob/master/docs/faang_sample_metadata.md">FAANG sample metadata specification</a>:
    Metadata specification for biological samples derived from animals (animals, tissue samples, cells or other biological materials). Complies with EBI database requirements and <a href="https://www.ebi.ac.uk/biosamples/">BioSamples</a> database formats. </li>
    <li><a href="https://github.com/FAANG/faang-metadata/blob/master/docs/faang_experiment_metadata.md">FAANG experimental metadata specification</a>:
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
      There are no widely accepted standards for X-ray raw data files. Generally these are stored and archived in the Vendor’s native formats. Metadata is stored in CBF/<a href="https://www.iucr.org/resources/cif">imgCIF</a> format (see: <a href="https://www.iucr.org/resources/data/dddwg/metadata-catalogue">catalogue of metadata resources for crystallographic applications</a>). <br><br>
      Processed structural information is submitted to structural databases in the <a href="http://mmcif.pdb.org/">PDBx/.mmCIF</a> format.<br><br>
      <h5>Electron microscopy</h5>
      <ul>
        <li>Data archiving and validation standards for cryo-EM maps and models are coordinated internationally by <a href="http://emdataresource.org/">EMDataResource</a> (EMDR).</li>
        <li>Cryo-EM structures (map, experimental metadata, and optionally coordinate model) are deposited and processed through the <a href="https://deposit-2.wwpdb.org/">wwPDB OneDep system</a>, following the same annotation and validation workflow also used for X-ray crystallography and nuclear magnetic resonance (NMR) structures. EMDB holds all workflow metadata while PDB holds a subset of the metadata.</li>
        <li>Most electron microscopy data is stored in either raw data formats (binary, bitmap images, tiff, etc.) or proprietary formats developed by vendors (dm3, emispec, etc.).</li>
        <li>Processed structural information is submitted to structural resources as <a href="http://mmcif.pdb.org/">PDBx/mmCIF</a>.</li>
        <li>Experimental metadata include information about the sample, specimen preparation, imaging, image processing, symmetry, reconstruction method, resolution and resolution method, as well as a description of the modeling/fitting procedures used and are described in <a href="http://emdataresource.org/index.html">EMDR</a>, see also <a href="https://aca.scitation.org/doi/10.1063/1.5138589">Lawson et al 2020</a>.</li>
      </ul>
      <h5>NMR</h5>
      <ul>
        <li>There are no widely accepted standards for NMR raw data files. Generally these are stored and archived in single FID/SER files.</li>
        <li>One effort for the standardization of NMR parameters extracted from 1D and 2D spectra of organic compounds to the proposed chemical structure is the <a href="http://nmredata.org/">NMReDATA</a> format.</li>
        <li>There is no universally accepted format, especially for crucial FID-associated metadata. <a href="http://www.bmrb.wisc.edu/formats.shtml">NMR-STAR</a> and its <a href="https://github.com/uwbmrb/nmr-star-dictionary">NMR-STAR Dictionary</a> is the archival format used by the <a href="http://www.bmrb.wisc.edu/">Biological Nuclear Magnetic Resonance data Bank</a> (BMRB), the international repository of biomolecular NMR data and an archive of the <a href="http://www.wwpdb.org/">Worldwide Protein Data Bank</a> (wwPDB).</li>
        <li>The <a href="http://nmrml.org/">nmrML format specification</a> (XML Schema Definition (XSD) and an accompanying controlled vocabulary called nmrCV) are an open mark up language and ontology for NMR data.</li>
        <li>Processed structural information is submitted in the <a href="http://mmcif.pdb.org/">PDBx/mmCIF</a> format.</li>
      </ul>
      <h5>Neutron scattering</h5>
      <ul>
        <li>ENDF/B-VI of Cross-Section Evaluation Working Group (<a href="https://www.nndc.bnl.gov/csewg/">CSEWG</a>) and JEFF of OECD/NEA have been widely utilized in the nuclear community. The latest versions of the two nuclear reaction data libraries are <a href="https://www.oecd-nea.org/dbdata/jeff/">JEFF-3.3</a> and ENDF/B-VIII.0 (<a href="https://www.sciencedirect.com/science/article/pii/S0969804319301484#bib3">Brown et al., 2018</a>) with a significant upgrade in data for a number of nuclides (<a href="https://www.sciencedirect.com/science/article/pii/S0969804319301484#bib6">Carlson et al., 2018</a>).</li>
        <li>Neutron scattering data are stored in the internationally-adopted <a href="https://www.oecd-nea.org/dbdata/data/manual-endf/endf102.pdf">ENDF-6</a> format maintained by <a href="https://www.nndc.bnl.gov/csewg/">CSEWG</a>.</li>
        <li>Processed structural information is submitted in the <a href="http://mmcif.pdb.org/">PDBx/mmCIF</a> format.</li>
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
    For a curated list of relevant standards see <a href="https://fairsharing.org">FAIRsharing</a> using the query ‘<a href="https://fairsharing.org/search/?q=metabolomics&content=standard&name=&taxonomies=&organisations=&shortname=&description=&supportlinks=&licenses=&countries=&maintainers=&expanded_onto_domains=&expanded_onto_disciplines=&user_defined_tags=&record_id=&miriam_id=&search_state=hidden">metabolomics</a>’.
    <ul>
      <li>Core Information for Metabolomics Reporting <a href="https://github.com/MSI-Metabolomics-Standards-Initiative/CIMR/">CIMR</a> standard</li>
      <li>For identifying chemical compounds use <a href="https://doi.org/10.25504/FAIRsharing.qv4b3c">SMILES</a> or <a href="https://doi.org/10.25504/FAIRsharing.ddk9t9">InChl</a></li>
      <li>To document Investigation/Study/Assay data, use the <a href="https://isa-specs.readthedocs.io/en/latest/">ISA Abstract Model</a>, also implemented as a tabular format, <a href="https://doi.org/10.25504/FAIRsharing.53gp75">ISA-Tab</a> in <a href="https://www.ebi.ac.uk/metabolights">MetaboLights</a>. For an introduction to ISA, see (<a href="https://doi.org/10.1038/ng.1054">Sansone S-A et al., 2012</a>)</li>
      <li>Recommended formats for LC-MS data: <a href="https://fairsharing.org/bsg-s001216/">ANDI-MS</a> specification, an analytical data interchange protocol for chromatographic data representation and/or <a href="http://www.psidev.info/mzML">mzML</a>
      <li>Recommended formats for NMR data: <a href="http://nmrml.org/cv/">nmrCV</a>, <a href="http://nmrml.org/schema/">nmrML</a></li>
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
    <li>Metadata should follow recommendations from the <a href="http://msi-workgroups.sourceforge.net/bio-metadata/">CIMR standard</a> by the Metabolomics Standards Initiative. It should be made available as tab or comma separated files (.tsv or .csv).</li>
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
  For a curated list of relevant standards see <a href="https://fairsharing.org">FAIRsharing</a> using the query ’<a href="https://fairsharing.org/search/?q=proteomics&content=standard&name=&taxonomies=&organisations=&shortname=&description=&supportlinks=&licenses=&countries=&maintainers=&expanded_onto_domains=&expanded_onto_disciplines=&user_defined_tags=&record_id=&miriam_id=&search_state=hidden">proteomics</a>’ 

  <ul>
    <li>Use the minimal information model specified in <a href="http://www.psidev.info/miape">MIAPE</a> by the HUPO Proteomics Standards Initiative (<a href="https://doi.org/10.1038/nbt1329">HUPO PSI</a>), and fill the model using the controlled vocabularies specified by the Proteomics Standards Initiative: <a href="http://www.psidev.info/groups/mass-spectrometry#controlled">PSI CVs</a></li>
    <li>Recommended formats: 
      <ul>
        <li>For gel electrophoresis <a href="http://www.psidev.info/gelml/1.0">gelML</a></li>
        <li>For transition lists <a href="http://www.psidev.info/traml">TraML</a></li>
        <li>For raw spectrometer output <a href="http://www.psidev.info/mzml">mzML</a></li>
        <li>For reporting <a href="http://www.psidev.info/mztab">mzTab</a></li>
        <li>For protein quantisation data <a href="http://www.psidev.info/mzquantml">mzQuantML</a></li>
        <li>For protein identification data <a href="http://www.psidev.info/mzidentml">mzIdentML</a></li>
        <li>For metadata <a href="https://isa-tools.org/">ISA-TAB</a> with conversion to PRIDE format</li>
      </ul>
    </li>
  </ul>
  </span>
  </div>
</div>

### Resources & Training
* [RDMkit on Metadata](https://rdmkit.elixir-europe.org/metadata_management)
* [Metadata module](https://nbisweden.github.io/module-metadata-dm-practices/) in course [Introduction to data management practices](https://uppsala.instructure.com/courses/48087/pages/introduction-to-data-management-practices)