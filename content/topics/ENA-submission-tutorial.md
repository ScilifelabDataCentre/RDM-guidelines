---
title: ENA submission tutorial
category: Other
tags: ["submission methods","interactive","command line","programmatic","study","sample","raw reads","sequencing data","assembly","umbrella"]
toc: True
---

# ENA submission tutorial

The aim of this tutorial is to provide guidance through the process of submitting genomics data to the <a href="https://www.ebi.ac.uk/ena/" target="_blank">European Nucleotide Archive</a> (ENA). The task is to submit  the genomic sequence data used to create an assembly, to one study, submit the assembly to another study, and then finally group these two studies together under an umbrella study. By the end of this tutorial you will:
* Understand the terminology used by ENA.
* Know how to properly describe and format your genomics data for submission.
* Know how to do a submission.

It serves as complementary material, including examples, to the <a href="https://ena-docs.readthedocs.io/en/latest/index.html" target="_blank">ENA Documentation</a>.

## Preparations
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseFind1" role="button" aria-expanded="false" aria-controls="collapseFind1">
    Obtaining an ENA Webin Account
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseFind1">
  <div class="card card-body">
    <span>
        In order to do a submission, you need an account in ENA. To create an account, please go to the <a href="https://www.ebi.ac.uk/ena/submit/webin/" target="_blank">ENA submission homepage</a>, click on <b>Register</b>, and fill in the required details.
        <br><br>
        <i>Login page on the ENA submission homepage:</i>
        <br><br>
        <div class="text-center">
        <img src="/img/ena_tutorial/ENA_login_startpage.png" height="350" class="rounded">
        </div>
        <br><br>
        <i>Enter account details to obtain an account in ENA:</i>
        <br><br>
        <div class="text-center">
        <img src="/img/ena_tutorial/ENA_login_detailspage.png" height="500" class="rounded">
        </div>
        <br><br>
        <h3>Add contacts</h3>
        Once you have filled in all of the required fields, you can log in to the submission service. You may wish to add contacts if you are working with other people to complete your submission. You can do this by logging into your account then selecting <i>Home > Manage account</i>. Any contacts that you add will be notified if there are any major changes to data submissions, and they will be listed as contacts on public data.
    </span>
  </div>  
  <br>
</div>

