---
title: Research involving human data
contributors: []
toc: True
---

# Research involving human data

<div class="alert alert-warning" role="alert">
  <B><I>Disclaimer!</I></B> The PI, as well as everyone with access to sensitive personal data, is responsible for following current laws and regulations, and SciLifeLab will not assume legal responsibility for advice provided in these guidelines.
</div>

Research that involves humans or biological samples from humans should take ethical, legal and societal implications (ELSI) into account. This is true also when research involves data about humans. It is important to consider all the different aspects early in a research project, as the consequences of not doing so may be severe.

When planning a research project, it is often useful to think of ELSI with respect to the different stages in the data life cycle. For example: what laws do I need to follow during the data collection phase? Or, how can I maximise data reuse without compromising the personal integrity of data subjects? What concerns you need to address depend on your research questions and the type of data you want to collect (for example if you have personal data or not).


## What is personal data?

Any data that directly or indirectly can be linked to a living person is considered personal data under the General Data Protection Regulation (GDPR). This can for example be a person's name or personal identity number. Different pieces of information, which collected together can lead to the identification of a particular person, is also regarded as personal data. For instance can a street address in combination with a person's gender in some cases be sufficient to identify a particular person. Read more in the [legal reference regarding personal data](/topics/gdpr-legal-reference/#personal-data).


## What is sensitive personal data?

Some personal data is regarded as [sensitive](https://ec.europa.eu/info/law/law-topic/data-protection/reform/rules-business-and-organisations/legal-grounds-processing-data/sensitive-data/what-personal-data-considered-sensitive_en), for example data related to health and genetics. This includes **all kinds of genetic data** (both RNA and DNA, and both somatic and germline information), and is likely to apply to  other kinds of omics data as well. One should keep in mind that genetic data about a deceased person also may be regarded as personal data under GDPR if the data can be used to identify a living relative of that person.

Aggregated data (like population frequencies or number of sequence reads for a gene) might not be considered personal data (and hence not sensitive personal data), but a decision has to be made on a case-by-case basis.

Sensitive personal data should always be [pseudonymised](/topics/gdpr-legal-reference/#pseudonymisation), which means that a particular person cannot be identified from the data unless it is combined with other data that has not been disclosed to the public. A common pseudonymisation procedure is to replace personal identity numbers with artificial identifiers. It is important to remember that pseudonymised data is still regarded as personal data under GDPR. See also legal reference regarding [sensitive data](/topics/gdpr-legal-reference#sensitive-data)


## Important regulations to follow

Below we list some important regulations to follow when conducting research that involves human data.

* **General Data Protection Regulation (GDPR)** – All research involving personal data must comply with the [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/).
The [Swedish Authority for Privacy Protection (IMY)](https://www.imy.se/en/) upholds the protection of personal data, monitors that they are handled correctly and do not fall into the wrong hands. See also [GDPR considerations](#gdpr-considerations) further below.

* **The Ethical Review Act** – Ethical review by the [Ethical Review Authority](https://etikprovningsmyndigheten.se/) is needed when research involves human data, according to the Swedish ethical review act ([Lag (2003:460) om etikprövning av forskning som avser människor](https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-2003460-om-etikprovning-av-forskning-som_sfs-2003-460) - *Swedish*). See also [Ethical considerations](#ethical-considerations) below.

* **Other regulations**
  * [The Patient Data Act](https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/patientdatalag-2008355_sfs-2008-355)
  * [The Biobank Act](https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-2002297-om-biobanker-i-halso--och_sfs-2002-297)


## Who is responsible for the data?

An important concept in GDPR is the [data controller](/topics/gdpr-legal-reference/#controller), which is the person or entity that determines the purposes and means of the processing of some personal data.

Many people wrongly believe that the principal investigator in a research project is the controller for the project's data. In fact, this is practically never the case for Swedish academic research. Instead, the controller is typically the university (or sometimes the hospital) where the principal investigator is employed. That being said, the principal investigator should act as a representative of her institution and is responsible for ensuring that personal data is handled correctly in her projects.

The data controller must be identified before any personal data is processed in the project, which means before the data is being collected.


## Sharing human data

Data that cannot be used to identify a living person can normally be shared publicly. However, one must first be sure that the data is truly anonymous. This can be a difficult endeavour, especially if the research involves genetic data. When dealing with human data in a project, it is crucial to document every decision that is being made regarding the data in relation to GDPR.

Personal data may be possible to share under some circumstances. Make sure to follow GDPR, the ethical review act and other relevant regulations. See further information below regarding considerations.

The GDPR states that the processing (including storing) of personal data should stop when the intended purpose of the processing has been fullfilled. There are, however, exemptions to this e.g. when the processing is done for research purposes. Also, from a research ethics point of view, research data should be kept to make it possible for others to validate published findings and reuse data for new discoveries. This is also governed by what the data subjects have been informed about regarding the data procesing.

<a href="/topics/sharing-human-data"><b>See more guidelines on sharing human data <i class="bi bi-arrow-right-square-fill"></i></b></a>
<br/><br/>

<!-- Data processing agreement, data transfer agreement, data access agreement -->


## GDPR considerations

<!-- Merge content of "PIs working with human data" and “Sensitive personal data”
Risk assessment, DPIA … -->
Before embarking on a new project, consider the following:
* Have the data processing been reported to the [data protection officer](#data-protection-officer-dataskyddsombud)?
* What is the purpose of processing the personal data?
* Who is the data controller of the personal data processed in the project?
* What is the [legal basis](#legal-basis-for-processing-personal-data) for processing the personal data?
* Have [data processing agreements](#data-processing) been established between the data controller(s) and any data processors?
* Have Data Protection Impact Assessments ([DPIA](#data-protection-impact-assessment-dpia)) been performed for the personal data?
* What technical and procedural [safeguards](#security-of-processing) have been established for processing the data?
* What happens with the data [after project completion](#repositories-for-publishing-human-data)?


### Data Protection Officer (dataskyddsombud)

The role of the data protection officer is to check that the General Data Protection Regulation (GDPR) is complied with within the organisation. If personal data is processed in your research, you should report this to your institute’s [Data Protection Officer (DPO)](/topics/university-rdm-resources#data-protection-officers).


### Legal basis for processing personal data

[Article 6 (1)](https://gdpr-info.eu/art-6-gdpr/) lists under what conditions the processing is considered lawful. Of these, **Consent** or **Public interest** are relevant when it comes to research. You should determine what legal basis (or bases) you have for processing the personal data in your project.

Traditionally, consent has been the basis for processing personal data for research, but under the GDPR there cannot be an imbalance between the processor and the data subject for it to be considered to be freely given. In Sweden the use of consent as the legal basis for processing by universities for research purposes is therefore not recommended. Instead, public interest should probably be your legal basis. Note that if your legal basis for processing is consent, a [number of requirements](https://gdpr-info.eu/issues/consent/) exists for the consent to be considered valid under the GDPR. Consents given before the GDPR might not live up to this.

Also note that even if public interest is the legal basis, other laws and research ethics standards might still require you to have consent from the subjects for performing the research.


### Data Processing

<!-- what is meant / definition; storage & analysis by other than the controller requires agreement -->
All processing of personal data must comply with the [Principles relating to processing of personal data](/topics/gdpr-legal-reference/#principles-of-processing-of-personal-data) in the GDPR.


#### Agreements

<!-- Data processing agreement, data transfer agreement, data access agreement -->
* A Data Processing Agreement is needed when a Processor (someone from a different university than the controller) is processing the data (e.g. storing or analysing) on behalf of the Controller.
<!-- * A Data Transfer Agreement is needed when... -->
<!-- * A Data Access Agreement is needed when... -->


#### Responsibilities <!-- controller versus processor -->

As a Controller you should:
* Ensure that data processing agreements are established when needed.
* Ensure that all Processors are informed on what can and cannot be done to the data.
* Ensure that all processing is done in a compute environment with a suitable level of security, e.g. [Bianca at Uppmax](http://www.uppmax.uu.se/support/user-guides/bianca-user-guide/).

As a Processor you should:
* Only handle the data according to the instructions from the Controller.
* In the case of a [data breach](/topics/gdpr-legal-reference/#data-breach), accidental or otherwise, immediatly report the incident to the Controller.


### Data Protection Impact Assessment (DPIA)

A Data Protection Impact Assessment (DPIA) is needed if the personal data processing is likely to result in a high risk to individual people's rights ([IMY on Impact assessments and prior consultation](https://www.imy.se/en/organisations/data-protection/this-applies-accordning-to-gdpr/impact-assessments-and-prior-consultation/)). The purpose of a DPIA is to prevent risks before they occur, by identifying what risks exist and draw up procedures to meet those risks. In order be able to decide if a DPIA is needed, you should perform a risk analysis. Analyse what risks your personal data processing may involve and suggest appropriate security measures. Document your findings so that you can demonstrate that you comply with the GDPR. If the risk analysis shows that a DPIA is needed, there are tools to help you e.g. [PIA software from CNIL](https://www.cnil.fr/en/open-source-pia-software-helps-carry-out-data-protection-impact-assessment).


### Security of processing

To ensure that the personal data that you process in the project is protected at an appropriate level, you should apply [technical and procedural safeguards](/topics/gdpr-legal-reference/#security-of-processing) to ensure that the rights of the data subjects are not violated. Examples of such measures include, but are not limited to, pseudonymisation and encryption of data, the use of computing and storage environments with heightened security, and clear and documented procedures for project members to follow.


## Ethical considerations

<!-- Ethical review and informed consent
Merge content of "PIs working with human data" and “Sensitive personal data” -->
Before embarking on a new project, consider the following:
* Has the project (or parts of the project) undergone ethical review?
* Have informed consents been collected from the research subjects?
* Are there limitations of use defined in these?
* Is the intended research purpose within the scope of the limitations of use that is defined in the ethics approval(s) and/or the informed consent(s)?

The purpose of these questions is to spell out what uses the subjects have consented to, and/or for what uses ethical approvals have been given. Then, given the stated research purpose of this project, are the consents and ethical approvals for the datasets compatible with this.
<!--  enable others to reuse your data by specifying in the application how the data is going to be shared -->
<!-- From https://fega.nbis.se/submission/ethical-approval.html, do we include part and link out? #### Informed consent
Depending on what kind of research you are doing, you may be required to collect consent agreements from the research participants. This means that the participants—before they consent to participate—must be informed about the purpose of the research, as well as about any risks and benefits involved in their participation. The information that you plan to give to the participants should be attached to your ethical review application. The [Ethical Review Act](https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-2003460-om-etikprovning-av-forskning-som_sfs-2003-460) specifies when consent agreements are required.

When you prepare the information for the participants, it might be a good to think of the following:

* Express clearly that the participant’s personal data may be used in other research projects. Try to define the data reuse conditions by specifying a research purpose rather than by stating with whom the data can be shared. In particular, do not limit the data access to only researchers, since researchers sometimes need help from non-researchers (e.g. technical staff) with the data.
* Consider which countries the data can be shared with. Can it be shared only within EU/EES? Or perhaps only within Sweden?
* Personal data must normally be pseudonymised before it is shared. Don’t forget to inform the participants about that. Data that is pseudonymised can only be used to identify individuals in combination with other data. -->
<!-- ### Other considerations -->


## Resources

<!-- Link to other resources about human data in research -->
* [RDMkit on Human data](https://rdmkit.elixir-europe.org/human_data)
* Swedish National Data service (SND) on [Research material with personal data](https://snd.gu.se/en/manage-data/plan/research-material-with-personal-data)
* Consider using the Ethical, Legal and Social Implications (ELSI) checklist developed by the [Tryggve project](https://neic.no/tryggve/). It was developed with cross-border collaborative projects in mind, but it should be useful for other research projects as well. It is available as a [MS Word file](https://neic.no/tryggve/files/Tryggve_ELSI_checklist_v1.0_2019-12-17.docx) and in the [SciLifeLab Data Stewardship Wizard](https://dsw.scilifelab.se/):
  1. Log in using your university credentials
  1. Click on Projects in the left sidebar, and click the Create button
  1. Choose *ELSI Checklist Template*
