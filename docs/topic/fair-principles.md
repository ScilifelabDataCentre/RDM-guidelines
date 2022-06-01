# FAIR principles

[FAIR](https://www.force11.org/group/fairgroup/fairprinciples) stands for Findable, Accessible, Interoperable and Reusable:

* To be **Findable**: Data and metadata should be easy to find by both humans and computer systems. Basic machine readable descriptive metadata allows the discovery of interesting data sets and services.

* To be **Accessible**: Data and metadata should be stored for the long term such that they can be easily accessed and downloaded or locally used by machines and humans using standard communication protocols.

* To be **Interoperable**: Data should be ready to be exchanged, interpreted and combined in a (semi)automated way with other data sets by humans as well as computer systems.

* To be **Reusable**: Data and metadata are sufficiently well-described to allow data to be reused in future research, allowing for integration with other compatible data sources. Proper citation must be facilitated, and the conditions under which the data can be used should be clear to machines and humans.


In [Wilkinson, et al 2016](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4792175/pdf/sdata201618.pdf) a set of principles were defined for each of these properties. Below, each of the principles are explained further as adapted from [FAIR principles translation](http://www.snf.ch/SiteCollectionDocuments/FAIR_principles_translation_SNSF_logo.pdf).


## F1. (meta)data are assigned a globally unique and persistent identifier	
**Explanation:** Each data set is assigned a globally unique and persistent identifier (PID), for example a [DOI](https://www.doi.org/). These identifiers allow to find, cite and track (meta)data.	

**Action:** Ensure that each data set is assigned a globally unique and persistent identifier. Certain repositories automatically assign identifiers to data sets as a service. If not, researchers must obtain a PID via a PID registration service.

## F2. data are described with rich metadata (defined by R1 below)	
**Explanation:** Each data set is thoroughly (see below, in R1) described: these metadata document how the data was generated, under what term (license) and how it can be (re)used, and provide the necessary context for proper interpretation. This information needs to be machine-readable.	

**Action:** Fully document each data set in the metadata, which may include descriptive information about the context, quality and condition, or characteristics of the data. Another researcher in any field, or their computer, should be able to properly understand the nature of your dataset. Be as generous as possible with your metadata (see R1).

## F3. metadata clearly and explicitly include the identifier of the data it describes	
**Explanation:** The metadata and the data set they describe are separate files. The association between a metadata file and the data set is obvious thanks to the mention of the data set’s PID in the metadata.	

**Action:** Make sure that the metadata contains the data set’s PID.

## F4. (meta)data are registered or indexed in a searchable resource	
**Explanation:** Metadata are used to build easily searchable indexes of data sets. These resources will allow to search for existing data sets similarly to searching for a book in a library.	

**Action:** Provide detailed and complete metadata for each data set (see F2).

## A1. (meta)data are retrievable by their identifier using a standardized communications protocol	
**Explanation:** If one knows a data set’s identifier and the location where it is archived, one can access at least the metadata. Furthermore, the user knows how to proceed to get access to the data.	

**Action:** Clearly define who can access the actual data, and specify how. It is possible that data will actually not be downloaded, but rather reused in situ. If so, the metadata must specify the conditions under which this is allowed (sometimes versus the conditions needed to fulfill for external usage/“download”).

### A1.1 the protocol is open, free, and universally implementable	
**Explanation:** Anyone with a computer and an internet connection can access at least the metadata.

### A1.2 the protocol allows for an authentication and authorization procedure, where necessary	
**Explanation:** It often makes sense to request users to create a user account on a repository. This allows to authenticate the owner (or contributor) of each data set, and to potentially set user specific rights.

### A2. metadata are accessible, even when the data are no longer available	
**Explanation:** Maintaining all data sets in a readily usable state eternally would require an enormous amount of curation work (adapting to new standards for formats, converting to different format if specifically needed software is discontinued, etc.). Keeping the metadata describing each data set accessible, however, can be done with much less resources. This allows to build comprehensive data indexes including all current, past and potentially arising data sets.	

**Action:** Provide detailed and complete metadata for each data set (see below in R1).

## I1. (meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation
**Explanation:** Interoperability typically means that each computer system has at least knowledge of the other system’s formats in which data is exchanged. If (meta)data are to be searchable and if compatible data sources should be combinable in a (semi)automatic way, computer systems need to be able to decide if the content of data sets are comparable. Obvious issues arise when different languages are used to describe the data or when spelling errors make the comparison of descriptions and variable names more difficult. It is critical to use controlled vocabularies and a well-defined framework to describe and structure (meta)data in order to ensure findability and interoperability of datasets.	

**Action:** Provide machine readable data and metadata in an accessible language, using a well-established formalism. In particular, data and metadata are annotated with resolvable vocabularies/ontologies/thesauri that are commonly used in the field. The [RDF](https://www.w3.org/RDF/) extensible knowledge representation model is a way to describe and structure datasets. You can refer to the [Dublin Core Schema](https://dublincore.org/schemas/) as an example.

## I2. (meta)data use vocabularies that follow FAIR principles	
**Explanation:** The controlled vocabulary used to describe data sets needs to be documented. This documentation needs to be easily findable and accessible by anyone who uses the data set.

**Action:** The vocabularies/ontologies/thesauri are themselves findable, accessible, interoperable and thoroughly documented, hence FAIR. Researchers can refer to metrics assessing the FAIRness of a digital resource (if available).

## I3. (meta)data include qualified references to other (meta)data	
**Explanation:** If the data set builds on another data set, if additional data sets are needed to complete the data, or if complementary information is stored in a different data set, this needs to be specified. In particular, the scientific link between the data sets needs to be described. Furthermore, all data sets need to be properly cited (i.e. including their persistent identifiers).	

**Action:** Properly cite relevant/associated data sets, in particular by providing their persistent identifiers, in the metadata, and describe the scientific link/relation to your data set.

## R1. meta(data) are richly described with a plurality of accurate and relevant attributes	
**Explanation:** Description of a data set is required at two different levels:
* metadata describing the data set (intrinsic): what does the data set contain, how was the data generated, how has it been processed, how can it be reused …
* metadata describing the data (submitterdefined): any needed information to properly use the data, such as definitions of the variable names

**Action:** Provide complete metadata for each data file. Some points to take into consideration (non-exhaustive list):
* Scope of your data: for what purpose was it generated/collected?
* Particularities or limitations about the data that other users should be aware of.
* Date of the data set generation, lab conditions, who prepared the data, parameter settings, name and version of the software used.
* Is it raw or processed data?
* Variable names are explained or self-explanatory (i.e. defined in the research field’s controlled vocabulary).
* Version of the archived and/or reused data is clearly specified and documented.

### R1.1. (meta)data are released with a clear and accessible data usage license	
**Explanation:** The conditions under which the data can be used should be clear to machines and humans. This has to be specified in the metadata describing a data set.

**Action:** Include information about the license in the metadata. If a particular license is needed, you have to provide it along with the data set. Where possible it is suggested to use common licenses, such as CC 0, CC BY, etc., which can be referred to by URL.

### R1.2. (meta)data are associated with detailed provenance	
**Explanation:** Detailed information about the provenance of data is necessary for reuse: this will, for example, allow researchers to understand how the data was generated, in which context it can be reused, and how reliable it is. Provenance is a central issue in scientific databases to validate data.	

**Action:** The metadata to thoroughly describe the workflow that led to your data: Who generated or collected it? How has it been processed? Has it been published before? Does it contain data from someone else, potentially transformed or completed? Ideally the workflow is described in a machine-readable format. Criterion I3 is closely linked to this issue when reusing published data sets.

### R1.3. (meta)data meet domainrelevant community standards	
**Explanation:** It is easier to reuse data sets if they are similar: same type of data, data organized in a standardized way, well-established and sustainable file formats, documentation (metadata) following a common template and using common vocabulary. If community standards or best practices for data archiving and sharing exist, they should be followed. Note that quality issues are not addressed by the FAIR principles. How reliable data is lies in the eye of the beholder and depends on the foreseen application.

**Action:** Prepare your (meta)data according to community standards and best practices for data archiving and sharing in your research field. There might be situations where good practice exist for the type of data to be submitted but the submitter has valid and specified reasons to divert from the standard practice. This needs to be addressed in the metadata.