<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseFind2" role="button" aria-expanded="false" aria-controls="collapseFind2">
    Preparing the metadata
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseFind2">
  <div class="card card-body">
    <span>
        To ensure that sample data is registered with at least a minimum amount of metadata, ENA provides <a href="https://www.ebi.ac.uk/ena/browser/checklists" target="_blank">“Sample Checklists”</a> which are used to tailor the sample descriptions to fit minimum standards. For convenience, we have created templates for the checklists we have used. The templates come with instructions on how to do an interactive submission, via the ENA Webin Portal, but even when doing a programmatic submission, the template can be useful for collecting all necessary descriptions / metadata.
        <br><br>
        Download an appropriate template, and fill in the sheets according to the instructions in the template:
        <ul>
            <li>ERC000011 <a href="/files/meta-data-templates/metadata_template_default_ERC000011.xlsx">ENA default sample checklist </a>(Excel spreadsheet)</li>
            <li>ERC000015 <a href="/files/meta-data-templates/metadata_template_human-gut_ERC000015.xlsx">GSC MIxS human gut </a>(Excel spreadsheet)</li>
            <li>ERC000024 <a href="/files/meta-data-templates/metadata_template_GSC-MIxS-water_ERC000024.xlsx">GSC MIxS water </a>(Excel spreadsheet)</li>
            <li>ERC000033 <a href="/files/meta-data-templates/metadata_template_virus_ERC000033.xlsx">ENA virus pathogen reporting standard checklist </a>(Excel spreadsheet)</li>
            <li>ERC000036 <a href="/files/meta-data-templates/metadata_template_sewage_ERC000036.xlsx">ENA sewage checklist </a>(Excel spreadsheet)</li>
            <li>ERC000050 <a href="/files/meta-data-templates/metadata_template_ENA_binned_metagenome_ERC000050.xlsx">ENA binned metagenome checklist </a>(Excel spreadsheet)</li>
            <li>ERC000053 <a href="/files/meta-data-templates/metadata_template_tree-of-life_ERC000053.xlsx">Tree of Life Checklist </a>(Excel spreadsheet)</li>
        </ul>
        <!-- question is if we should link to VIB templates instead of ours, but that we can do in the future. Perhaps not, they do differ which can be confusing for users -->
        The templates are divided into five sheets (each related to a type of metadata object), namely <b>study</b>, <b>sample</b>, <b>experiment</b>, <b>run</b> and <b>assemblies</b>. It is good practice to fill in all relevant sheets in the template, as having all the metadata collected in one place eases the submission process.
        <br><br>
        In the sample sheet, the first row contains the following:
        <ol>
          <li>The name of the checklist</li>
          <li>Field names</li>
          <li>Description of the field</li>
          <li>If the field is mandatory, recommended or optional</li>
        </ol>
        Note that some fields have controlled vocabulary, which are available in the template as drop-down lists (the lists become visible when you click on a cell).
        <br><br>
        <b>Note</b>: It is <i>strongly</i> recommended that you provide as much information as possible in the metadata sheets as it will increase the <a href="https://www.go-fair.org/fair-principles/" target="_blank">FAIRness</a> of your data, and thus the probability of it being useful in future research efforts. 
        <h3>An example</h3>
        In this scenario we have used the Tree of life checklist. A completed template is found in <a href="/files/ena_tutorial/Alectoris-graeca-metadata.xlsx">Alectoris-graeca-metadata.xlsx</a>, adapted from a real submission made under the <a href="https://biodiversitygenomics.eu/" target="_blank">Biodiversity Genomics Europe</a> (BGE) project organised by the <a href="https://www.erga-biodiversity.eu/" target="_blank">European Reference Genome Atlas</a> (ERGA) initiative. The task is to submit four datasets (one PacBio HiFi WGS, two Illumina HiC, and one Illumina RNAseq), including four samples, all in one study, plus a chromosome level assembly in another study, and then group these them studies together under an umbrella study. Please note that it is not necessary to submit the assembly in a study separate from the raw reads. In our example it is done to demonstrate how umbrella studies can be used.
    </span>
  </div>  
  <br>
</div>

<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseFind3" role="button" aria-expanded="false" aria-controls="collapseFind3">
    Preparing the data files
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseFind3">
  <div class="card card-body">
    <span>
    In the run sheet of a metadata template, the file names of the raw reads and their md5 checksums are collected. For the three types of submissions of raw reads described in this tutorial, the data files need to be uploaded to the dropbox on ENA's servers. The exact name of the files as they reside at ENA, including any subfolders, should be filled in the run sheet. The checksums are used to validate that the data transfers have been completed without loss.
    <h3>Checksums</h3>
    Typically you will receive the checksums from the data producer in the delivery, but in case you need to calculate them yourself:
    <br><br>
    <ol>
        <li> Open a terminal (command prompt) window and change to the directory where the raw reads are located, e.g. <code>cd my_data/raw/</code>.</li>
        <li>Modify and execute the command <code>md5sum * > checksums-md5.txt</code> to match your file names and required output name. The command will calculate the checksums for all files in current directory and list them in a file named checksums-md5.txt.</li>
    </ol>
    <h3>Data transfers</h3>
    There are multiple ways of transferring the raw read files to ENA upload area, depending on which type of machine the transfer is initiated from, see <a href="https://ena-docs.readthedocs.io/en/latest/submit/fileprep/upload.html" target="_blank">ENA documentation on file upload</a>. If all else fails, a simple <code>lftp</code> will work, but  large file transfers always risk transfer interruption, and you will have to start all over again. In order to avoid this, it might be worth the effort of installing and using Aspera, since it has the functionality of resuming transfers. For more information regarding using Aspera, please see our topic page on <a href="/topics/data-transfer">Data transfer</a>.
    </span>
  </div>  
  <br>
</div>

## Submission methods

