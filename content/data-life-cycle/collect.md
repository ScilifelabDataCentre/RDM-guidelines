---
title: Collecting phase
phase: Collect
tags: ["data producers", "storage", "genomics data", "imaging data", "metabolomics data", "proteomics data", "documentation"]
toc: True
---

# Collecting
During this phase all necessary data to be analysed in the project is collected, either by generating new datasets or by reusing earlier collected datasets. This phase lays the foundation of the quality of both the data and the accompanying documentation. Hence, it is important that quality measures are implemented and that all steps of collection is appropriately recorded. During this phase possibly large amounts of data might need to be transferred between data producers, compute facilities and storage facilities.

<a class="link-teal" href="/data-life-cycle/reuse"><b>Learn more about data reuse <i class="bi bi-arrow-right-square"></i></b></a>
<br><br>
<a class="link-teal" href="/topics/data-transfer"><b>Learn more about data transfer <i class="bi bi-arrow-right-square"></i></b></a>
<br><br>

## Documentation
Data documentation should clearly describe how the data was collected, so that someone else can understand and correctly interpret the data. Documentations can be keept as a README file, both on a higher project-level or on a more detailed level. Make use of electronic lab notebooks (often offered by the university / institute) and metadata standards, and name and organise the files produced appropriately, see e.g. *'<a href="https://doi.org/10.1371/journal.pcbi.1000424" target="_blank">A Quick Guide to Organizing Computational Biology Projects</a>'* for advice. 

<a class="link-teal" href="/topics/readme-files"><b>Learn more about README files <i class="bi bi-arrow-right-square"></i></b></a>
<br><br>
<a class="link-teal" href="/topics/metadata"><b>Learn more about metadata standards <i class="bi bi-arrow-right-square"></i></b></a>
<br><br>

## Data producers
 SciLifeLab provides access to a range of pioneering technologies in molecular biosciences. Please find below links to data generating SciLifeLab services.

<a class="btn btn-round btn-aqua" href="https://www.scilifelab.se/genomics/" target="_blank">SciLifeLab Genomics <i class="bi bi-box-arrow-up-right"></i></a>
<br>

<a class="btn btn-round btn-aqua" href="https://www.scilifelab.se/proteomics/" target="_blank">SciLifeLab Proteomics <i class="bi bi-box-arrow-up-right"></i></a>
<br>

<a class="btn btn-round btn-aqua" href="https://www.scilifelab.se/metabolomics-and-exposomics/" target="_blank">SciLifeLab Matabolomics and Exposomics <i class="bi bi-box-arrow-up-right"></i></a>
<br>

<a class="btn btn-round btn-aqua" href="https://www.scilifelab.se/spatial-omics/" target="_blank">SciLifeLab Spatial Omics <i class="bi bi-box-arrow-up-right"></i></a>
<br>

<a class="btn btn-round btn-aqua" href="https://www.scilifelab.se/cellular-and-molecular-imaging/" target="_blank">SciLifeLab Cellular and Molecular Imaging <i class="bi bi-box-arrow-up-right"></i></a>
<br>

<a class="btn btn-round btn-aqua" href="https://www.scilifelab.se/structural-biology/" target="_blank">SciLifeLab Structural Biology <i class="bi bi-box-arrow-up-right"></i></a>
<br><br>

## Storage
The PI, and his/her academic institution are ultimately responsible for the data, and ensuring that all data is backed-up is essential. The 3-2-1 rule of thumb means that there should be 3 copies of the data, on 2 different types of media, and 1 of the copies at different physical location. This means that even if all the projects research inputs and outputs are located at a backed-up resource, a (third) copy of the data should be maintained.

At least essential data, such as raw data and other data that may be difficult or even impossible to recreate in case of corruption or loss, should be copied off-site (using e.g. SciLifeLab FAIR Storage or storage provided by the institute).

Consider uploading the raw data to a repository already when receiving them, under an embargo (if it is important that the data remains private during the project). This way there is always an off-site backup with the added benefit of making the data sharing phase more efficient.

<a class="link-teal" href="https://data.scilifelab.se/services/fairstorage/" target="_blank"><b>Learn more about SciLifeLab FAIR Storage <i class="bi bi-box-arrow-up-right"></i></b></a>
<br>

<a class="link-teal" href="/data-life-cycle/preserve"><b>Learn more about data preserving <i class="bi bi-arrow-right-square"></i></b></a>
<br>

<a class="link-teal" href="/data-life-cycle/share"><b>Learn more about data sharing <i class="bi bi-arrow-right-square"></i></b></a>
<br><br>

## Resources
Please find below resources concerning the research data life cycle phase collect in form of training, guidance and/or tools.

{{< resources-per-page-phases >}}
