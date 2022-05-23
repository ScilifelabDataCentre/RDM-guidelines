# PIs - working with human data

***Disclaimer!**  The PI, as well as everyone with access to sensitive personal data, is responsible for following current laws and regulations, and NBIS will not assume legal responsibility for advice provided in these guidelines.*

## Human data - What you should as a PI
* Be aware of that if your project contains human derived biomedical data, it is most probably ‘[sensitive data](#what-is-sensitive-personal-data)’.
* Be aware of that [you](#who-is-responsible-for-the-data) (as an employee of your institute) must ensure that the GDPR (and other laws) are followed.
* Be able to demonstrate that you follow the GDPR (see [human data legal reference page for more info](./human-data-legal.md)). E.g. define the purpose for processing the data, decide on the legal basis, protect the data, etc
* In case you work at a different institute than Uppsala University, ensure that there is a data processing agreement between your institute and Uppsala University. This is the legal instruction from you as the representative of the Controller to NBIS in the role of Processor. [General processing agreements](./general-processing-agreements.md) have been established with some Swedish universities, and more are on their way.
* Inform the NBIS bioinformaticians about the conditions for what can and cannot be done to the data according to [ethical permit(s) and informed consent text(s)](#ethical-permits-and-informed-consents).
* Define the procedures for how the personal data should be handled in the project, and communicate these to all involved, including NBIS bioinformaticians.
* [Make the data available to the NBIS bioinformatician](#how-do-nbis-bioinformaticians-access-and-analyse-sensitive-personal-data) in a compute environment with a suitable level of security, which is typically the Bianca system at UPPMAX. If necessary, decide and approve alternative compute solutions outside of Bianca for NBIS bioinformaticians to use. Note that working with sensitive data outside of Bianca is highly discouraged, the motivation for which should be documented! In case you work at a different institute than Uppsala University, you need a data processing agreement between your institute and UPPMAX/Uppsala University for using the Bianca system - see [instructions](https://www.uppmax.uu.se/support/faq/general-miscellaneous-faq/sensitive+data+questions/) at UPPMAX.
* Data made available to the NBIS bioinformatician **must** be pseudonymised. No directly identifiable information about the research subjects can be included in the data and metadata.
* It is advisable that you have a strategy regarding if and how so called ‘[secondary findings](https://pubmed.ncbi.nlm.nih.gov/25150271/)’ should be acted on vis-a-vis the research subjects.
* Deposit the data in a [controlled access repository](#how-do-i-publish-sensitive-personal-data), during (preferably) or after the project.

Also consider going through this [Ethical, Legal and Social implications (ELSI) checklist](./sensitive-data.md) for your project.

You are welcome to contact the NBIS data manager for further consultation (<data@nbis.se>). Also, do consult with the [Data Protection Officer](./data-protection-officer.md) (“Dataskyddsombud”) of your employer.

## More information
### What is sensitive personal data
* Any data that directly or indirectly can be associated with a living person is considered personal data.
* Some personal data are regarded as [sensitive](https://ec.europa.eu/info/law/law-topic/data-protection/reform/rules-business-and-organisations/legal-grounds-processing-data/sensitive-data/what-personal-data-considered-sensitive_en), e.g. data related to health and genetic data. This explicitly includes **all genetic data** (both RNA and DNA, and both somatic and germline information), and is likely to also apply to many other omics data.
* Personal data should always be pseudonymised, but the data will still remain sensitive in legal terms.
* Aggregated data (like population frequencies) might not be considered sensitive anymore, but a decision has to be made on a case-to-case basis.

### Who is responsible for the data
* The person who decides how and why the personal data should be processed is responsible for ensuring that the processing is done according to the law. That person is called the *Controller* (of personal data). The Controller is typically the university employer of the PI, and the PI should act as a representative of her university employer and is responsible for ensuring that personal data is handled correctly in her projects.

### Ethical permits and Informed consents
* Before the start of a support project, the PI must share the ethical permit(s) and informed consent text(s) for the study with the NBIS bioinformatician. The PI is also responsible for clearly explaining to the NBIS bioinformatician the conditions for what can and cannot be done to the data according to the above documents.
* Note that the ethical permits and the consent forms must cover *all the datasets* made readable to the NBIS bioinformatician (e.g. all the datasets stored in a granted Bianca project, see below).

> *Tip! Ask the PI to add the ethical permit(s) and informed consent texts to the project catalog on Bianca, preferably also with a short summary of the limitations/boundaries of use of the data. The NBIS data manager (<data@nbis.se>) can help the PI write this summary.*

### How do NBIS bioinformaticians access and analyse sensitive personal data
* Large-scale sensitive personal data can be analysed at the national computer cluster specifically dedicated to sensitive personal data, [Bianca](http://www.uppmax.uu.se/support/user-guides/bianca-user-guide/). If an NBIS bioinformatician plans to analyse sensitive personal data elsewhere, we suggest that they first consult with the NBIS data manager (<data@nbis.se>), as well as inform and get approval from the PI on how they plan to process the personal data outside Bianca. *Note that working with sensitive data outside of Bianca is highly discouraged, and needs a strong documented motivation!*
* The PI of the study formally grants access to the data by adding the NBIS bioinformatician to the relevant Bianca project in Supr (<https://supr.snic.se>).
* Findings outside the scope of the study (secondary findings) will never be looked for by the NBIS bioinformatician, and will always be reported to the PI if accidentally found. It is advisable that the PI has a strategy regarding if and how such information should be acted on vis-a-vis the research subjects.

### How do I publish sensitive personal data
We are working on a federated version of the European Genome-phenome Archive ([EGA](https://ega-archive.org/)) in Sweden (EGA-SE), where sensitive human genomic and phenotypic data can be stored locally in e.g. Sweden, and the metadata stored centrally at EGA to make the data discoverable. The Swedish node is close, but not yet in a production stage (hopefully later this year). In the meantime we suggest to keep the human sequencing data stored locally, and make a metadata-only record in the [SciLifeLab Data Repository](https://www.scilifelab.se/data/repository) with contact details on how to get access, and for which a DOI can be issued. The DOI can then be used in the article to refer to the dataset. Once the Swedish EGA node is operational, and the dataset deposited there, the access information can be changed to point at the EGA ID. See <https://doi.org/10.17044/scilifelab.12292778>, for an example.

## References
### GDPR
* [Dataskyddsförordningen](https://www.imy.se/verksamhet/dataskydd/det-har-galler-enligt-gdpr/introduktion-till-gdpr/dataskyddsforordningen-i-fulltext/) - *Swedish*
* [General Data Protection Regulation](https://gdpr-info.eu/) - *English*

## Information about the GDPR
* The Swedish Data Protection Authority (*Datainspektionen*) [GDPR information pages](https://www.imy.se/verksamhet/dataskydd/det-har-galler-enligt-gdpr/introduktion-till-gdpr/) - *Swedish*
* European Commission [Data Protection information pages](https://ec.europa.eu/info/law/law-topic/data-protection/reform_en) - *English*

## Further questions
If you have further questions regarding sensitive personal data, you are welcome to contact the NBIS data manager (<data@nbis.se>).