ENA describes <a href="https://ena-docs.readthedocs.io/en/latest/submit/general-guide.html" target="_blank">three methods</a> of submission, none of which can be used to complete all parts of a submission: interactive, command line (using Webin-CLI), and programmatic.

### Interactive Submission Method
This method involves filling out web forms directly in the browser and downloading template spreadsheets that can be completed off-line and later uploaded to ENA. This is the easiest method to use if you are unfamiliar with submissions, but quickly becomes time-consuming with bulk submission (> 50 records). It is possible to register and submit **studies**, **samples**, and **raw reads** this way.

#### Test submission
ENA provides two sites for submission; one for <a href="https://wwwdev.ebi.ac.uk/ena/submit/webin" target="_blank">test submissions</a> and one for <a href="https://www.ebi.ac.uk/ena/submit/webin" target="_blank">'real' submissions</a> (i.e. an actual submission to ENA). We recommend doing a test submission first, using the example data provided, in order to get an understanding of the different steps. <b>Note:</b> The test service is purged every 24 h, meaning that any submitted test file will be removed before the following day, making it impossible to begin a submission one day and continue the next.

<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseFind4a" role="button" aria-expanded="false" aria-controls="collapseFind4a">
    Register studies
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseFind4a">
  <div class="card card-body">
    <span>
        <ul>
            <li>ENA's documentation on <a href="https://ena-docs.readthedocs.io/en/latest/submit/study/interactive.html" target="_blank"> Register a study interactively</a>.</li>
            <li>Go to <a href="https://wwwdev.ebi.ac.uk/ena/submit/webin" target="_blank">ENA login (test)</a> and login.</li>
            <li>After logging in, you will see the landing page (shown below) that includes multiple options for completing your registration. </li>
            <li>In the top left of the landing page, there is a <b>Dashboard</b> menu that expands when you click on it. Click it and select <b>Register Study (Project)</b> or click on the <b>Register Study</b> option in the <i>Studies (Projects)</i> section on the landing page (the options for 'Study' are shown in yellow).</li>
            <br>
            <div class="text-center">
            <img src="/img/ena_tutorial/Step1_register_study.png" height="400" class="rounded">
            </div>
            <br>
            <div class="text-center">
            <img src="/img/ena_tutorial/Step1_register_study_picb.png" height="400" class="rounded">
            </div>
            <br>
            <li>Enter the details of the project, by copy and paste from the metadata template. Asterisks (*) denote mandatory fields. The 'Release date' is the date that the record will become publicly available. This can be updated later, so if you are unsure on a precise date, you can provide an estimated date (maximum two years forward in time). You will get a notification email from ENA, a few weeks prior to the release date, when your data is about to become public. If necessary, the release date can then be consecutively extended any number of times by up to two years.</li>
            <li>In our example the study registration is repeated twice, once for the genomic sequencing data and once for the assembly data. The umbrella study needs to be registered using a different method, see further <b>Umbrella submission</b> in <a href="#programmatic-submission-method"> Programmatic Submission Method</a> below.</li> 
            <br>
            <div class="text-center">
            <img src="/img/ena_tutorial/Step2_register_study.png" height="400" class="rounded">
            </div>
            <br>
            <li> <b>Note:</b> In case you have an annotated assembly you must also provide a <b>locus tag</b> field, e.g. with an abbreviation of the scientific name of the species.</li>
            <li>Click <b>Submit</b>. A pop-up window will appear, check that the submission was successful by reading the content of the window, copy the project accession number (starting with PRJEB...) and add it to your metadata template for future reference, then click <b>Close</b>.</li>
        </ul>
    </span>
  </div>
  <br>
