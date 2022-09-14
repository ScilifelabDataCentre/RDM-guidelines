---
title: Sensitive data
toc: True
---

## Sensitive personal data

The following is a list of Ethical, Legal and Social Implications (ELSI) that should be considered when working with human data.
The content on this page is based on a checklist that has been developed in the [Tryggve project](https://neic.no/tryggve/). It is intended be used as a tool to document these considerations, and is available as:
1. An MS Word file that can be downloaded from the [Tryggve project pages](https://neic.no/tryggve/links/).
2. In the [SciLifeLab Data Stewardship Wizard](https://dsw.scilifelab.se/) (SciLifeLab DSW)
  * Log in to the [SciLifeLab DSW](https://dsw.scilifelab.se/) using your university credentials
  * Select Projects in the left sidebar, and click the Create button
  * Choose *ELSI Checklist Template* from the list of project templates

*Note that the checklist was created with cross-border collaborative projects in mind, but it should be useful for other research projects as well.*

Before the collection of personal data has begun you should always consult with the [Data Protection Officer](data-protection-officer) of your organisation.

### Ethical reviews and informed consent ([more info](#ethical-reviews-and-informed-consents))

* Has the project (or parts of the project) undergone ethical review?
* Have informed consents been collected from the research subjects?
* Are there limitations of use defined in these?
* Is the intended research purpose within the scope of the limitations of use that is defined in the ethics approval(s) and/or the informed consent(s)?


### GDPR ([more info](#gdpr))

* What is the **purpose** of processing of the personal data?
* Who is the **Controller(s)** of the personal data?
* What is the **legal basis** processing of the personal data?
* What are the **exemptions for the prohibition for processing of special categories of data** (such as health and genetic data) under Art. 9 GDPR used?
* Have **data processing agreements** been established between the data controller(s) and any data processors?
* Has a **Data Protection Impact Assessments (DPIA)** been performed for the personal data?
* What happens with the data after project completion?
* What technical and procedural safeguards will be established for processing the data?

### Other considerations ([more info](#other-considerations))

* Are there other relevant national legislation considerations that has to be taken into account?
  - e.g. regarding public access to information, biobank acts, etc.
* Are there other Terms & conditions for data access (in particular if presenting  obstacles for cross-border processing of health data)?
  - e.g. register data access policies
* Are there other legal agreements between project parties that should be considered?
  - e.g. conditions regarding data reuse and intellectual property

---

### Clarifications and comments

#### Ethical reviews and informed consents
The purpose of these questions is to spell out what uses the subjects have consented to, and/or for what uses ethical approvals have been given. Then, given the stated research purpose of this project, are the consents and ethical approvals for the datasets compatible with this.

#### GDPR

##### State the purpose of processing the personal data
The GDPR stipulates that to process personal data the controller must do that with stated purposes, and not further process the data in a manner that is incompatible with those purposes ([Article 5 - Principles relating to processing of personal data](https://gdpr-info.eu/art-5-gdpr/)).

##### Who are the data controller of the personal data processed in the project?
[Article 4](https://gdpr-info.eu/art-4-gdpr/) (7): _“‘**controller**’ means the natural or legal person, public authority, agency or other body which, alone or jointly with others, **determines the purposes** and means of the processing of personal data; […].”_ The Controller is typically the university employer of the PI, and the PI should act as a representative of her university employer and is responsible for ensuring that personal data is handled correctly in her projects. If the project involves more than one legal entity, and joint controllership is considered, make sure that all parties understand their obligations, and it is probably good to define the terms for this in an agreement between the parties.

##### What is the legal basis for processing the personal data?
[Article 6](https://gdpr-info.eu/art-6-gdpr/) (1) lists under what conditions the processing is considered lawful. Of these, **Consent** or **Public interest** are relevant when it comes to research. You should determine what legal basis (or bases) you have for processing the personal data in your project.  

Traditionally, _consent_ has been the basis for processing personal data for research, but under the GDPR there cannot be an imbalance between the processor and the data subject for it to be considered to be freely given. In some countries the use of consent as the legal basis for processing by universities for research purposes is therefore not recommended. In those cases, public interest should probably be your legal basis. Note that if your legal basis for processing is consent, a [number of requirements](https://gdpr-info.eu/issues/consent/) exists for the consent to be considered valid under the GDPR. Consents given before the GDPR might not live up to this.  

Also note that even if _public interest_ is the legal basis, other laws and research ethics standards might still require you to have consent from the subjects for performing the research.  

Please consult with the [Data Protection Officer](data-protection-officer) of your organisation on which legal basis to apply to your data.

##### What are the exemptions for the prohibition for processing of special categories of data (such as health and genetic data) under Art. 9 GDPR used?
Processing of certain categories of personal data is not allowed unless there are exemptions in law to allow this. Among these categories (“sensitive data”) are _“‘[...] data revealing racial or ethnic origin, [...] genetic data, [...] data concerning health’”_. Most types of personal data collected in biomedical research will fall under these categories. [Article 9](https://gdpr-info.eu/art-9-gdpr/) (2) lists a number of exemptions that apply, of which consent and scientific research are most likely to be relevant for research. Please consult with your [Data Protection Officer](data-protection-officer) of your organisation.

##### Have data processing agreements been established between the data controller(s) and any data processors?
[Article 4](https://gdpr-info.eu/art-4-gdpr/) (8): _“‘processor’ means a natural or legal person, public authority, agency or other body which processes personal data on behalf of the controller.”_ Examples of this is if you use a secure computing environment provided by another organisation to do your analysis or to store the data, along with several other scenarios. In the case that you do, there needs to be a legal agreement established between the controller(s) and processor(s) as defined in [Article 28](https://gdpr-info.eu/art-28-gdpr/) (3): _“Processing by a processor shall be governed by a contract or other legal act under Union or Member State law, that is binding on the processor with regard to the controller and that sets out the subject-matter and duration of the processing, the nature and purpose of the processing, the type of personal data and categories of data subjects and the obligations and rights of the controller. […]”_ Article 28 also lists the required contents of such an agreement. [Your organisation](data-protection-officer) and/or the processor organisation will probably have agreement templates that you can use.

##### Have Data Protection Impact Assessments (DPIA) been performed for the personal data?
Where a type of processing is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall, prior to the processing, carry out an assessment of the impact of the envisaged processing operations on the protection of personal data, a so called _Data Protection Impact Assessment_ (DPIA) - [Article 35](https://gdpr-info.eu/art-35-gdpr/). To clarify when this is necessary, the Swedish Data Protection Authority (DPA) "Datainspektionen" has issued [guidance](https://www.datainspektionen.se/globalassets/dokument/beslut/list-regarding-data-protection-impact-assessments.pdf) of when an impact assessment is required. Large-scale processing of sensitive data such as genetic or other health related data is listed as requiring DPIAs. The French DPA has made a [PIA tool](https://www.cnil.fr/en/open-source-pia-software-helps-carry-out-data-protection-impact-assesment) (endorsed by several other DPAs) available that can help in performing these impact assessments. Please also consult your [Data Protection Officer](data-protection-officer) of your organisation.

##### What technical and procedural safeguards have been established for processing the data?
To ensure that the personal data that you process in the project is protected at an appropriate level, you should apply technical and procedural safeguards to ensure that the rights of the data subjects are not violated. Examples of such measures include, but are not limited to, pseudonymisation end encryption of data, the use of computing and storage environments with heightened security, and clear and documented procedures for project members to follow.

##### What happens with the data after project completion?
The GDPR states that the processing (including storing) of personal data should stop when the intended purpose of the processing is done. There are, however, exemptions to this e.g. when the processing is done for research purposes. Also, from a research ethics point of view, research data should be kept to make it possible for others to validate published research findings and reuse data for new discoveries. This is also governed by what the data subjects have been informed about regarding how you will treat the data after project completion. The recommendation is to deposit the sensitive data in the appropriate controlled access repositories if such are available, but this requires that the data subjects are informed and have agreed to this.

#### Other considerations
There might also exist other national legal or procedural considerations for cross-border research collaborations. Other laws might affect how and if data can or cannot be made available outside the country of origin. The operating procedures of government authorities or other organisations might create obstacles for sharing data across borders. To make sure that it is clear how original and derived data, as well as results, can be used by the parties after the project completion, consider establishing legal agreements that defines this. This can include e.g. reuse of data for other projects or intellectual property rights derived from the research project.
