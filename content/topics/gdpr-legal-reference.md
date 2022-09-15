---
title: GDPR - legal reference
toc: True
---

# Legal reference - General Data Protection Regulation (GDPR)
>This section is an attempt to describe the reasoning behind the [guidelines regarding working with human data](/topics/research-involving-human-data) in more detail by referring to relevant sections of the **General Data Protection Regulation (GDPR)**, the EU-wide legislation that stipulates how personal data should be handled.
>
>Note that this information is our understanding of the legislation, and does not constitute legal advice in individal cases. Please consult the legal office of your university if you need assistance.

The entity who decides on why and how personal data should be processed is called [Controller](#controller). In an academic research context, this is the university that employs the PI(s) responsible for the research project. All employees of a university are obliged to process personal data according to the GDPR.

A Controller can decide to use another entity to help process the data. That entity is called a [Processor](#processor). The Controller must instruct the Processor how the data is to be processed in a legaly binding [contract](#contract-controller-processor), and the Processor must be able to show that they adhere to the GDPR when processing data on behalf of the Controller.

Human DNA or RNA sequence data is [sensitive personal data](#sensitive-data), as it is [genetic data](#genetic-data). This is probably to be considered true in most cases even if the sequence data is not accompanied with any other data, as it will be a factor “specific to the […] genetic […] identity of that natural person” ([Article 4 (1)](#personal-data)). <!-- copied from PI page -->Aggregated data (like population frequencies) might not be considered sensitive anymore, but a decision has to be made on a case-to-case basis.

Even if the data is only referred to by an identifier that is not associated with the individual, and the researchers processing the data are not themselves in possession of the key of how the identifier relates to the individual, the data is still personal data, as the person can be [identified indirectly](#personal-data). In this case the data is said to be [pseudonymised](#pseudonymisation). <!-- copied and rephrased from PI page -->Data should be processed in pseudonymised form whenever possible, meaning that no directly identifiable information about the research subjects is included in the data and metadata.

As defined in [Article 5](#principles-of-processing-of-personal-data), to process personal data, the Controller must:

* Identify the **legal basis** for data processing *before it starts*
* Inform in a transparent and honest way
* Decide the **purpose** and stick to it
* Only collect data that is needed
* Not collect more data than necessary
* Not use data for another incompatible purpose
* Erase data when no longer needed (there might be exemptions to this for research data)
* Ensure that data is correct and updated
* Protect collected data – confidential and intact

And be able to **demonstrate** that the GDPR is followed.

There are two [legal bases](#legal-basis-for-processing-personal-data) that could be applicable for processing sensitive personal data for research purposes: [public interest](#public-interest) and [consent](#consent). In Sweden, public interest seems to be considered the most appropriate when processing personal data for research purposes at universities.

It is important that all personnel that process the data are aware of the purpose for which the data has been consented, to not unintentionally use it for any incompatible purpose.

A researcher processing personal data should therefore have defined the **legal basis** and the **purpose** for processing that data, and what (and only what) data is needed to perform the purpose. Furthermore, to have defined what procedures are to be used to ensure that data is correct and protected. The [security measures](#security-of-processing) taken should be based on an evaluation of the risks for, and consequences of, the personal data not being correct and protected. Appropriate technical and organisational measures shall be implemented to ensure a level of security appropriate to the risk. It is advisable that the researcher seek guidance from the legal and information security functions of the university adminstration about this.

The UPPMAX [Bianca](http://www.uppmax.uu.se/support/user-guides/bianca-user-guide/) system has been designed to have technical and information security procedures that are appropriate for processing sensitive human data for analysis. Using this systems then relieves the researcher from having to define these technical and security procedures themselves (at least for the analysis phase of a project). The researcher can decide to analyse (sensitive) personal data elsewhere, but then they will have to define the appropriate procedures. <!-- copied from PI page -->In case the Controller work at a different institute than Uppsala University, a data processing agreement between that institute and UPPMAX/Uppsala University, needs to be established - see [instructions](https://www.uppmax.uu.se/support/faq/general-miscellaneous-faq/sensitive+data+questions/) at UPPMAX.
___
## Legal references for key concepts
### Personal data
[Article 4 (1)](https://gdpr-info.eu/art-4-gdpr/): ‘**personal data**’ means any information relating to an identified or identifiable natural person (‘data subject’); an identifiable natural person is one who can be identified, directly or ***indirectly***, in particular by reference to an identifier such as a name, an identification number, location data, an online identifier or to one or more factors specific to the physical, physiological, ***genetic***, mental, economic, cultural or social identity of that natural person

### Sensitive data
[Article 9](https://gdpr-info.eu/art-9-gdpr/) – The following personal data is considered ‘sensitive’ and is subject to specific processing conditions:

* personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs;
* trade-union membership;
* ***genetic data***, biometric data processed solely to identify a human being;
* ***health-related data***;
* data concerning a person’s sex life or sexual orientation.

Processing of sensitive personal data is only allowed during certain circumstances outlined in Article 9, among them that the data subject has given explicit consent, or for reasons of substantial public interest. It can be noted that EU member states can introduce further conditions, including limitations, with regard to the processing of genetic data, biometric data or data concerning health. *Currently, no such further conditions have been suggested for Sweden.*

### Genetic data
[Article 4 (13)](https://gdpr-info.eu/art-4-gdpr/): ‘**genetic data**’ means personal data relating to the inherited or acquired genetic characteristics of a natural person which give unique information about the physiology or the health of that natural person and which result, in particular, from an analysis of a biological sample from the natural person in question

[Recital 34](https://gdpr-info.eu/recitals/no-34/): “Genetic data should be defined as personal data relating to the inherited or acquired genetic characteristics of a natural person which result from the analysis of a biological sample from the natural person in question, in particular chromosomal, deoxyribonucleic acid (DNA) or ribonucleic acid (RNA) analysis, or from the analysis of another element enabling equivalent information to be obtained.”

### Pseudonymisation
[Article 4 (1)](https://gdpr-info.eu/art-4-gdpr/): ‘**pseudonymisation**’ means the processing of personal data in such a manner that the personal data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately and is subject to technical and organisational measures to ensure that the personal data are not attributed to an identified or identifiable natural person

### Roles
#### *Controller*
[Article 4 (7)](https://gdpr-info.eu/art-4-gdpr/): ‘**controller**’ means the natural or legal person, public authority, agency or other body which, alone or jointly with others, determines the purposes and means of the processing of personal data; […]

#### *Processor*
[Article 4 (8)](https://gdpr-info.eu/art-4-gdpr/): ‘**processor**’ means a natural or legal person, public authority, agency or other body which processes personal data on behalf of the controller.

#### *Contract Controller-Processor*
[Article 28 (3)](https://gdpr-info.eu/art-28-gdpr/): Processing by a processor shall be governed by a contract or other legal act under Union or Member State law, that is binding on the processor with regard to the controller and that sets out the subject-matter and duration of the processing, the nature and purpose of the processing, the type of personal data and categories of data subjects and the obligations and rights of the controller. […]

## Principles of processing of personal data
Central to the GDPR are the [Principles relating to processing of personal data - Article 5](https://gdpr-info.eu/art-5-gdpr/):

>(1) Personal data shall be:
>
>a) processed lawfully, fairly and in a transparent manner in relation to the data subject (‘lawfulness, fairness and transparency’);
>
>b) collected for specified, explicit and legitimate purposes and not further processed in a manner that is incompatible with those purposes; further processing for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes shall, in accordance with [Article 89(1)](https://gdpr-info.eu/art-89-gdpr/), not be considered to be incompatible with the initial purposes (‘purpose limitation’);
>
>c) adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed (‘data minimisation’);
>
>d) accurate and, where necessary, kept up to date; every reasonable step must be taken to ensure that personal data that are inaccurate, having regard to the purposes for which they are processed, are erased or rectified without delay (‘accuracy’);
>
>e) kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data will be processed solely for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes in accordance with [Article 89(1)](https://gdpr-info.eu/art-89-gdpr/) subject to implementation of the appropriate technical and organisational measures required by this Regulation in order to safeguard the rights and freedoms of the data subject (‘storage limitation’);
>
>f) processed in a manner that ensures appropriate security of the personal data, including protection against unauthorised or unlawful processing and against accidental loss, destruction or damage, using appropriate technical or organisational measures (‘integrity and confidentiality’).
>
>(2) The controller shall be responsible for, and be able to demonstrate compliance with, paragraph 1 (‘accountability’).

### Legal basis for processing personal data
[Article 6](https://gdpr-info.eu/art-6-gdpr/) – Personal data can only be processed in the following circumstances:

* with the **consent** of the individuals concerned;
* where there is a **contractual obligation** (a contract between your company/organisation and a client);
* to meet a **legal obligation** under EU or national legislation;
* where processing is necessary for the performance of a task carried out in the **public interest** under EU or national legislation;
* to protect the **vital interests** of an individual;
* for your organisation’s **legitimate interests**, but only after having checked that the fundamental rights and freedoms of the person whose data you’re processing aren’t seriously impacted.

### Consent
[Article 4 (11)](https://gdpr-info.eu/art-4-gdpr/): ‘**consent**’ of the data subject means any freely given, specific, informed and unambiguous indication of the data subject’s wishes by which he or she, by a statement or by a clear affirmative action, signifies agreement to the processing of personal data relating to him or her.

### Public interest
Exercise of official authority or task in the public interest: The data controller must process personal data in order to carry out its duties as an authority or to carry out a task in the public interest. [Article 6](https://gdpr-info.eu/art-6-gdpr/).

### Security of processing
[Article 32](https://gdpr-info.eu/art-32-gdpr/) - “*Taking into account the state of the art, the costs of implementation and the nature, scope, context and purposes of processing as well as the risk of varying likelihood and severity for the rights and freedoms of natural persons, the controller and the processor shall implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk*”

### Data breach
[Article 4 (12)](https://gdpr-info.eu/art-4-gdpr/): ‘**personal data breach**’ means a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted, stored or otherwise processed;

## Further references
### GDPR text
* [Dataskyddsförordningen](https://www.imy.se/verksamhet/dataskydd/det-har-galler-enligt-gdpr/introduktion-till-gdpr/dataskyddsforordningen-i-fulltext/) - *Swedish*
* [General Data Protection Regulation](https://gdpr-info.eu/) - *English*

### Information about the GDPR
* The Swedish Data Protection Authority (*Datainspektionen*) [GDPR information pages](https://www.imy.se/verksamhet/dataskydd/det-har-galler-enligt-gdpr/introduktion-till-gdpr/) - *Swedish*
* European Commission [Data Protection information pages](https://ec.europa.eu/info/law/law-topics/data-protection/reform_en) - *English*

## Further questions
If you have further questions regarding sensitive personal data, you are welcome to contact the SciLifeLab data management team (<data-management@scilifelab.se>).