</div>
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseFind4b" role="button" aria-expanded="false" aria-controls="collapseFind4b">
    Register samples
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseFind4b">
  <div class="card card-body">
    <span>
        <ul>
            <li>ENA's documentation on <a href="https://ena-docs.readthedocs.io/en/latest/submit/samples/interactive.html" target="_blank">Register samples interactively</a>.</li>
            <li>Create <a href="/files/ena_tutorial/Alectoris-graeca-samples.tsv">Alectoris-graeca-samples.tsv</a> by copying the filled rows of the <code>ENA_samples</code> sheet of a metadata template in .tsv format. This can be done in any text editor, e.g. Notepad or Visual Studio Code. 
            <li>Remove rows 3 (with field descriptions) and 4 (with info if mandatory/recommended/optional) from the .tsv file.</li>
            <li>Go to the browser where you are logged in to ENA, and register the samples either by clicking on the Dashboard menu (top left of the page) and selecting <b>Register Samples</b> or by clicking on the <b>Register Samples</b> option in the <b>Samples</b> section of the landing page (all related options in green).
            <br><br>
            Both of the above options lead to the same place, which gives two options: (1) Download spreadsheet to register samples, and (2) Upload filled spreadsheet to register samples.</li>
            <br>
            <div class="text-center">
            <img src="/img/ena_tutorial/Register_sample_options.png" height="250" class="rounded">
            </div>
            <br>
            <li>Select the latter and upload the samples .tsv file. Click on <b>Submit Completed Spreadsheet</b>, verify that the submission was successful in the pop-up Submission window, and then click <b>Close</b>.</li>
        </ul>
    </span>
  </div>
  <br>
</div>
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseFind4c" role="button" aria-expanded="false" aria-controls="collapseFind4c">
    Submit raw reads
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseFind4c">
  <div class="card card-body">
    <span>
        <ul>
            <li>ENA's documentation on <a href="https://ena-docs.readthedocs.io/en/latest/submit/reads/interactive.html" target="_blank">Submit raw reads interactively</a>.</li>
            <li>Raw reads are submitted in a similar fashion as samples, with the exception of one additional step:
            <ul>
                <li>For interactive submission of raw reads, one needs to combine the information concerning the experiment and the runs into one .tsv file. Hence, copy cells A1:F7 in the 'ENA_run' sheet and paste them to cells added to the cells M2:R8 in 'ENA_experiment' sheet (this is already done in the example .xlsx file).</li>
            </ul>
            <li>Create <a href="/files/ena_tutorial/Alectoris-graeca-experiments.tsv">Alectoris-graeca-experiments.tsv</a> by copying the filled rows of the <code>ENA_experiment</code> sheet of a metadata template in .tsv format. This can be done in any text editor, e.g. Notepad or Visual Studio Code. </li>
            <li>Remove rows 3 (with field descriptions) and 4 (with info if mandatory/recommended/optional) from the .tsv file.</li>
            <li>Go to the browser where you are logged in to ENA, and register the experiments either by clicking on the Dashboard menu (top left of the page) and selecting <b>Submit Reads</b>, or by clicking on the <b>Submit Reads</b> option in the <b>Raw Reads (Experiments and Runs)</b> section of the landing page (all related options in orange).</li>
            <li>Both of the above options lead to the same place, which gives two options: (1) Download spreadsheet template for Read submission, and (2) Upload filled spreadsheet template for Read submission.</li>
            <li>Select the latter and upload the experiments .tsv file. Click on <b>Submit Completed Spreadsheet</b>, verify that the submission was successful in the pop-up Submission window, and then click <b>Close</b>.</li>
        </ul>
    </span>
  </div>  
  <br>
</div>

### Command-Line Submission Method
This method uses ENA’s **Webin-CLI program**. Submissions require the preparation of text (manifest) files that are validated before submissions are completed. It is possible to submit **raw reads** and **assemblies**, this way. Actually, for assemblies, this is the **only** way to submit.

