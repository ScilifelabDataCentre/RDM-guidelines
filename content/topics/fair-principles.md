---
title: FAIR principles
category: Other
toc: True
---

# FAIR principles

[FAIR](https://www.force11.org/group/fairgroup/fairprinciples) stands for Findable, Accessible, Interoperable and Reusable. In [Wilkinson, et al 2016](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4792175/pdf/sdata201618.pdf) (PDF) a set of principles were defined for each of these properties. Below, each of the principles are explained further (click on the buttons for detailed information), as adapted from [FAIR principles translation](http://www.snf.ch/SiteCollectionDocuments/FAIR_principles_translation_SNSF_logo.pdf) (PDF).

## Findable
Data and metadata should be easy to find by both humans and computer systems. Basic machine readable descriptive metadata allows the discovery of interesting datasets and services.
<p>
  <button class="btn-expandable"> <a data-bs-toggle="collapse" href="#collapseFind1" role="button" aria-expanded="false" aria-controls="collapseFind1">
    F1: Persistent identifier
    <i class="bi bi-chevron-double-down p-2"></i>
  </a></button>
</p>
<div class="collapse" id="collapseFind1">
  <div class="card">
    <div class="card-header"><h3>F1: (meta)data are assigned a globally unique and persistent identifier</h3></div>
    <div class="card-body">
    <span>
      <b>Explanation:</b> Each dataset is assigned a globally unique and persistent identifier (PID), for example a <a href="https://www.doi.org/">DOI</a>. These identifiers allow to find, cite and track (meta)data.	<br><br>
      <b>Action:</b> Ensure that each dataset is assigned a globally unique and persistent identifier. Certain repositories automatically assign identifiers to datasets as a service. If not, researchers must obtain a PID via a PID registration service.
    </span>
    </div>
  </div>  
  <br>
</div>
<p>
  <button class="btn-expandable"> <a data-bs-toggle="collapse" href="#collapseFind2" role="button" aria-expanded="false" aria-controls="collapseFind2">
    F2: Rich metadata
    <i class="bi bi-chevron-double-down p-2"></i>
  </a></button>
</p>
<div class="collapse" id="collapseFind2">
  <div class="card">
    <div class="card-header"><h3>F2: data are described with rich metadata</h3></div>
    <div class="card-body">
    <span>
      <b>Explanation:</b> Each dataset is thoroughly (see below, in R1) described: these metadata document how the data was generated, under what term (license) and how it can be (re)used, and provide the necessary context for proper interpretation. This information needs to be machine-readable.	<br><br>
      <b>Action:</b> Fully document each dataset in the metadata, which may include descriptive information about the context, quality and condition, or characteristics of the data. Another researcher in any field, or their computer, should be able to properly understand the nature of your dataset. Be as generous as possible with your metadata (see R1).
    </span>
    </div>
  </div>  
  <br>
</div>
<p>
  <button class="btn-expandable"> <a data-bs-toggle="collapse" href="#collapseFind3" role="button" aria-expanded="false" aria-controls="collapseFind3">
    F3: Include identifier
    <i class="bi bi-chevron-double-down p-2"></i>
  </a></button>
</p>
<div class="collapse" id="collapseFind3">
  <div class="card">
    <div class="card-header"><h3>F3: metadata clearly and explicitly include the identifier of the data it describes</h3></div>
    <div class="card-body">
    <span>
      <b>Explanation:</b>The metadata and the dataset they describe are separate files. The association between a metadata file and the dataset is obvious thanks to the mention of the dataset’s PID in the metadata. 	<br><br>
      <b>Action:</b> Make sure that the metadata contains the dataset’s PID.
    </span>
    </div>
  </div>  
  <br>
</div>
<p>
  <button class="btn-expandable"> <a data-bs-toggle="collapse" href="#collapseFind4" role="button" aria-expanded="false" aria-controls="collapseFind4">
    F4: Searchable resource
    <i class="bi bi-chevron-double-down p-2"></i>
  </a></button>
</p>
<div class="collapse" id="collapseFind4">
  <div class="card">
    <div class="card-header"><h3>F4: (meta)data are registered or indexed in a searchable resource</h3></div>
    <div class="card-body">
    <span>
      <b>Explanation:</b> Metadata are used to build easily searchable indexes of datasets. These resources will allow to search for existing datasets similarly to searching for a book in a library.	<br><br>
      <b>Action:</b> Provide detailed and complete metadata for each dataset (see F2).
    </span>
    </div>
  </div>  
</div>

## Accessible
Data and metadata should be stored for the long term such that they can be easily accessed and downloaded or locally used by machines and humans using standard communication protocols.
<p>
  <button class="btn-expandable"> <a data-bs-toggle="collapse" href="#collapseAccess1" role="button" aria-expanded="false" aria-controls="collapseAccess1">
    A1: Standardized communication protocol
    <i class="bi bi-chevron-double-down p-2"></i>
  </a></button>
</p>
<div class="collapse" id="collapseAccess1">
  <div class="card">
    <div class="card-header"><h3>A1: (meta)data are retrievable by their identifier using a standardized communications protocol</h3></div>
    <div class="card-body">
    <span>
      <b>Explanation:</b> If one knows a dataset’s identifier and the location where it is archived, one can access at least the metadata. Furthermore, the user knows how to proceed to get access to the data.	<br><br>
      <b>Action:</b> Clearly define who can access the actual data, and specify how. It is possible that data will actually not be downloaded, but rather reused in situ. If so, the metadata must specify the conditions under which this is allowed (sometimes versus the conditions needed to fulfill for external usage/“download”).
    </span>
    </div>
  </div>  
  <br>
</div>
<p>
  <button class="btn-expandable"> <a data-bs-toggle="collapse" href="#collapseAccess2" role="button" aria-expanded="false" aria-controls="collapseAccess2">
    A1.1: Open protocol
    <i class="bi bi-chevron-double-down p-2"></i>
  </a></button>
</p>
<div class="collapse" id="collapseAccess2">
  <div class="card">
    <div class="card-header"><h3>A1.1: the protocol is open, free, and universally implementable</h3></div>
    <div class="card-body">
    <span>
      <b>Explanation:</b> Anyone with a computer and an internet connection can access at least the metadata.
    </span>
    </div>
  </div>  
  <br>
</div>
<p>
  <button class="btn-expandable"> <a data-bs-toggle="collapse" href="#collapseAccess3" role="button" aria-expanded="false" aria-controls="collapseAccess3">
    A1.2: Authentication
    <i class="bi bi-chevron-double-down p-2"></i>
  </a></button>
</p>
<div class="collapse" id="collapseAccess3">
  <div class="card">
    <div class="card-header"><h3>A1.2: the protocol allows for an authentication and authorization procedure, where necessary</h3></div>
    <div class="card-body">
    <span>
      <b>Explanation:</b> It often makes sense to request users to create a user account on a repository. This allows to authenticate the owner (or contributor) of each dataset, and to potentially set user specific rights.
    </span>
    </div>
  </div>  
  <br>
</div>
<p>
  <button class="btn-expandable"> <a data-bs-toggle="collapse" href="#collapseAccess4" role="button" aria-expanded="false" aria-controls="collapseAccess4">
    A2: Persistent metadata
    <i class="bi bi-chevron-double-down p-2"></i>
  </a></button>
</p>
<div class="collapse" id="collapseAccess4">
  <div class="card">
    <div class="card-header"><h3>A2: metadata are accessible, even when the data are no longer available</h3></div>
    <div class="card-body">
    <span>
      <b>Explanation:</b> Maintaining all datasets in a readily usable state eternally would require an enormous amount of curation work (adapting to new standards for formats, converting to different format if specifically needed software is discontinued, etc.). Keeping the metadata describing each dataset accessible, however, can be done with much less resources. This allows to build comprehensive data indexes including all current, past and potentially arising datasets.	<br><br>
      <b>Action:</b> Provide detailed and complete metadata for each dataset (see below in R1).
    </span>
    </div>
  </div>  
</div>

## Interoperable
Data should be ready to be exchanged, interpreted and combined in a (semi)automated way with other datasets by humans as well as computer systems.
<p>
  <button class="btn-expandable"> <a data-bs-toggle="collapse" href="#collapseInterop1" role="button" aria-expanded="false" aria-controls="collapseInterop1">
    I1: Formal language
    <i class="bi bi-chevron-double-down p-2"></i>
  </a></button>
</p>
<div class="collapse" id="collapseInterop1">
  <div class="card">
    <div class="card-header"><h3>I1: (meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation</h3></div>
    <div class="card-body">
    <span>
      <b>Explanation:</b> Interoperability typically means that each computer system has at least knowledge of the other system’s formats in which data is exchanged. If (meta)data are to be searchable and if compatible data sources should be combinable in a (semi)automatic way, computer systems need to be able to decide if the content of datasets are comparable. Obvious issues arise when different languages are used to describe the data or when spelling errors make the comparison of descriptions and variable names more difficult. It is critical to use controlled vocabularies and a well-defined framework to describe and structure (meta)data in order to ensure findability and interoperability of datasets.	<br><br>
      <b>Action:</b> Provide machine readable data and metadata in an accessible language, using a well-established formalism. In particular, data and metadata are annotated with resolvable vocabularies/ontologies/thesauri that are commonly used in the field. The <a href="https://www.w3.org/RDF/">RDF</a> extensible knowledge representation model is a way to describe and structure datasets. You can refer to the <a href="https://dublincore.org/schemas/">Dublin Core Schema</a> as an example.
    </span>
    </div>
  </div>  
  <br>
</div>
<p>
  <button class="btn-expandable"> <a data-bs-toggle="collapse" href="#collapseInterop2" role="button" aria-expanded="false" aria-controls="collapseInterop2">
    I2: FAIR vocabularies
    <i class="bi bi-chevron-double-down p-2"></i>
  </a></button>
</p>
<div class="collapse" id="collapseInterop2">
  <div class="card">
    <div class="card-header"><h3>I2: (meta)data use vocabularies that follow FAIR principles</h3></div>
    <div class="card-body">
    <span>
      <b>Explanation:</b> The controlled vocabulary used to describe datasets needs to be documented. This documentation needs to be easily findable and accessible by anyone who uses the dataset.	<br><br>
      <b>Action:</b> The vocabularies/ontologies/thesauri are themselves findable, accessible, interoperable and thoroughly documented, hence FAIR. Researchers can refer to metrics assessing the FAIRness of a digital resource (if available).
    </span>
    </div>
  </div>  
  <br>
</div>
<p>
  <button class="btn-expandable"> <a data-bs-toggle="collapse" href="#collapseInterop3" role="button" aria-expanded="false" aria-controls="collapseInterop3">
    I3: Include references
    <i class="bi bi-chevron-double-down p-2"></i>
  </a></button>
</p>
<div class="collapse" id="collapseInterop3">
  <div class="card">
    <div class="card-header"><h3>I3: (meta)data include qualified references to other (meta)data</h3></div>
    <div class="card-body">
    <span>
      <b>Explanation:</b> If the dataset builds on another dataset, if additional datasets are needed to complete the data, or if complementary information is stored in a different dataset, this needs to be specified. In particular, the scientific link between the datasets needs to be described. Furthermore, all datasets need to be properly cited (i.e. including their persistent identifiers).	<br><br>
      <b>Action:</b> Properly cite relevant/associated datasets, in particular by providing their persistent identifiers, in the metadata, and describe the scientific link/relation to your dataset.
    </span>
    </div>
  </div>  
</div>

## Reusable
Data and metadata are sufficiently well-described to allow data to be reused in future research, allowing for integration with other compatible data sources. Proper citation must be facilitated, and the conditions under which the data can be used should be clear to machines and humans.
<p>
  <button class="btn-expandable"> <a data-bs-toggle="collapse" href="#collapseReuse1" role="button" aria-expanded="false" aria-controls="collapseReuse1">
    R1: Rich description
    <i class="bi bi-chevron-double-down p-2"></i>
  </a></button>
</p>
<div class="collapse" id="collapseReuse1">
  <div class="card">
    <div class="card-header"><h3>R1: meta(data) are richly described with a plurality of accurate and relevant attributes</h3></div>
    <div class="card-body">
    <span>
      <b>Explanation:</b> Description of a dataset is required at two different levels:
      <ul>
        <li>metadata describing the dataset (intrinsic): what does the dataset contain, how was the data generated, how has it been processed, how can it be reused...</li>
        <li>metadata describing the data (submitterdefined): any needed information to properly use the data, such as definitions of the variable names</li>
      </ul>
      <b>Action:</b> Provide complete metadata for each data file. Some points to take into consideration (non-exhaustive list):
      <ul>
        <li>Scope of your data: for what purpose was it generated/collected?</li>
        <li>Particularities or limitations about the data that other users should be aware of.</li>
        <li>Date of the dataset generation, lab conditions, who prepared the data, parameter settings, name and version of the software used.</li>
        <li>Is it raw or processed data?</li>
        <li>Variable names are explained or self-explanatory (i.e. defined in the research field’s controlled vocabulary).</li>
        <li>Version of the archived and/or reused data is clearly specified and documented.</li>
      </ul>
    </span>
    </div>
  </div>  
  <br>
</div>
<p>
  <button class="btn-expandable"> <a data-bs-toggle="collapse" href="#collapseReuse2" role="button" aria-expanded="false" aria-controls="collapseReuse2">
    R1.1: License
    <i class="bi bi-chevron-double-down p-2"></i>
  </a></button>
</p>
<div class="collapse" id="collapseReuse2">
  <div class="card">
    <div class="card-header"><h3>R1.1: (meta)data are released with a clear and accessible data usage license</h3></div>
    <div class="card-body">
    <span>
      <b>Explanation:</b> The conditions under which the data can be used should be clear to machines and humans. This has to be specified in the metadata describing a dataset.	<br><br>
      <b>Action:</b> Include information about the license in the metadata. If a particular license is needed, you have to provide it along with the dataset. Where possible it is suggested to use common licenses, such as CC 0, CC BY, etc., which can be referred to by URL.
    </span>
    </div>
  </div>  
  <br>
</div>
<p>
  <button class="btn-expandable"> <a data-bs-toggle="collapse" href="#collapseReuse3" role="button" aria-expanded="false" aria-controls="collapseReuse3">
    R1.2: Provenance
    <i class="bi bi-chevron-double-down p-2"></i>
  </a></button>
</p>
<div class="collapse" id="collapseReuse3">
  <div class="card">
    <div class="card-header"><h3>R1.2. (meta)data are associated with detailed provenance</h3></div>
    <div class="card-body">
    <span>
      <b>Explanation:</b> Detailed information about the provenance of data is necessary for reuse: this will, for example, allow researchers to understand how the data was generated, in which context it can be reused, and how reliable it is. Provenance is a central issue in scientific databases to validate data.	<br><br>
      <b>Action:</b> The metadata to thoroughly describe the workflow that led to your data: Who generated or collected it? How has it been processed? Has it been published before? Does it contain data from someone else, potentially transformed or completed? Ideally the workflow is described in a machine-readable format. Criterion I3 is closely linked to this issue when reusing published datasets.
    </span>
    </div>
  </div>  
  <br>
</div>
<p>
  <button class="btn-expandable"> <a data-bs-toggle="collapse" href="#collapseReuse4" role="button" aria-expanded="false" aria-controls="collapseReuse4">
    R1.3: Community standards
    <i class="bi bi-chevron-double-down p-2"></i>
  </a></button>
</p>
<div class="collapse" id="collapseReuse4">
  <div class="card">
    <div class="card-header"><h3>R1.3: (meta)data meet domain relevant community standards</h3></div>
    <div class="card-body">
    <span>
      <b>Explanation:</b> It is easier to reuse datasets if they are similar: same type of data, data organized in a standardized way, well-established and sustainable file formats, documentation (metadata) following a common template and using common vocabulary. If community standards or best practices for data archiving and sharing exist, they should be followed. Note that quality issues are not addressed by the FAIR principles. How reliable data is lies in the eye of the beholder and depends on the foreseen application.	<br><br>
      <b>Action:</b> Prepare your (meta)data according to community standards and best practices for data archiving and sharing in your research field. There might be situations where good practice exist for the type of data to be submitted but the submitter has valid and specified reasons to divert from the standard practice. This needs to be addressed in the metadata.
    </span>
    </div>
  </div>  
  <br>
</div>

## Resources
Please find below resources concerning the FAIR principles in form of training, guidance and/or tools.

{{< resources-per-page-topics >}}
