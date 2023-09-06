---
title: Data transfer
contributors: []
toc: True
---

# Data transfer
Quite often large amounts of data is generated, and it can be worth spending some time considering how to transfer data from the data producer to storage and analysis environment. Consider the capacity of the internet connection, transfer via a low bandwith network can be so time-consuming that it might be faster and easier to send the data on a hard drive through carrier services.

## SciLifeLab Data Delivery System
The Data Delivery System (DDS) is a cloud-based system for the delivery of data from SciLifeLab platforms to their users. It consists of a command line interface (CLI) and a web interface. This system is e.g. used by the National Genomics Infrastucture (NGI) for delivers of sequencing data.

* [DDS homepage](https://delivery.scilifelab.se/)
* [DDS documentation](https://scilifelabdatacentre.github.io/dds_cli/)
* [NGI guide on DDS](https://ngisweden.scilifelab.se/resources/data-delivery-dds/)

## Uppmax

Please find below some useful links from the compute resource Uppmax regarding data transfer:

* [Basic SFTP commands for transferring files](https://uppmax.uu.se/support-sv/user-guides/basic-sftp-commands/)
* [NAISS-SENS Bianca Deliver user guide for NGI data](https://scilifelabdatacentre.github.io/dds_cli/installation/#bianca)
* [Transit user guide - secure data transfer of sensitive data](https://uppmax.uu.se/support-sv/user-guides/transit-user-guide/)

### Using Aspera on Uppmax

Aspera  (ascp) is a command-line transfer program that can be used for stable transfers of files e.g. from Uppmax to ENA (European Nucleotide Archive) upload area when doing submission (see further [ENA guide on using ascp](https://ena-docs.readthedocs.io/en/latest/submit/fileprep/upload.html?highlight=ascp#using-aspera-ascp-command-line-program)). Aspc gives the user many options (use command `ascp --help` or see e.g. [ascp command reference](https://download.asperasoft.com/download/docs/ascp/3.5.2/html/dita/ascp_usage.html)), below is an example where a set of fastq files will be uploaded to a subfolder at ENA:

1. Open a terminal window and log in to Uppmax using your credentials:  
  `ssh -X username@rackham.uppmax.uu.se`
1. Use [interactive](https://www.uppmax.uu.se/support/faq/running-jobs-faq/how-can-i-run-interactively-on-a-compute-node/) mode in order to execute the transfer at a compute node using a compute project:  
  `interactive -A project-name`
1. In order to be able to use the ascp command, it needs to be activated by typing:  
  `module load ascp`
1. Aspera has an environment variable that you can use in order to add your password at the remote/receiving site (in this case ENA) to memory, so you don't have to type it when executing the transfer command:  
  `export ASPERA_SCP_PASS='my-ENA-password'`
1. The command below will copy all fastq.gz files found in all subfolders under 'path-to-uppmax-folder' to the user 'Webin-XXXXX' (exchange to your login-name at ENA) upload area at ENA under subfolder 'subfolder-at-ENA' (which will be created if it doesn't already exist):  
  `ascp --file-checksum=md5 -d -k 3 --mode=send --overwrite=always -QT -l300M --host=webin.ebi.ac.uk --user=Webin-XXXXX path-to-uppmax-folder/**/*.fastq.gz subfolder-at-ENA`

Note: In order to check the progress and outcome of the transfer, a program such as FileZilla can be used to connect to your upload area at ENA from your local computer, see instructions at ENA on [Using FileZilla on Windows](https://ena-docs.readthedocs.io/en/latest/submit/fileprep/upload.html?highlight=filezilla#using-filezilla-on-windows).