<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseFind6" role="button" aria-expanded="false" aria-controls="collapseFind6">
    Assembly submission
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseFind6">
  <div class="card card-body">
    <span>
        <ul>
            <li>ENA's documentation on <a href="https://ena-docs.readthedocs.io/en/latest/submit/assembly/genome.html" target="_blank">Submitting Genome Assemblies of Individuals or Cultured Isolates</a>.</li>
            <li>The only way to submit assemblies is by using the tool called Webin-CLI, hence the first step is to download the latest version, see ENA's documentation on <a href="https://ena-docs.readthedocs.io/en/latest/submit/general-guide/webin-cli.html" target="_blank">Webin-CLI Submission</a>. This tutorial will use Java jar, but a Docker image is also available.</li>
            <li>Webin-CLI requires that the metadata is formatted in a manifest file, hence create <a href="/files/ena_tutorial/Alectoris-graeca-manifest.txt">Alectories-graeca-manifest.txt</a>.</li>
            <li>Note that in order to submit a chromosome level assembly, a gzipped file listing the chromosomes is also needed. An example of what they look like is in <a href="/files/ena_tutorial/chromosome_list.txt">chromosome_list.txt</a>. We will also submit a <a href="/files/ena_tutorial/unlocalised_list.txt">unlocalised_list.txt</a>, which contains a list of unlocalised sequences.</li>
            <li>Webin-CLI can be used in two steps, first to validate and, upon successful validation, to submit:
<div class="clipboard">
    <button class="clipboard-button copy-button" type="button">
        <img class="clipboard-icon" src="/img/icons/copy.svg" alt="Copy to clipboard icon">
    </button>
    <button class="clipboard-button copied-button" type="button" style="display: none;">
        <img class="clipboard-icon" src="/img/icons/check.svg" alt="Copy to clipboard icon">
    </button>
</div>
<pre><code>
java -jar ~/webin-cli-8.2.0.jar -ascp -context genome -userName Webin-XXXXX -password 'YYYYY' -manifest ./Alectoris-graeca-manifest.txt -validate -test
<br></code></pre>
<div class="clipboard">
    <button class="clipboard-button copy-button" type="button">
        <img class="clipboard-icon" src="/img/icons/copy.svg" alt="Copy to clipboard icon">
    </button>
    <button class="clipboard-button copied-button" type="button" style="display: none;">
        <img class="clipboard-icon" src="/img/icons/check.svg" alt="Copy to clipboard icon">
    </button>
</div>
<pre><code>
java -jar ~/webin-cli-8.2.0.jar -ascp -context genome -userName Webin-XXXXX -password 'YYYYY' -manifest ./Alectoris-graeca-manifest.txt -submit -test
</code></pre>
            </li>
            <li><b>Note:</b> The <code>-test</code> indicates that the submission will be made to the test instance. Omit this when doing real submissions.</li>
            <li> Upon a successful submission, an accession starting with ERZ will be obtained. However, this is not the official accession to be used in a publication. ENA will need to process the assembly, and when this is done you will receive an email with the genome assembly accession to be used (GCA_xxxxxx), e.g.: 
<pre><code>
    ASSEMBLY_NAME | ASSEMBLY_ACC  | STUDY_ID   | SAMPLE_ID   | CONTIG_ACC                      | SCAFFOLD_ACC | CHROMOSOME_ACC
    bAleGra1.1    | GCA_965278835 | PRJEB79727 | ERS17759205 | CBDIHD010000001-CBDIHD010000076 |              | OZ257071-OZ257110
<br></code></pre>
            </li>
        </ul>
    </span>
  </div>  
  <br>
</div>

### Programmatic Submission Method
This method requires the preparation of XML files that are sent to ENA using cURL (or uploading them via the Webin Portal of ENA). It is possible to register and submit **studies**, **samples**, and **raw reads** this way. This is the **only** way to register **umbrella** studies.

Any programmatic submission requires two .xml files, one with the action (ADD, MODIFY, RELEASE, CANCEL) and one with the metadata. The submission is done via a cURL command in a terminal window, and all levels (study, sample, raw reads) can be registered and submitted at the same time, but in this tutorial the levels will be submitted separately.

#### Test submission
ENA provides two sites for submission; one for test submissions (`https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/`) and one for 'real' submissions (i.e. an actual submission to ENA) (`https://www.ebi.ac.uk/ena/submit/drop-box/submit/`). We recommend doing a test submission first, using the example data provided, in order to get an understanding of the different steps. <b>Note:</b> The test service is purged every 24 h, meaning that any submitted test file will be removed before the following day, making it impossible to begin a submission one day and continue the next.

