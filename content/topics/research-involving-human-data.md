---
title: Research involving human data
contributors: []
toc: True
---

# Research involving human data

<div class="alert alert-warning" role="alert">
  <B><I>Disclaimer!</I></B> The PI, as well as everyone with access to sensitive personal data, is responsible for following current laws and regulations, and SciLifeLab will not assume legal responsibility for advice provided in these guidelines.
</div>


<!-- >***Disclaimer!** The PI, as well as everyone with access to sensitive personal data, is responsible for following current laws and regulations, and SciLifeLab will not assume legal responsibility for advice provided in these guidelines.* <!-- probably need a bit more disclaimer text -->

## What is human data?
Any data that directly or indirectly can be associated with a living person is considered personal data, e.g. name, address and personal identity number. See also legal reference regarding [personal data](/topics/gdpr-legal-reference/#personal-data).

## What is sensitive human data?
Some personal data are regarded as [sensitive](https://ec.europa.eu/info/law/law-topic/data-protection/reform/rules-business-and-organisations/legal-grounds-processing-data/sensitive-data/what-personal-data-considered-sensitive_en), e.g. data related to health and genetic data. This explicitly includes **all genetic data** (both RNA and DNA, and both somatic and germline information), and is likely to also apply to  other kinds of omics data. Aggregated data (like population frequencies) might not be considered sensitive anymore, but a decision has to be made on a case-to-case basis. Personal data should always be [pseudonymised](/topics/gdpr-legal-reference/#pseudonymisation), but the data will still remain sensitive in legal terms. See also legal reference regarding [sensitive data](/topics/gdpr-legal-reference#sensitive-data).

## Important regulations to follow
Please find below an overview of relevant regulations to follow when doing research involving human data.

* **General Data Protection Regulation (GDPR)** – All research involving personal data must comply with the [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/).
The [Swedish Authority for Privacy Protection (IMY)](https://www.imy.se/en/) upholds the protection of personal data, monitors that they are handled correctly and do not fall into the wrong hands. See also [GDPR considerations](#gdpr-considerations) further below.

* **The Ethical Review Act** – Ethical review by the [Ethical Review Authority](https://etikprovningsmyndigheten.se/) is needed when research involves human data, according to the Swedish ethical review act ([Lag (2003:460) om etikprövning av forskning som avser människor](https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-2003460-om-etikprovning-av-forskning-som_sfs-2003-460) - *Swedish*). See also [Ethical considerations](#ethical-considerations) further below.

* **Other regulations**
  * [The Patient Data Act](https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/patientdatalag-2008355_sfs-2008-355)
  * [The Biobank Act](https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-2002297-om-biobanker-i-halso--och_sfs-2002-297)

## Who is responsible for the data?
The person who decides how and why the personal data should be processed is responsible for ensuring that the processing is done according to the law. That person is called the [Controller](/topics/gdpr-legal-reference/#controller) (of personal data). The Controller is typically the university employer of the principal investigator (PI). The PI should act as a representative of her university employer and is responsible for ensuring that personal data is handled correctly in her projects.


## Sharing and publishing human data
Anonymised data can be shared publicly, but you have to first be sure that the data is truly anonymous which can be hard, especially if you are working with genetic data. <!-- need to add info on what anonymous means, I can't find an official definition -->

Personal data may be allowed to be shared under some circumstances. Make sure to follow GDPR, the ethical review act and other relevant regulations, see further information below regarding [considerations](#considerations-when-working-with-human-data).

The GDPR states that the processing (including storing) of personal data should stop when the intended purpose of the processing is done. There are, however, exemptions to this e.g. when the processing is done for research purposes. Also, from a research ethics point of view, research data should be kept to make it possible for others to validate published findings and reuse data for new discoveries. This is also governed by what the data subjects have been informed about regarding how you will treat the data after project completion. The recommendation is to deposit the sensitive data in the appropriate controlled access repositories if such are available, but this requires that the data subjects are informed and have agreed to this.

<a href="/topics/publishing-human-data"><b>See more guidelines on publishing human data <i class="bi bi-arrow-right-square-fill"></i></b></a>
<br/><br/>

<!-- Data processing agreement, data transfer agreement, data access agreement -->

## Considerations when working with human data

### GDPR considerations
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

#### Data Protection Officer (dataskyddsombud)

The role of the data protection officer is to check that the General Data Protection Regulation (GDPR) is complied with within the organisation. If personal data is processed in your research, you should report this to your institute’s [Data Protection Officer (DPO)](/topics/university-rdm-resources#data-protection-officers).

#### Legal basis for processing personal data
[Article 6 (1)](https://gdpr-info.eu/art-6-gdpr/) lists under what conditions the processing is considered lawful. Of these, **Consent** or **Public interest** are relevant when it comes to research. You should determine what legal basis (or bases) you have for processing the personal data in your project.

Traditionally, consent has been the basis for processing personal data for research, but under the GDPR there cannot be an imbalance between the processor and the data subject for it to be considered to be freely given. In Sweden the use of consent as the legal basis for processing by universities for research purposes is therefore not recommended. Instead, public interest should probably be your legal basis. Note that if your legal basis for processing is consent, a [number of requirements](https://gdpr-info.eu/issues/consent/) exists for the consent to be considered valid under the GDPR. Consents given before the GDPR might not live up to this.

Also note that even if public interest is the legal basis, other laws and research ethics standards might still require you to have consent from the subjects for performing the research.

#### Data Processing
<!-- what is meant / definition; storage & analysis by other than the controller requires agreement -->
All processing of personal data must comply with the [Principles relating to processing of personal data](/topics/gdpr-legal-reference/#principles-of-processing-of-personal-data) in the GDPR.

##### Agreements
<!-- Data processing agreement, data transfer agreement, data access agreement -->
* A Data Processing Agreement is needed when a Processor (someone from a different university than the controller) is processing the data (e.g. storing or analysing) on behalf of the Controller.
<!-- * A Data Transfer Agreement is needed when... -->
<!-- * A Data Access Agreement is needed when... -->

##### Responsibilities <!-- controller versus processor -->
As a Controller you should:
* Ensure that data processing agreements are established when needed.
* Ensure that all Processors are informed on what can and cannot be done to the data.
* Ensure that all processing is done in a compute environment with a suitable level of security, e.g. [Bianca at Uppmax](http://www.uppmax.uu.se/support/user-guides/bianca-user-guide/).

As a Processor you should:
* Only handle the data according to the instructions from the Controller.
* In the case of a [data breach](/topics/gdpr-legal-reference/#data-breach), accidental or otherwise, immediatly report the incident to the Controller.

#### Data Protection Impact Assessment (DPIA)
A Data Protection Impact Assessment (DPIA) is needed if the personal data processing is likely to result in a high risk to individual people's rights ([IMY on Impact assessments and prior consultation](https://www.imy.se/en/organisations/data-protection/this-applies-accordning-to-gdpr/impact-assessments-and-prior-consultation/)). The purpose of a DPIA is to prevent risks before they occur, by identifying what risks exist and draw up procedures to meet those risks. In order be able to decide if a DPIA is needed, you should perform a risk analysis. Analyse what risks your personal data processing may involve and suggest appropriate security measures. Document your findings so that you can demonstrate that you comply with the GDPR. If the risk analysis shows that a DPIA is needed, there are tools to help you e.g. [PIA software from CNIL](https://www.cnil.fr/en/open-source-pia-software-helps-carry-out-data-protection-impact-assessment).

#### Security of processing
To ensure that the personal data that you process in the project is protected at an appropriate level, you should apply [technical and procedural safeguards](/topics/gdpr-legal-reference/#security-of-processing) to ensure that the rights of the data subjects are not violated. Examples of such measures include, but are not limited to, pseudonymisation and encryption of data, the use of computing and storage environments with heightened security, and clear and documented procedures for project members to follow.

### Ethical considerations
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

## Resources & Training
<!-- Link to other resources about human data in research -->
* [RDMkit on Human data](https://rdmkit.elixir-europe.org/human_data)
* Swedish National Data service (SND) on [Research material with personal data](https://snd.gu.se/en/manage-data/plan/research-material-with-personal-data)
* Consider using the Ethical, Legal and Social Implications (ELSI) checklist developed by the [Tryggve project](https://neic.no/tryggve/). It was developed with cross-border collaborative projects in mind, but it should be useful for other research projects as well. It is available as a [MS Word file](https://neic.no/tryggve/files/Tryggve_ELSI_checklist_v1.0_2019-12-17.docx) and in the [SciLifeLab Data Stewardship Wizard](https://dsw.scilifelab.se/):
  1. Log in using your university credentials
  1. Click on Projects in the left sidebar, and click the Create button
  1. Choose *ELSI Checklist Template*
