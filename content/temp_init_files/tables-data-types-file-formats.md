<!---
Origin is dsw-appendix, but we decided not to put this information in any of the metadata or share pages. However, since they are already written, we keep the tables if we would like to use them later.

There are two versions, the first lists the file formats, description and which data types is associated with the file type, the second starts with the data type, and also includes a column with repositories that accepts the described data type and file format.
--->

<!---
## Typical data types and file formats

Please find below a table with the most common data types and file formats within life science, adapted from [Griffin PC, Khadake J, LeMay KS et al. Best practice data life cycle approaches for the life sciences [version 2; referees: 2 approved]. F1000Research 2018, 6:1618](https://doi.org/10.12688/f1000research.12344.2):

<div class="table-responsive">
  <table class="table table-hover table-bordered">
    <thead  class="table-active">
      <tr>
        <td>File format</td>
        <td>Description</td>
        <td>Data type</td>
      </tr>
    </thead>
    <tr>
      <td><a href="https://doi.org/10.25504/FAIRsharing.rz4vfg">FASTA</a></td>
      <td>FASTA is a text-based format for representing nucleotide sequences 
      or protein sequences, in which nucleotides or amino acids 
      are represented using single-letter codes.</td>
      <td>Raw DNA/RNA sequence, Assembled DNA sequence (no annotation), Protein sequence</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.25504/FAIRsharing.r2ts5t">FASTQ</a></td>
      <td>FASTQ combines base quality information with the nucleotide sequence. </td>
      <td>Raw DNA/RNA sequence</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.25504/FAIRsharing.wvgta9">HDF5</a></td>
      <td>HDF5 is a newer sequence read format used by long read sequencers 
      e.g. PacBio and Oxford Nanopore. </td>
      <td>Raw DNA/RNA sequence</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.25504/FAIRsharing.k97xzh">SAM</a>, <a href="https://doi.org/10.25504/FAIRsharing.hza1ec">BAM</a>, <a href="https://doi.org/10.25504/FAIRsharing.f846bd">CRAM</a></td>
      <td>Sequences aligned to a reference are represented in sequence 
      alignment and mapping format (SAM). Its binary version is 
      called BAM and further compression can be done using the 
      CRAM format.</td>
      <td>Raw DNA/RNA sequence, Aligned DNA sequence</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.25504/FAIRsharing.q9nh66">Flat file</a></td>
      <td>Annotation can be integrated with assemblies in contig, scaffold or 
      chromosome flat file format. </td>
      <td>Assembled DNA sequence (with annotation)</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.25504/FAIRsharing.mg1mdc">AGP</a></td>
      <td>AGP (A Gold Path) files are used to describe how smaller fragments are placed in an 
      assembly but do not contain the sequence information themselves. </td>
      <td>Assembled DNA sequence</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.25504/FAIRsharing.sggb1n">GTF</a>, <a href="https://doi.org/10.25504/FAIRsharing.qaaj0q">GFF</a>, <a href="https://doi.org/10.25504/FAIRsharing.dnk0f6">GFF3</a></td>
      <td>General feature format or general transfer format are 
      commonly used to store genomic features in tab-delimited 
      flat text format. GFF3 is a more advanced version of the 
      basic GFF that allows description of more complex 
      features.</td>
      <td>Gene model or genomic feature annotation</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.25504/FAIRsharing.mwmbpq">BED</a></td>
      <td>BED (Browser Extensible Data) format is a tab-delimited text format that also allows 
      definition of how a feature should be displayed (e.g. on a genome browser)</td>
      <td>Gene model or genomic feature annotation</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.25504/FAIRsharing.rg2vmt">GB/GBK</a></td>
      <td>GenBank flat file Format (GB/GBK) is also commonly used but not well standardised</td>
      <td>Gene model or genomic feature annotation</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.25504/FAIRsharing.77fbbf">GAF</a>, <a href="https://doi.org/10.25504/FAIRsharing.rtm51">GPAD</a>, <a href="https://doi.org/10.25504/FAIRsharing.820ebm">GPI</a></td>
      <td>A GAF file is a Gene Ontology (GO) Annotation File containing annotations made to the GO by a contributing resource such as FlyBase 
      or Pombase. The need for a way to represent genes/gene products separately from annotations, as well as the need to use the evidence ontology has lead to the creation of the GPAD (Gene Product Annotation Data) and GPI (Gene Product Information) formats.</td>
      <td>Gene functional annotation</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.25504/FAIRsharing.cfzz0h">VCF</a></td>
      <td>A tab-delimited text format to store meta-information as 
      header lines followed by information about variants position in the genome.</td>
      <td>Genetic/genomic variants</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.25504/FAIRsharing.77e3my">PSI-MI XML</a>, <a href="https://doi.org/10.25504/FAIRsharing.ve0710">MITAB</a></td>
      <td>Data formats developed to exchange molecular interaction 
      data, related metadata and fully describe molecule constructs.</td>
      <td>Interaction data</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.25504/FAIRsharing.26dmba">mzML</a></td>
      <td>A formally defined XML format for representing mass 
      spectrometry data. Files typically contain sequences of 
      mass spectra, plus metadata about the experiment.</td>
      <td>Raw metabolite profile, Raw proteome profile</td>
    </tr>    <tr>
      <td><a href="https://doi.org/10.25504/FAIRsharing.es03fk">nmrML</a></td>
      <td>XML based data format that define nuclear magnetic resonance raw data in metabolomics</td>
      <td>Raw metabolite profile</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.25504/FAIRsharing.xvf5y3">Darwin core</a></td>
      <td>The Darwin Core (DwC) standard facilitates the exchange of 
      information about biodiversity such as geographic location of organisms and 
      associated collection of specimens.</td>
      <td>Organisms and specimens</td>
    </tr>
  </table>
</div>
--->
<!---
<div class="table-responsive">
  <table class="table table-hover table-bordered">
    <thead  class="table-active">
      <tr>
        <td>Data type</td>
        <td>Format name</td>
        <td>Description</td>
        <td>Suitable repositories</td>
      </tr>
    </thead>
    <tr>
      <td>Raw DNA/RNA sequence</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.rz4vfg">FASTA</a> <a href="https://doi.org/10.25504/FAIRsharing.r2ts5t">FASTQ</a></td>
      <td>FASTA is a common text format to store DNA/RNA/Protein sequence and 
      FASTQ combines base quality information with the nucleotide sequence. </td>
      <td><a href="http://www.ebi.ac.uk/ena/submit/genomes-sequence-submission">ENA</a></td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.wvgta9">HDF5</a></td>
      <td>HDF5 is a newer sequence read format used by long read sequencers 
      e.g. PacBio and Oxford Nanopore. </td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.k97xzh">SAM</a> <a href="https://doi.org/10.25504/FAIRsharing.hza1ec">BAM</a> <a href="https://doi.org/10.25504/FAIRsharing.f846bd">CRAM</a></td>
      <td>Raw sequence can also be stored in unaligned SAM/ BAM/ CRAM format.</td>
      <td><a href="http://www.ebi.ac.uk/ena/submit/genomes-sequence-submission">ENA</a></td>
    </tr>
    <tr>
      <td>
      Assembled DNA sequence</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.rz4vfg">FASTA</a></td>
      <td>Assemblies without annotation are generally stored in FASTA format.
      </td>
      <td><a href="http://www.ebi.ac.uk/ena/submit/genomes-sequence-submission">ENA</a></td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.q9nh66">Flat file</a></td>
      <td>Annotation can be integrated with assemblies in contig, scaffold or 
      chromosome flat file format. </td>
      <td><a href="http://www.ebi.ac.uk/ena/submit/genomes-sequence-submission">ENA</a></td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.mg1mdc">AGP</a></td>
      <td>AGP (A Gold Path) files are used to describe how smaller fragments are placed in an 
      assembly but do not contain the sequence information themselves. </td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Aligned DNA 
      sequence</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.k97xzh">SAM</a> <a href="https://doi.org/10.25504/FAIRsharing.hza1ec">BAM</a> <a href="https://doi.org/10.25504/FAIRsharing.f846bd">CRAM</a></td>
      <td>Sequences aligned to a reference are represented in sequence 
      alignment and mapping format (SAM). Its binary version is 
      called BAM and further compression can be done using the 
      CRAM format.</td>
      <td><a href="http://www.ebi.ac.uk/ena/submit/genomes-sequence-submission">ENA</a></td>
    </tr>
    <tr>
      <td>Gene model or genomic feature annotation</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.sggb1n">GTF</a> <a href="https://doi.org/10.25504/FAIRsharing.qaaj0q">GFF</a> <a href="https://doi.org/10.25504/FAIRsharing.dnk0f6">GFF3</a></td>
      <td>General feature format or general transfer format are 
      commonly used to store genomic features in tab-delimited 
      flat text format. GFF3 is a more advanced version of the 
      basic GFF that allows description of more complex 
      features.</td>
      <td><a href="http://www.ensembl.org/info/website/upload/">Ensembl</a></td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.mwmbpq">BED</a></td>
      <td>
      BED (Browser Extensible Data) format is a tab-delimited text format that also allows 
      definition of how a feature should be displayed (e.g. on a genome browser)</td>
      <td><a href="http://www.ensembl.org/info/website/upload/">Ensembl</a></td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.rg2vmt">GB/GBK</a></td>
      <td>GenBank flat file Format (GB/GBK) is also commonly used but not well standardised</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Gene functional annotation</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.77fbbf">GAF</a> <a href="https://doi.org/10.25504/FAIRsharing.rtm51">GPAD</a><a href="https://doi.org/10.25504/FAIRsharing.820ebm">GPI</a></td>
      <td>A GAF file is a Gene Ontology Annotation File containing annotations 
      made to the GO by a contributing resource such as FlyBase 
      or Pombase. However, the GAF standard is applicable 
      outside of GO, e.g. using other ontologies such as PO. GAF 
      (v2) is a simple tab-delimited file format with 17 columns 
      to describe an entity (e.g. a protein), its annotation and 
      some annotation metadata</td>
      <td><a href="http://geneontology.org/docs/submitting-go-annotations/">GeneOntology</a></td>
    </tr>
    <tr>
      <td>Genetic/genomic variants</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.cfzz0h">VCF</a></td>
      <td>A tab-delimited text format to store meta-information as 
      header lines followed by information about variants position in the genome.</td>
      <td><a href="http://www.ensembl.org/info/website/upload/var.html">Ensembl</a>, <a href="https://www.ebi.ac.uk/eva/?Submit-Data">EVA</a></td>
    </tr>
    <tr>
      <td>Interaction data</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.77e3my">PSI-MI XML</a> <a href="https://doi.org/10.25504/FAIRsharing.ve0710">MITAB</a></td>
      <td>Data formats developed to exchange molecular interaction 
      data, related metadata and fully describe molecule 
      constructs.</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>Raw metabolite profile</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.26dmba">mzML</a> <a href="https://doi.org/10.25504/FAIRsharing.es03fk">nmrML</a></td>
      <td>XML based data formats that define mass spectrometry and 
      nuclear magnetic resonance raw data in Metabolomics</td>
      <td><a href="https://www.ebi.ac.uk/metabolights/">MetaboLights</a></td>
    </tr>
    <tr>
      <td>Protein sequence</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.rz4vfg">FASTA</a></td>
      <td>A text-based format for representing nucleotide sequences 
      or protein sequences, in which nucleotides or amino acids 
      are represented using single-letter codes.</td>
      <td><a href="https://www.uniprot.org">Uniprot</a></td>
    </tr>
    <tr>
      <td>Raw proteome profile</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.26dmba">mzML</a></td>
      <td>A formally defined XML format for representing mass 
      spectrometry data. Files typically contain sequences of 
      mass spectra, plus metadata about the experiment.</td>
      <td><a href="https://www.ebi.ac.uk/pride">PRIDE</a></td>
    </tr>
    <tr>
      <td>Organisms and specimens</td>
      <td><a href="https://doi.org/10.25504/FAIRsharing.xvf5y3">Darwin core</a></td>
      <td>The Darwin Core (DwC) standard facilitates the exchange of 
      information about biodiversity such as geographic location of organisms and 
      associated collection of specimens.</td>
      <td>&nbsp;</td>
    </tr>
  </table>
</div>
--->