<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseFind5a" role="button" aria-expanded="false" aria-controls="collapseFind5a">
    Register studies
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseFind5a">
  <div class="card card-body">
    <span>
        <ul>
            <li>ENA's documentation on <a href="https://ena-docs.readthedocs.io/en/latest/submit/study/programmatic.html" target="_blank">Register a study programmatically</a>.</li>
            <li>Create the action .xml, <a href="/files/ena_tutorial/submission.xml">submission.xml</a>, and update the desired release date. It can be set to maximum two years forward in time, and be adjusted later on. You will get a notification email from ENA, a few weeks prior to the release date, when your data is about to become public.</li>
            <li>Create the metadata .xml, <a href="/files/ena_tutorial/Alectoris-graeca-study.xml">Alectoris-graeca-study.xml</a>, with the names, titles, and descriptions of the raw reads study and the assembly study. Note that there is an <code>alias</code> added to each of the studies, <code>bAleGra-study-raw-reads</code> and <code>bAleGra1-study-assembly</code>. These are used in the submission of experiment and assembly, respectively, to be able to refer to which study they should be submitted to. This is handy if you want to submit all levels of metadata in the same cURL command, since you wouldn't know the accession number of the project at that point.</li>
            <li>Submit in a terminal window by typing:
<div class="clipboard">
    <button class="clipboard-button copy-button" type="button">
        <img class="clipboard-icon" src="/img/icons/copy.svg" alt="Copy to clipboard icon">
    </button>
    <button class="clipboard-button copied-button" type="button" style="display: none;">
        <img class="clipboard-icon" src="/img/icons/check.svg" alt="Copy to clipboard icon">
    </button>
</div>
<pre><code>
curl -u username:password -F "SUBMISSION=@submission.xml" -F "PROJECT=@Alectoris-graeca-study.xml" "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"
<br></code></pre>
            </li>
            <li>A receipt will be written in the window, with <code>success="true"</code> or <code>success="false"</code>. If true you will get the accession numbers, note these down in the .xlsx file. An example receipt:
<pre><code>
    &lt;?xml version="1.0" encoding="UTF-8"?&gt;
    &lt;?xml-stylesheet type="text/xsl" href="receipt.xsl"?&gt;
    &lt;RECEIPT receiptDate="2024-09-05T08:24:23.589+01:00" submissionFile="submission.xml" success="true"&gt;
        &lt;PROJECT accession="PRJEB79726" alias="bAleGra-study-raw-reads" status="PRIVATE" holdUntilDate="2025-05-10Z"&gt;
            &lt;EXT_ID accession="ERP163841" type="study"/&gt;
        &lt;/PROJECT&gt;
        &lt;PROJECT accession="PRJEB79727" alias="bAleGra1-study-assembly" status="PRIVATE" holdUntilDate="2025-05-10Z"&gt;
            &lt;EXT_ID accession="ERP163842" type="study"/&gt;
        &lt;/PROJECT&gt;
        &lt;SUBMISSION accession="ERA30781837" alias="SUBMISSION-05-09-2024-08:24:23:241"/&gt;
        &lt;MESSAGES&gt;
            &lt;INFO&gt;All objects in this submission are set to private status (HOLD).&lt;/INFO&gt;
        &lt;/MESSAGES&gt;
        &lt;ACTIONS&gt;ADD&lt;/ACTIONS&gt;
        &lt;ACTIONS&gt;HOLD&lt;/ACTIONS&gt;
    &lt;/RECEIPT&gt;
<br></code></pre>
            </li>
        </ul>
    </span>
  </div>
  <br>
</div>
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseFind5b" role="button" aria-expanded="false" aria-controls="collapseFind5b">
    Register samples
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseFind5b">
  <div class="card card-body">
    <span>
        <ul>
            <li>ENA documentation on <a href="https://ena-docs.readthedocs.io/en/latest/submit/samples/programmatic.html" target="_blank">Register samples programmatically</a>.</li>
            <li>Create the metadata .xml, <a href="/files/ena_tutorial/Alectoris-graeca-samples.xml">Alectoris-graeca-samples.xml</a>, for the four samples.</li>
            <li>As with the study, a submission.xml is needed. We can reuse the one already created, but the HOLD action will not have any effect since all samples are private 'forever' unless an experiment refers to it. The sample will become public the same time as the experiment becomes public.</li>
            <li>Register in a terminal window by typing:
