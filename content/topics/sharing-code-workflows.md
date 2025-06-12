---
title: Sharing code and workflows
category: Other
toc: True
---

# Sharing code and workflows 
In the era of [FAIR](https://data-guidelines.scilifelab.se/topics/fair-principles) (Findable, Accessible, Interoperable and Reusable) and [Open Science](https://www.vr.se/english/mandates/open-science/open-access-to-research-data.html), **all research outputs** should be shared and made available to the public. This includes the code and workflows produced during the course of the research project.

## What are code & workflows?

**Code**

Code in this context ranges from individual instructions and scripts, to software. Individual instructions and scripts are pieces of code that execute specific tasks or algorithms within research contexts. This could include anything from simple data manipulation or visualisation to complex simulations. 
Software encompasses code in a packaged, documented and operational form, designed to conduct a range of scientific tasks, thereby becoming an essential tool in the research project.

**Workflows** 

Scientific workflows or pipelines describe the structured sequences that organise and automate research tasks. They detail the flow of data between tasks, often managed by Workflow Management Systems (WMS), and encapsulate a higher level of complexity by integrating multiple software components, scripts, and tools. 

## Why share code & workflows?
<div class="row">
  <div class="col-7">
    In life science research, code and workflows are often as important as the data itself. From data processing scripts to full analysis pipelines — sharing your code is about <b>openness</b>, <b>improving</b> your science, gaining <b>recognition</b>, and allowing others to build on your work.
    <br><br>
    Openly sharing code and workflows not only fulfils key scientific and ethical principles, but also catalyses new discoveries and collaborations across the life sciences. It ensures that research methodologies are transparent, reproducible, and accessible to all, laying the groundwork for a more inclusive and innovative scientific community.
  </div>
  <div class="col-5" style="text-align: center;">
    <img src="/img/illustrations/works-on-my-computer.JPG" alt="Works on my computer" class="img-fluid">
    <br><small>Robot: MetaManMachine by Nikola Vasiljevic (2021), CC BY-SA 4.0, doi:<a href="https://doi.org/10.5281/zenodo.4471098" target="_blank">10.5281/zenodo.4471098</a></small>
  </div>
</div>

### Strengthen scientific integrity and utility

* **Transparency and Reproducibility** – Clear documentation and the ability to replicate analyses build trust in scientific results, and are essential for verifying and understanding research findings.
* **Reusability and Preservation** – Sharing workflows allows them to be applied to new datasets or challenges, maximising the utility and lifespan of research tools, and preventing the loss of valuable methodologies.

### Enhance research efficiency and compliance

* **Operational Efficiency** – Modular, well-documented software facilitates smoother research processes, from rerunning experiments to adapting methodologies for new data. 
* **Legal and Ethical Compliance** – Publishing software and data independently of each other, and of associated research articles, simplifies compliance with licencing requirements. Adherence with open code mandates set by journals and funders both enhances research credibility, and broadens dissemination.
* **Recognition** – Open code obtains scholarly recognition through citations, emphasising the importance of software as a research output.

### Foster collaboration and global innovation
* **Global Access and Education** – Sharing tools broadens their reach, enabling equitable access and serving as vital resources for training the next generation of scientists, particularly in resource-limited settings.
* **Community Contributions and Cross-Field Innovation** – Open software encourages community input and interdisciplinary exchanges, leading to more robust, flexible solutions and sparking innovation across research domains.

<a class="link-teal" href="https://www.software.ac.uk/blog/why-should-you-care-about-reproducible-code-and-how-get-started" target="_blank"> <b>Learn more about practical benefits and how to get started <i class="bi bi-box-arrow-up-right"></i></b></a>

<a class="link-teal" href="https://urn.kb.se/resolve?urn=urn:nbn:se:kb:publ-738" target="_blank"><b>Download and read the National Library of Sweden’s national guidelines <i class="bi bi-box-arrow-up-right"></i></b></a>

## How to share code & workflows?

How you share code and workflows depends on your goals; whether you seek transparency, collaboration, or community contributions. Keep in mind that your objectives may evolve over time, and every step towards FAIR practices adds value.  

<a class="link-teal" href="https://github.com/ScilifelabDataCentre/open-science-checklists/blob/main/open_software_checklist.md" target="_blank"> <b>Consult the SciLifeLab Open Science Software Checklist for comprehensive guidance<i class="bi bi-box-arrow-up-right"></i></b></a>

### Where can code and workflows be shared?

To ensure transparency, make a static copy of your code or workflow available for long-term access, independent of any research paper. This should be accompanied by a README file with a clear description, usage instructions, and licence(s). Collaborative version control platforms, such as GitHub, are ideal for both sharing and ongoing development. Use tags or releases to reference specific versions of your code.

To enhance FAIRness, consider obtaining a persistent identifier by publishing your code or workflow in a research output repository, such as [Zenodo](https://zenodo.org/) or the [SciLifeLab Data Repository](https://figshare.scilifelab.se/). This can be achieved by linking your GitHub repository or uploading files directly.

If your code or workflow is intended for reuse, distribute it through a package manager (e.g., [BioConda](https://bioconda.github.io/) or [CRAN](https://cran.r-project.org/)). For workflows, consider joining communities like [nf-core](https://nf-co.re/) or [Galaxy Europe](https://galaxyproject.org/eu/), and register your workflow on platforms such as [WorkflowHub](https://workflowhub.eu/). These steps help others build upon your work.

For software, consider publishing in a dedicated software journal (e.g. [Journal of Open Source Software](https://joss.theoj.org/)) or as a software article in a life sciences journal (e.g. [PLOS Computational Biology](https://collections.plos.org/collection/software/) or [BMC Bioinformatics](https://bmcbioinformatics.biomedcentral.com/submission-guidelines/preparing-your-manuscript/software-article)).

### Tips & Tricks

- Start from a template or "cookie cutter" to streamline setup, and follow best practices. 
- Write readable code by using meaningful variable names, a logical structure, and clear comments. Some coding languages offer packages/tools that lint and format code for consistency. 
- Expand your README file beyond the basics. See our [README topic page](https://data-guidelines.scilifelab.se/topics/readme-files) for inspiration. 
- Ask a colleague to test whether they can access and understand how to use the code.
- Remember to cite your code in your research publications.





## Resources
Please find below resources concerning the sharing of code and workflows in form of training, guidance, and/or tools.

{{< resources-per-page-topics >}}
