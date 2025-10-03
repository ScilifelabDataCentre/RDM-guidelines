---
title: Sharing code and workflows
category: Other
tags: ["research outputs", "RSQkit","software", "scripts"]
toc: True
---

# Sharing code and workflows 
In the era of FAIR (Findable, Accessible, Interoperable and Reusable) and <a href="https://www.vr.se/english/mandates/open-science/open-access-to-research-data.html" target="_blank">Open Science</a>, **all research outputs** should be shared and made available to the public. This includes the code and workflows produced during the course of the research project. This page, while not exhaustive, aims to give an introduction to the topic of FAIR code. 

<a class="link-teal" href="/topics/fair-principles"><b>Learn more about the FAIR principles <i class="bi bi-arrow-right-square"></i></b></a>

## What are code & workflows?

**Code**

Code in this context ranges from individual instructions and scripts, to software. Individual instructions and scripts are pieces of code that execute specific tasks or algorithms within research contexts. This could include anything from simple data manipulation or visualisation to complex simulations. Software encompasses code in a packaged, documented and operational form, designed to conduct a range of scientific tasks, thereby becoming an essential tool in the research project.

**Workflows** 

Scientific workflows or pipelines are code that describe the structured sequences that organise and automate research tasks. They detail the flow of data between tasks, often managed by Workflow Management Systems (WMS), and encapsulate a higher level of complexity by integrating multiple software components, scripts, and tools. 

## Why share code & workflows?

In life science research, code and workflows are often as important as the data itself. From data processing scripts to full analysis pipelines — sharing your code is about <b>openness</b>, <b>improving</b> your science, gaining <b>recognition</b>, and allowing others to build on your work.

<br><br>
<img src="/img/illustrations/code-workflows-visual.png" alt="Benefits of sharing code and workflows" class="img-fluid">
<small>© Media Elements sourced from <a href="http://canva.com/" target="_blank">Canva.com</a></small>
<br><br>

Openly sharing code and workflows not only fulfils key scientific and ethical principles, but also catalyses new discoveries and collaborations across the life sciences. It ensures that research methodologies are transparent, reproducible, and accessible to all, laying the groundwork for a more inclusive and innovative scientific community.

* **Strengthen scientific integrity and utility** - Clear documentation and the ability to replicate analyses build trust in scientific results, and are essential for verifying and understanding research findings. Sharing workflows allows them to be applied to new datasets or challenges, maximising the utility and lifespan of research tools, and preventing the loss of valuable methodologies.

* **Enhance research efficiency and compliance** - Modular, well-documented code facilitates smoother research processes, from rerunning experiments to adapting methodologies for new data.  Publishing code and data independently of each other, and of associated research articles, simplifies compliance with licencing requirements. Adherence with open code mandates set by journals and funders both enhances research credibility, and broadens dissemination. Open code obtains scholarly recognition through citations, emphasising the importance of code as a research output.

* **Foster collaboration and global innovation** - Sharing tools broadens their reach, enabling equitable access and serving as vital resources for training the next generation of scientists, particularly in resource-limited settings. Open code encourages community input and interdisciplinary exchanges, leading to more robust, flexible solutions, and sparking innovation across research domains.

<a class="link-teal" href="https://www.software.ac.uk/blog/why-should-you-care-about-reproducible-code-and-how-get-started" target="_blank"> <b>Learn more about practical benefits from Software Sustainability Institute <i class="bi bi-box-arrow-up-right"></i></b></a>

<a class="link-teal" href="https://everse.software/RSQKit/fair_rs" target="_blank"><b>Read about FAIR Research Software Principles at RSQKit <i class="bi bi-box-arrow-up-right"></i></b></a>

## How to share code & workflows?

How you share code and workflows depends on your goals; whether you seek transparency, collaboration, or community contributions. Keep in mind that your objectives may evolve over time, and every step towards FAIR practices adds value.  

<a class="link-teal" href="https://github.com/ScilifelabDataCentre/open-science-checklists/blob/main/open_software_checklist.md" target="_blank"> <b>Consult the SciLifeLab Open Science Software Checklist for comprehensive guidance <i class="bi bi-box-arrow-up-right"></i></b></a>

### Where can code and workflows be shared?

To ensure transparency, make a copy of your code or workflow available for long-term access, independent of any research paper. This should be accompanied by a README file with a clear description, usage instructions, and licence(s). Remember to also describe the compute environment (platform, specific software versions, dependencies or libraries used) in order to ensure compatibility and eliminate potential version conflicts or discrepancies. Collaborative version control platforms, such as GitHub, are ideal for both sharing and ongoing development. Use tags or releases to be able to reference specific versions of your code in publication etc.

To enhance FAIRness, consider obtaining a persistent identifier for your code or workflow. One way to obtain a persisten identifier is by publishing your code or workflow in a research output repository, such as <a href="https://zenodo.org/" target="_blank"> Zenodo</a> or the <a href="https://figshare.scilifelab.se/" target="_blank">SciLifeLab Data Repository</a>. This can be achieved by linking your GitHub repository or uploading files directly. Another way to obtain a persistent identifier is via the <a href="https://rrid.site" target= "_blank">Research Resource Identification Portal (RRID)</a>. 

If your code or workflow is intended for reuse, distribute it through a package manager (e.g., <a href="https://bioconda.github.io/" target= "_blank">BioConda</a> or <a href="https://cran.r-project.org/" target= "_blank">CRAN</a>). For workflows, consider joining communities like <a href="https://nf-co.re/" target= "_blank">nf-core</a> or <a href="https://galaxyproject.org/eu/" target= "_blank">Galaxy Europe</a>, and register your workflow on platforms such as <a href="https://workflowhub.eu/" target= "_blank">WorkflowHub</a>. These steps help others build upon your work.

For software, consider publishing in a dedicated software journal (e.g. <a href="https://joss.theoj.org/" target= "_blank">Journal of Open Source Software</a>) or as a software article in a life sciences journal (e.g. <a href="https://collections.plos.org/collection/software/" target= "_blank">PLOS Computational Biology</a> or <a href="https://bmcbioinformatics.biomedcentral.com/submission-guidelines/preparing-your-manuscript/software-article" target= "_blank">BMC Bioinformatics</a>).

<a class="link-teal" href="https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content" target="_blank"><b>Referencing and citing content on GitHub <i class="bi bi-box-arrow-up-right"></i></b></a>

### Tips & Tricks

- Start from a template or "cookie cutter" to streamline setup, and follow best practices. 
- Write readable code by using meaningful variable names, a logical structure, and clear comments. Some coding languages offer packages/tools that lint and format code for consistency. 
- Expand your README file beyond the basics. See our [README topic page](https://data-guidelines.scilifelab.se/topics/readme-files) for inspiration. 
- Ask a colleague to test whether they can access and understand how to use the code.
- Remember to cite your code in your research publications.





## Resources
Please find below resources concerning the sharing of code and workflows in form of training, guidance, and/or tools.

{{< resources-per-page-topics >}}