<div class="clipboard">
    <button class="clipboard-button copy-button" type="button">
        <img class="clipboard-icon" src="/img/icons/copy.svg" alt="Copy to clipboard icon">
    </button>
    <button class="clipboard-button copied-button" type="button" style="display: none;">
        <img class="clipboard-icon" src="/img/icons/check.svg" alt="Copy to clipboard icon">
    </button>
</div>
<pre><code>
curl -u username:password -F "SUBMISSION=@submission.xml" -F "SAMPLE=@Alectoris-graeca-samples.xml" "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"
<br></code></pre>
            </li>
            <li>Upon success of the submission, each sample will obtain a BioSample accession (starting with SAMEA) and one internal ENA accession (starting with ERS).</li>
            </li>
        </ul>
    </span>
  </div>
  <br>
</div>
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseFind5c" role="button" aria-expanded="false" aria-controls="collapseFind5c">
    Submit raw reads
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseFind5c">
  <div class="card card-body">
    <span>
        <ul>
            <li>ENA's documentation on <a href="https://ena-docs.readthedocs.io/en/latest/submit/reads/programmatic.html" target="_blank">Submit raw reads programmatically</a>.</li>
            <li>Two metadata .xml files are needed in order to submit raw reads, one each for the experiments the runs.</li>
            <li>Create <a href="/files/ena_tutorial/Alectoris-graeca-experiments.xml">Alectoris-graeca-experiments.xml</a> and <a href="/files/ena_tutorial/Alectoris-graeca-runs.xml">Alectoris-graeca-runs.xml</a></li>
            <li>A note on <code>alias</code>. We have created aliases for both studies and samples, which is not necessary if one submits each metadata object separately, because then <code>refname=""</code> can be replaced by <code>accession=""</code> and the accessions received in previous steps can be added. However, when it comes to submission of raw reads, we will submit both objects at the same time and thus we don't yet know what the experiment accessions will be. For the experiment aliases, we will use a combination of the sample alias and the library name, and the run aliases are named with the experiment alias and the respective file type as an addition at the end.</li>
            <li>As in the previous step, the submission.xml created for the study will be reused also here.</li>
            <li>Submit in a terminal window by typing:
<div class="clipboard">
    <button class="clipboard-button copy-button" type="button">
        <img class="clipboard-icon" src="/img/icons/copy.svg" alt="Copy to clipboard icon">
    </button>
    <button class="clipboard-button copied-button" type="button" style="display: none;">
        <img class="clipboard-icon" src="/img/icons/check.svg" alt="Copy to clipboard icon">
    </button>
</div>
<pre><code>
curl -u username:password -F "SUBMISSION=@submission.xml" -F "EXPERIMENT=@Alectoris-graeca-experiments.xml" -F "RUN=@Alectoris-graeca-runs.xml" "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"
<br></code></pre>
            </li>
            <li>Upon success of the submission, both experiments and runs will obtain accession numbers(starting with ERX and ERR, respectively). The run accessions will be used in the next step, assembly submission.</li>
        </ul>
    </span>
  </div>
  <br>
</div>
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseFind5d" role="button" aria-expanded="false" aria-controls="collapseFind5d">
    Umbrella submission
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseFind5d">
  <div class="card card-body">
    <span>
        <ul>
            <li>ENA's documentation on <a href="https://ena-docs.readthedocs.io/en/latest/faq/umbrella.html" target="_blank">Create an Umbrella Study</a>.</li>
            <li>Create a <a href="/files/ena_tutorial/submission-umbrella.xml">submission-umbrella.xml</a>, with the ADD action and an <a href="/files/ena_tutorial/umbrella.xml">umbrella.xml</a> where the two studies (one for the raw reads and one for the assembly) are added as children.</li>
            <li><b>Note:</b> Umbrella studies are automatically created with a release date two years ahead in time. A separate submission, with the action RELEASE, is done when it is time to make the umbrella public, see how in ENA's documentation <a href="https://ena-docs.readthedocs.io/en/latest/faq/umbrella.html#releasing-umbrella-studies" target="_blank">Releasing Umbrella Studies</a>.</li>
            <li>Register in a terminal window by typing:
