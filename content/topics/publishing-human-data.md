---
title: Publishing human data
contributors: []
toc: True
---

# Publishing human data

<div class="alert alert-warning" role="alert">
  <B><I>Disclaimer!</I></B> The PI, as well as everyone with access to sensitive personal data, is responsible for following current laws and regulations, and SciLifeLab will not assume legal responsibility for advice provided in these guidelines.
</div>

The GDPR states that the processing (including storing) of personal data should stop when the intended purpose of the processing is done. There are, however, exemptions to this e.g. when the processing is done for research purposes. Also, from a research ethics point of view, research data should be kept to make it possible for others to validate published findings and reuse data for new discoveries. This is also governed by what the data subjects have been informed about regarding how you will treat the data after project completion. The recommendation is to deposit the sensitive data in the appropriate controlled access repositories if such are available, but this requires that the data subjects are informed and have agreed to this.

<a href="/topics/research-involving-human-data"><b>See more guidelines on research involving human data <i class="bi bi-arrow-right-square-fill"></i></b></a>
<br/><br/>
<a href="/topics/gdpr-legal-reference.md"><b>See more guidelines on GDPR <i class="bi bi-arrow-right-square-fill"></i></b></a>
<br/><br/>


## Repositories for publishing human data

### FEGA Sweden
[Federated European Genome-phenome Archive (FEGA) Sweden](https://fega.nbis.se/) is an archive for storing and sharing data in Sweden in a way that meets the requirements of the General Data Protection Regulation (GDPR). Any data submitted to the archive is subject to controlled access, which means that access to the data only will be granted after a formal application procedure. The Swedish node is close, but not yet in a production stage. In the meantime we suggest to keep the human sequencing data stored locally and make a metadata-only record in the SciLifeLab Data Repository. Once the Swedish EGA node is operational, and the dataset deposited there, the access information can be changed to point at the EGA ID. See https://doi.org/10.17044/scilifelab.12292778.v1, for an example.

### SciLifeLab Data Repository
The SciLifeLab Data Repository offers a possibility to publish a metadata record. This allows for publishing metadata about human data without actually publishing the human data itself. More information regarding accounts and submission can be found [here](https://www.scilifelab.se/data/repository). When creating a metadata record choose the license “Restricted access” and add an email to the metadata field "access request email”. It is important to not upload the human data, but do provide as much descriptive metadata as possible to improve the findability.

## How can SciLifeLab help you to publish your human data?

**Who can get help?** If you are a researcher at a Swedish academic institution working in SciLifeLab’s areas of activity, you can get help from SciLifeLab Data Management support team.

**What kind of data publishing can we support?** If your data is located on the Bianca server at UPPMAX (or in the future at FEGA Sweden), we can help with the publishing and access requests! If your data is located in your own safe environment, we can not help with the handling of access requests but the to-do steps listed below are still valid.

Until FEGA Sweden is ready for both storing and sharing data, currently data can only be shared with PIs that can get a project account set up on Bianca.

This is what you need to do:
1. Adjust the Data Access Agreement and Data Access request forms (available from datacentre@scilifelab.se) to suit your particular case.
2. Store your data in your own project account on Bianca at UPPMAX.
3. Prepare a metadata record for the dataset in the SciLifeLab Data Repository. Set datacentre@scilifelab.se as “access request email” and your own email address as “contact email”.
4. In the manuscript add a section on Data Availability and make sure it includes information on where to go for requesting access to the data. The section in the manuscript can include eg. : “The data is deposited on a secure Swedish server and has been assigned a DOI (XXX). Data access requests may be submitted to the Science for Life Laboratory Data Centre through the DOI link.”
5. When a user applies for access to datacentre@scilifelab.se, the application will be vetted and you will be contacted by us. Then you can make a decision on access approved or denied. Ideally, you can (should) delegate this decision to an independent Data Access Committee (DAC).
6. When a user has been approved for access, Data Centre will document the processing and arrange for the physical file access. Until FEGA Sweden is up and running, the physical file access will be that you, as a PI, copies the dataset from your Bianca project space, to the specified project space of the approved applicant. Because of SNIC user policy, only PIs at a Swedish academic institution can have a project at Bianca. So to share data with a collaborator outside Sweden, the PI in Sweden needs to have applied for a project at Bianca. Please see [here](https://www.uppmax.uu.se/support/user-guides/bianca-user-guide/) for information on how to do this.
7. Data Centre will keep track of current and expired approvals.



## Resources & Training
* [RDMkit on Human data](https://rdmkit.elixir-europe.org/human_data)
