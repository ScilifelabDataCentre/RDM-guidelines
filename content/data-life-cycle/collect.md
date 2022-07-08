---
title: Collecting phase
menu:
    bottom_about:
        name: Collect
        identifier: collect
        weight: 10
toc: True
---

# Collecting

During this phase all necessary data to be analysed in the project is collected, either by generating new datasets or by [reusing](data-life-cycle/reuse) earlier collected datasets. This phase lays the foundation of the quality of both the data and the accompanying documentation. Hence, it is important that quality measures are implemented and that all steps of collection is appropriately recorded.

## Documentation
Data documentation should clearly describe how the data was collected, so that someone else can understand and correctly interpret the data. Make use of electronic lab notebooks (often offered by the university / institute) and [metadata standards](/topic/metadata), and name and organise the files produced appropriately.
 
## Data producers
Click on the data type buttons below to see SciLifeLab units who offer data generation services:
<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample1" role="button" aria-expanded="false" aria-controls="collapseExample1">
    Genomics data
  </a>
</p>
<div class="collapse" id="collapseExample1">
  <div class="card card-body">
  <span>
  <p>Please find below a selection of <a href="https://www.scilifelab.se/services/infrastructure?service=genomics">SciLifeLab Genomics services</a>:
  <ul>
    <li> <a href="https://ngisweden.scilifelab.se/">National Genomics Infrastructure</a> (NGI) offers an infrastructure equipped with a comprehensive range of technology platforms for next generation sequencing (NGS) and genotyping.</li>
    <ul>
      <li> Whole-genome sequencing (human)</li>
      <li> RNA sequencing</li>
      <li> Functional genomics & Epigenomics</li>
      <li> De novo genome sequencing</li>
      <li> Metagenomics</li>
      <li> Single-cell genomics</li>
    </ul>
    <li> <a href="https://www.scilifelab.se/units/eukaryotic-single-cell-genomics/">Eukaryotic Single Cell Genomics</a> (ESCG) offers high-throughput single cell transcriptomics services.</li>
    <li> <a href="https://www.scilifelab.se/units/microbial-single-cell-genomics/">Microbial Single Cell Genomics</a> provides customized, low to high-throughput experimental services for Swedish and international researchers working with prokaryotic and eukaryotic microbes. </li>
  </ul>
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
    <p>Please find below a selection of <a href="https://www.scilifelab.se/services/infrastructure?service=bioimaging-and-molecular-structure">SciLifeLab Bioimaging and Molecular Structure services</a>:
  <ul>
    <li> <a href="https://www.scilifelab.se/units/alm/">Advanced Light Microscopy</a> (ALM) unit give support with advanced fluorescence microscopy for nanoscale biological visualization, single molecule spectroscopy measurement and analysis with fluorescence correlation spectroscopy (FCS), as well as combined with superresolution dynamical studies (STED-FCS). Moreover, light-sheet fluorescence microscopy support allow users to image live and/or optically cleared larger samples.</li>
    <li> <a href="https://cryoem.scilifelab.se/">Cryo-EM</a> offers access to state-of-the-art equipment and expertise in single particle cryo-EM and cryo-tomography (cryo-ET).</li>
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
    <p>Please find below a selection of <a href="https://www.scilifelab.se/services/infrastructure?metabolomics">SciLifeLab Metabolomics services</a>:
  <ul>
    <li> <a href="http://www.swedishmetabolomicscentre.se/">Swedish Metabolomics Centre</a> (SMC) specializes in analyzing metabolites and lipids with mass spectrometry based methods.</li>
    <li> <a href="https://www.scilifelab.se/units/swedish-nmr-centre/">Swedish NMR Centre</a> provides access to state-of-the-art NMR instrumentation and methodology.</li>
  </ul>
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
    <p>Please find below a selection of <a href="https://www.scilifelab.se/services/infrastructure?proteomics">SciLifeLab Proteomics services</a>:
  <ul>
    <li> <a href="">Global Proteomics and Proteogenomics</a> offers proteomics information combined with sample specific genomic and transcriptomics information.</li>
    <li> <a href="https://www.scilifelab.se/units/chemical-proteomics/">Chemical proteomics</a> is a national unit expert on supporting drug discovery and development by proteome-wide deconvolution of targets and action mechanisms of small molecules.</li>
  </ul>
  <p>Also available is <a href="https://bioms.se/">Biological Mass Spectrometry</a> (BioMS) national infrastructure, which enables cutting-edge mass spectrometry and related advanced technology platforms.</p>
  </span>
  </div>
</div>

## Storage
The PI, and his/her academic institution are ultimately responsible for the data, and ensuring that all data is backed-up is essential. The 3-2-1 rule of thumb means that there should be 3 copies of the data, on 2 different types of media, and 1 of the copies at different physical location. This means that even if all the projects research inputs and outputs are located at a backed-up resource, a (third) copy of the data should be maintained.

At least essential data, such as raw data and other data that may be difficult or even impossible to recreate in case of corruption or loss, should be copied off-site (using e.g. [Swestore](http://www.snic.se/resources/swestore/) or storage provided by the institute). 

Consider uploading the raw data to a repository already when receiving them, under an embargo (if it is important that the data remains private during the project). This way there is always an off-site backup with the added benefit of making the [data sharing](/data-life-cycle/share) phase more efficient.

## Data transfer
Quite often large amounts of data is generated, and it can be worth spending some time considering how to transfer data from the data producer to storage and analysis environment. Consider the capacity of the internet connection, transfer via a low bandwith network can be so time-consuming that it might be faster and easier to send the data on a hard drive through carrier services.

Please find below some useful links from the SNIC compute resource Uppmax regarding data transfer:
* [Grus user guide for delivery of data from NGI](https://www.uppmax.uu.se/support/user-guides/grus-user-guide/)
* [Basic SFTP commands for transferring files](https://uppmax.uu.se/support-sv/user-guides/basic-sftp-commands/)
* [SNIC-SENS Bianca Deliver user guide for NGI data](https://www.uppmax.uu.se/support/user-guides/deliver-user-guide/)
* [Transit user guide - secure data transfer of sensitive data](https://uppmax.uu.se/support-sv/user-guides/transit-user-guide/)


## Resources & Training
* [RDMkit on Collecting Data](https://rdmkit.elixir-europe.org/collecting)
* [RDMkit on Data quality](https://rdmkit.elixir-europe.org/data_quality)
* [RDMkit on Data transfer](https://rdmkit.elixir-europe.org/data_transfer.html)
* [Data organisation module](https://nbisweden.github.io/module-organising-data-dm-practices/) in course [Introduction to data management practices](https://uppsala.instructure.com/courses/48087/pages/introduction-to-data-management-practices)