<div class="clipboard">
    <button class="clipboard-button copy-button" type="button">
        <img class="clipboard-icon" src="/img/icons/copy.svg" alt="Copy to clipboard icon">
    </button>
    <button class="clipboard-button copied-button" type="button" style="display: none;">
        <img class="clipboard-icon" src="/img/icons/check.svg" alt="Copy to clipboard icon">
    </button>
</div>
<pre><code>
curl -u Username:Password -F "SUBMISSION=@submission.xml" -F "PROJECT=@umbrella.xml" "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"
<br></code></pre>
            </li>
            <li>Umbrella studies cannot be seen when you login to your account. Hence, it is even more important that you make sure that the term <code>success="true"</code> is present in the typed receipt, and that you note down the received accession number in your metadata .xlsx file.</li>
        </ul>
    </span>
  </div>
  <br>
</div>

## Terminology
<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseFind7" role="button" aria-expanded="false" aria-controls="collapseFind7">
    Data types
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseFind7">
  <div class="card card-body">
    <span>
        <ul>
            <li><b>'Raw' sequence data</b> - Sequence data that is obtained directly from a sequencing instrument (typically in FASTQ or BAM file format).</li>
            <li><b>Analysed sequence data</b> - Sequence data that has been processed in some way after being obtained from a sequencing instrument. Such data has been normalised, and perhaps also subject to other processing (e.g. removal of outliers, calculation of expression measurements, and statistical analyses). Another example of analysed data is genome assemblies.</li>
            <li><b>Metadata</b> - Description of the data that gives, at a minimum, sufficient information to reproduce the data collection method (e.g. description of how the source material was obtained and details about the sequencing process, such as library preparation and instruments used).</li> 
        </ul>
    </span>
  </div>  
  <br>
</div>

<p>
  <button class="btn btn-expandable" data-bs-toggle="collapse" href="#collapseFind8" role="button" aria-expanded="false" aria-controls="collapseFind8">
    Metadata objects
    <i class="bi bi-chevron-double-down p-2"></i>
  </button>
</p>
<div class="collapse" id="collapseFind8">
  <div class="card card-body">
    <span>
    ENA recognises multiple 'levels'/'types' of metadata related to sequencing projects. These different 'levels'/'types' of metadata are represented by different metadata objects:
    <ul>
        <li><b>Study</b> - A study (project) object is used to group together all data submitted to ENA about a given study and to control its release date. A study accession number is typically used to cite data submitted to ENA. Note that all data and metadata associated with a study are made public together with the study when it is released.</li>
        <li><b>Sample</b> - A sample object contains information about the sequenced source material. Checklists are used to define which fields should be filled when describing samples. Note that a taxonomic classification system is used to refer to biological organisms; the accepted organism name and classification hierarchy are used, see <a href="https://doi.org/10.15468/avkgwm" target="_blank">The European Nucleotide Archive (ENA) taxonomy</a> for further details.</li>
        <li><b>Experiment</b> - An experiment object contains all the details about the metholodology used for sequencing, including library preparation protocols used and instrument details.</li>
        <li><b>Run</b> - A run object is part of an experiment object. It refers to data files that contain the raw reads.</li>
        <li><b>Analysis</b> - An analysis object contains secondary analysis results. These results are derived from the raw reads (e.g. a genome assembly).</li>
        </ul>
    </span>
  </div>
  <br>
</div>
<!-- likely should include the classic metadata model, or an updated version of it -->

## Resources
Please find below resources concerning ENA submission tutorial - in form of training, guidance and/or tools.

{{< resources-per-page-topics >}}

