---
title: Sharing code and workflows
category: Other
toc: True
---

# Sharing code and workflows 
In the era of [FAIR](https://data-guidelines.scilifelab.se/topics/fair-principles) (Findable, Accessible, Interoperable and Reusable) and [Open science](https://www.vr.se/english/mandates/open-science/open-access-to-research-data.html), **all research outputs** should be shared and made available to the public. This includes the code and workflows produced during the course of the research project.

## What is code & workflows?
**Code**

Code in this context ranges from individual instructions and scripts, to software. Individual instructions and scripts are code that execute specific tasks or algorithms within research contexts, from simple data manipulation and visualisation to complex simulations. 
Software encompasses code in a packaged, documented and operational form, designed to conduct a range of scientific tasks, thereby becoming an essential tool in the research project.

**Workflows** 

Scientific workflows or pipelines describe the structured sequences that organize and automate research tasks. They detail the flow of data between tasks, often managed by Workflow Management Systems (WMS), and encapsulate a higher level of complexity by integrating multiple software components, scripts, and tools. 

## Why share code & workflows?
<div class="row">
  <div class="col-7">
    In life science research, code and workflows are often as important as the data itself. From data processing scripts to full analysis pipelines — sharing your code is about <b>openness</b>, <b>improving</b> your science, gaining <b>recognition</b>, and allowing others to build on your work.
    <br><br>
    Openly sharing code and workflows not only fulfills key scientific and ethical principles but also catalyzes new discoveries and collaborations across the life sciences. It ensures that research methodologies are transparent, reproducible, and accessible to all, laying the groundwork for a more inclusive and innovative scientific community.
  </div>
  <div class="col-5" style="text-align: center;">
    <img src="/img/illustrations/works-on-my-computer.JPG" alt="Works on my computer" class="img-fluid">
    <br><small>Robot: MetaManMachine by Nikola Vasiljevic (2021), CC BY-SA 4.0, doi:<a href="https://doi.org/10.5281/zenodo.4471098" target="_blank">10.5281/zenodo.4471098</a></small>
  </div>
</div>

### Strengthen scientific integrity and utility

* **Transparency and Reproducibility** – Clear documentation and the ability to replicate analyses build trust in scientific results, and is essential for verifying and understanding research findings.
* **Reusability and Preservation** – Sharing enables workflows to be applied to new datasets or challenges, maximising the utility and lifespan of research tools and preventing the loss of valuable methodologies.

### Enhance research efficiency and compliance

* **Operational Efficiency** – Modular, well-documented software facilitates smoother research processes, from rerunning experiments to adapting methodologies for new data. 
* **Legal and Ethical Compliance** – Separate publication of software and data simplifies adherence to licensing requirements, while meeting journals' and funders' open code mandates strengthens research credibility and dissemination.
* **Recognition** – Open code obtains scholarly recognition through citations, emphasizing the importance of software as a research output.

### Foster collaboration and global innovation
* **Global Access and Education** – Sharing tools broadens their reach, enabling equitable access and serving as vital resources for training the next generation of scientists, particularly in resource-limited settings.
* **Community Contributions and Cross-Field Innovation** – Open software encourages community input and interdisciplinary exchanges, leading to more robust, flexible solutions and sparking innovation across research domains.

<a class="link-teal" href="https://www.software.ac.uk/blog/why-should-you-care-about-reproducible-code-and-how-get-started" target="_blank"> <b>Learn more about practical benefits and how to get started <i class="bi bi-box-arrow-up-right"></i></b></a>

<a class="link-teal" href="https://urn.kb.se/resolve?urn=urn:nbn:se:kb:publ-738" target="_blank"><b>Download and read the National Library of Sweden’s national guidelines <i class="bi bi-box-arrow-up-right"></i></b></a>

## How to share code & workflows?
How you choose to share code and workflows depends on your goal with the sharing. If your goal is to get contributions from others you will need to take more actions than if you only want to be transparent. Keep in mind that your goal can shift along the process and that any step towards FAIR is useful.

At minimum, a static copy of the code or workflow needs to be accessible long-term, independent from the research paper, so that it can be referenced. It should also be accompanied with a README file, that includes a description and instructions on how to use, and a license. 

When choosing what level of sharing is useful for a specific output consider these questions:

### Where can it be shared? (Findable)
1. At a collaborative version control service for active development e.g. GitHub
1. In a repository for publishing research outputs e.g. Zenodo or SciLifeLab Data Repository
1. Via a package manager (if intended for reuse) e.g BioConda or CRAN https://en.wikipedia.org/wiki/List_of_software_package_management_systems 
1. Via a software journal (publish papers about software either in software specific journals such as https://joss.theoj.org/ or in the software track of established life sciences journals, eg Plos Comp Bio https://collections.plos.org/collection/software/ or BMC Bioinformatics https://bmcbioinformatics.biomedcentral.com/submission-guidelines/preparing-your-manuscript/software-article)

### How will it be used?
1. For others to understand/review what has been done
1. For re-use as is by a small number of ppl
1. For others to build upon 


### Other considerations or recommendations:
* Consider starting from a template (sometimes called cookie cutter), e.g.: https://github.com/molssi/cookiecutter-cms
* Look at the OS checklist
* Rich metadata! (Reusable)
* Writing readable code (variable names, structure, comments/documentation)
* Expand the README - [readme.so](https://readme.so/)
    * **Description** 
    * **How to install/run**
    * Usage examples
    * How to contribute
    * Conditions of use
    * Suggested citation
    * Related publications if any
* Ask a colleague to test if they have access and can understand how to use the code
* Cite your code in your research paper

## Resources
Please find below resources concerning the sharing of code and workflows in form of training, guidance and/or tools.

{{< resources-per-page-topics >}}
