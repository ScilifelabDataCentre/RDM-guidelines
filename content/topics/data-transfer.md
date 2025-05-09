---
title: Data transfer
category: Other
toc: True
---

# Data transfer
Quite often large amounts of data is generated, and it can be worth spending some time considering how to transfer data from the data producer to storage and analysis environment. Consider the capacity of the internet connection, transfer via a low bandwith network can be so time-consuming that it might be faster and easier to send the data on a hard drive through carrier services.

## SciLifeLab Data Delivery System
The Data Delivery System (DDS) is a cloud-based system for the delivery of data from SciLifeLab platforms to their users. It consists of a command line interface (CLI) and a web interface. This system is e.g. used by the National Genomics Infrastucture (NGI) for delivers of sequencing data.

<div>
  <ul>
    <li><a href="https://delivery.scilifelab.se/">DDS homepage</a></li>
    <li><a href="https://scilifelabdatacentre.github.io/dds_cli/">DDS documentation</a></li>
    <li><a href="https://ngisweden.scilifelab.se/resources/data-delivery-dds/">NGI guide on DDS</a></li>
  </ul>
</div>

## Uppmax

Please find below some useful links from the compute resource Uppmax regarding data transfer:

<div>
  <ul>
    <li><a href="https://docs.uppmax.uu.se/cluster_guides/transfer_rackham/">File transfer to/from Rackham</a></li>
     <li><a href="https://docs.uppmax.uu.se/cluster_guides/transfer_bianca/">File transfer to/from Bianca</a></li>
    <li><a href="https://scilifelabdatacentre.github.io/dds_cli/installation/#bianca">NAISS-SENS Bianca Deliver user guide for NGI data</a></li>
  </ul>
</div>

### Using Aspera on Uppmax

Aspera  (ascp) is a command-line transfer program that can be used for stable transfers of files e.g. from Uppmax to ENA (European Nucleotide Archive) upload area when doing submission. Aspc gives the user many options (use command `ascp --help`), below is an example where a set of fastq files will be uploaded to a subfolder at ENA:

1. Open a terminal window and log in to Uppmax using your credentials:  
    ```
    ssh -X username@rackham.uppmax.uu.se
    ```
1. Use <a href="https://docs.uppmax.uu.se/cluster_guides/interactive_more/" target="_blank">interactive</a> mode in order to execute the transfer at a compute node using a compute project:  
    ```
    interactive -A project-name
    ```
1. In order to be able to use the ascp command, it needs to be activated by typing:  
    ```
    module load ascp
    ```
1. Aspera has an environment variable that you can use in order to add your password at the remote/receiving site (in this case ENA) to memory, so you don't have to type it when executing the transfer command:  
    ```
    export ASPERA_SCP_PASS='my-ENA-password'
    ```
1. The command below will copy all fastq.gz files found in all subfolders under 'path-to-uppmax-folder' to the user 'Webin-XXXXX' (exchange to your login-name at ENA) upload area at ENA under subfolder 'subfolder-at-ENA' (which will be created if it doesn't already exist):  
    ```
    ascp --file-checksum=md5 -d -k 3 --mode=send --overwrite=always -QT -l300M --host=webin.ebi.ac.uk --user=Webin-XXXXX path-to-uppmax-folder/**/*.fastq.gz subfolder-at-ENA
    ```

Note: In order to check the progress and outcome of the transfer, a program such as FileZilla can be used to connect to your upload area at ENA from your local computer.

<a class="link-teal" href="https://ena-docs.readthedocs.io/en/latest/submit/fileprep/upload.html" target="_blank"><b>Learn more about uploading files to ENA <i class="bi bi-box-arrow-up-right"></i></b></a>

<a class="link-teal" href="https://download.asperasoft.com/download/docs/ascp/3.5.2/html/dita/ascp_usage.html" target="_blank"><b>Learn more about the ascp command <i class="bi bi-box-arrow-up-right"></i></b></a>

## Transferring files using RClone
RClone is a command-line program that can be used to transfer files across a wide range of protocols. This can be useful when you you are unable to use specialised submission tools or Aspera, for example when transfering files in bulk to <a href="https://www.scilifelab.se/data/repository/" target="_blank">SciLifeLab Data Repository</a> over the FTPS protocol.

The following example describes how to upload files to SciLifeLab Data Repository (or any other FigShare repository):

1. Find/create your username and password for ftp uploads to Figshare
1. To configure your <a href="https://rclone.org/ftp/" target="_blank">ftp connection parameters for rclone</a> your command will look something like this (`rclone lfs :ftp:data` will list the content of your data uploads folder on FigShare):
   ```
   rclone lsf :ftp:data --ftp-host=ftps.figshare.com --ftp-user=$user --ftp-pass=$(rclone obscure $pass) --ftp-port=21 --ftp-explicit-tls
   ```
1. Use `rclone copy path/to/localfile :ftp:data/new-data-item-title-folder` to upload (use the same configuration flags as above)

<a class="link-teal" href="https://rclone.org/docs/" target="_blank"><b>Learn more about RClone <i class="bi bi-box-arrow-up-right"></i></b></a>

<a class="link-teal" href="https://help.figshare.com/article/upload-large-datasets-and-bulk-upload-using-the-ftp-uploader-desktop-uploader-or-api" target="_blank"><b>Learn more about ftp uploads to FigShare <i class="bi bi-box-arrow-up-right"></i></b></a>

## Resources
Please find below resources concerning data transfer in form of training, guidance and/or tools.

{{< resources-per-page-topics >}}
