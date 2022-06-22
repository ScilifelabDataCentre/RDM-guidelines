---
title: Collecting phase
menu:
    bottom_about:
        name: Collect
        identifier: collect
        weight: 10
toc: True
---

## Collecting
<!-- About/intro to the phase -->
<!-- refer to metadata standard page /topic/topic/metadata.md -->

Click on the data type buttons below to see which facilities who offer data generation services:
<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample1" role="button" aria-expanded="false" aria-controls="collapseExample1">
    Genomics data
  </a>
</p>
<div class="collapse" id="collapseExample1">
  <div class="card card-body">
  <span>
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
    <li> <a href="http://escg.se/">Eukaryotic Single-Cell Genomics</a> (ESCG) offers streamlined single cell RNA sequencing, as well as whole genome DNA amplification</li>
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
  <ul>
    <li> <a href="https://www.scilifelab.se/facilities/alm/">Advanced Light Microscopy</a> (ALM) facility give support with advanced fluorescence microscopy for nanoscale biological visualization using SIM, STED, STORM/PALM superresolution imaging. The facility also support single molecule spectroscopy measurement and analysis with fluorescence correlation spectroscopy (FCS), as well as combined with superresolution dynamical studies (STED-FCS). Moreover, light-sheet fluorescence microscopy support allow users to image live and/or optically cleared larger samples. Submit your application at the NMI (National Microscopy Infrastructure) project portal.</li>
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
  <ul>
    <li> <a href="http://www.swedishmetabolomicscentre.se/">Swedish Metabolomics Centre</a> (SMC) specializes in analyzing metabolites and lipids with mass spectrometry based methods.</li>
    <li> <a href="https://www.scilifelab.se/facilities/swedish-nmr-centre/">Swedish NMR Centre</a> provides access to state-of-the-art NMR instrumentation and methodology.</li>
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
  <ul>
    <li> <a href="https://bioms.se/">Biological Mass Spectrometry</a> (BioMS) national infrastructure enables cutting-edge mass spectrometry and related advanced technology platforms to be part of your research projects.</li>
    <li> <a href="https://www.scilifelab.se/facilities/chemical-proteomics-proteogenomics">Chemical proteomics & proteogenomics</a> national facility offers state-of-the art mass spectrometry (MS)-based proteomics support, including experimental planning, MS analysis and data analysis related to proteogenomics and chemical proteomics.</li>
  </ul>
  </span>
  </div>
</div>

### Storage
The PI, and his/her academic institution are ultimately responsible for the data, and ensuring that all data is backed-up is essential. The 3-2-1 rule of thumb means that there should be 3 copies of the data, on 2 different types of media, and 1 of the copies at different physical location. This means that even if all of the projects research inputs and outputs are located at an analysis resource that has backup, a (third) copy of the data should be maintained.

For example, Uppmax systems have a 30-day incremental backup, and it has happened that users accidentally destroy their own data and don't notice for more than 30 days.

At least essential data, such as raw data and other data that may be difficult or even impossible to recreate in case of corruption or loss, should be copied off-site (using e.g. [Swestore](http://www.snic.se/resources/swestore/) or storage provided by the institute). 

Consider uploading the raw data to a repository already when receiving them, under an embargo (if that is important to you). This way you always have an off-site backup with the added benefit of making the data sharing phase more efficient.

<!-- ## Transfer data
should include a section about data transfer, with links to Uppmax user guides eg Grus, Bianca deliver guide, etc. Or put it under genomics card above. 
* [Grus user guide for delivery of data from NGI](https://www.uppmax.uu.se/support/user-guides/grus-user-guide/)
* [Basic SFTP commands for transferring files](https://uppmax.uu.se/support-sv/user-guides/basic-sftp-commands/)
* [SNIC-SENS Bianca Deliver user guide for NGI data](https://www.uppmax.uu.se/support/user-guides/deliver-user-guide/)
* [Transit user guide - secure data transfer of sensitive data](https://uppmax.uu.se/support-sv/user-guides/transit-user-guide/)
-->

### Resources & Training
* [RDMkit on Collecting Data](https://rdmkit.elixir-europe.org/collecting)
* [RDMkit on Data transfer](https://rdmkit.elixir-europe.org/data_transfer.html)
* [Data organisation module](https://nbisweden.github.io/module-organising-data-dm-practices/) in course [Introduction to data management practices](https://uppsala.instructure.com/courses/48087/pages/introduction-to-data-management-practices)

