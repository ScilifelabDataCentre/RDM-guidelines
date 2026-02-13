---
title: Data transfer
category: Other
tags: ["scilifelab data delivery system","DDS","Uppmax","Dardel","aspera","ascp","aspera-cli","rclone"]
toc: True
---

# Data transfer
Quite often large amounts of data is generated, and it can be worth spending some time considering how to transfer data from the data producer to storage and analysis environment. Consider the capacity of the internet connection, transfer via a low bandwith network can be so time-consuming that it might be faster and easier to send the data on a hard drive through carrier services.

## SciLifeLab Data Delivery System
The Data Delivery System (DDS) is a cloud-based system for the delivery of data from SciLifeLab platforms to their users. It consists of a command line interface (CLI) and a web interface. This system is e.g. used by the National Genomics Infrastucture (NGI) for deliveries of sequencing data.

<div>
  <ul>
    <li><a href="https://delivery.scilifelab.se/">DDS homepage</a></li>
    <li><a href="https://scilifelabdatacentre.github.io/dds_cli/">DDS documentation</a></li>
    <li><a href="https://ngisweden.scilifelab.se/resources/data-delivery-dds/">NGI guide on DDS</a></li>
  </ul>
</div>

## Data transfer using Aspera

[Aspera CLI](https://github.com/IBM/aspera-cli/) (ascli) is a command-line interface for IBM Aspera products. As part of this client, there is a transfer tool `ascp` that can be used for stable transfers of files e.g. from Uppmax (or your own computer) to ENA (European Nucleotide Archive) upload area when doing submission. The main advantages over e.g. using `lftp` is that it is faster and can resume transfer if a connection breaks instead of having to start from the beginning.

[Installation](https://github.com/IBM/aspera-cli/?tab=readme-ov-file#install) of `ascp` is done in two steps, using [Ruby](https://github.com/IBM/aspera-cli/blob/main/docs/README.md#ruby) (version 3.1 or higher):

  ```
  gem install aspera-cli
  ascli config transferd install
  ```

There are many [ascp options](https://www.ibm.com/docs/en/ahts/4.4.x?topic=line-ascp-command-reference#ascp_usage__title__6), and it can be a bit confusing to know which ones to use. The command below will copy all .fastq.gz files found in all subfolders under 'path-to-uppmax-folder' to the user 'Webin-XXXXX' (exchange to your login-name at ENA) upload area at ENA under subfolder 'subfolder-at-ENA' (which will be created if it doesn't already exist):  

  ```
  ascp --file-checksum=md5 -d -k 3 --mode=send --overwrite=always -QT -l300M --host=webin.ebi.ac.uk --user=Webin-XXXXX path-to-uppmax-folder/**/*.fastq.gz subfolder-at-ENA
  ```

Aspera has an environment variable that you can use in order to add your password at the remote/receiving site (in this case ENA) to memory, so you don't have to type it when executing the transfer command:  
    ```
    export ASPERA_SCP_PASS='my-ENA-password'
    ```

**Note:** In order to check the progress and outcome of the transfer, a program such as FileZilla can be used to connect to your upload area at ENA from your local computer.

<a class="link-teal" href="https://ena-docs.readthedocs.io/en/latest/submit/fileprep/upload.html" target="_blank"><b>Learn more about uploading files to ENA <i class="bi bi-box-arrow-up-right"></i></b></a>

### Install Aspera on Uppmax

1. On Uppmax, we already have ruby installed so it is a matter of loading the module, then installing and adding paths to .bashrc:  
    ```
    module load ruby
    gem install aspera-cli
    echo 'export PATH="$PATH:/home/username/.gem/ruby/3.4.0/bin"' >> ~/.bashrc
    source ~/.bashrc
    ascli --version
    ascli conf ascp install
    ascli conf ascp info
    echo 'export PATH="$PATH:/home/username/.aspera/sdk"' >> ~/.bashrc
    source ~/.bashrc
    ascp --help
    ```

* **Note:** For other options of data transfer on Uppmax, please see:

  <div>
    <ul>
      <li><a href="https://docs.uppmax.uu.se/cluster_guides/transfer_pelle/" target="_blank">File transfer to/from Pelle</a></li>
      <li><a href="https://docs.uppmax.uu.se/cluster_guides/transfer_bianca/" target="_blank">File transfer to/from Bianca</a></li>
      <li><a href="https://scilifelabdatacentre.github.io/dds_cli/installation/#bianca" target="_blank">NAISS-SENS Bianca Deliver user guide for NGI data</a></li>
    </ul>
  </div>

### Install Aspera on Dardel

* There is an Aspera client available via command `ml aspera-cli/3.9.6.1467.159c5b1`. Note: Command `ml avail aspera-cli` lists the available versions

* However, newer versions of Aspera exist, and can be installed locally on Dardel:

    ```
    curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash
    source ~/.bashrc
    rbenv install 3.2.2
    rbenv global 3.2.2
    gem install aspera-cli
    echo 'export PATH="$PATH:/home/username/.gem/ruby/3.4.0/bin"' >> ~/.bashrc
    source ~/.bashrc
    ascli --version
    ascli conf ascp install
    ascli conf ascp info
    echo 'export PATH="$PATH:/home/username/.aspera/sdk"' >> ~/.bashrc
    source ~/.bashrc
    ascp --help
    ```

    **Note:** The instructions only works if you are in a bash shell. If in doubt run `echo $0` and if it doesn't reply with `bash` then type `bash` to change. Also, in case you don't have a file named `.bashrc` in your home directory, you can instead type `source ~/.bash_profile`.

* **Note:** For other options of data transfer on Dardel:
  * Dardel has multiple ways of transferring files to and from your local machine, see documentation on the <a href="https://support.pdc.kth.se/doc/data_management/file_transfer/" target="_blank">PDC on File transfer</a>.
  * In the future, Dardel will have dedicated nodes for transferring large files, see further on <a href="https://support.pdc.kth.se/doc/data_management/data_management/#nodes-for-file-operations" target="_blank">Nodes for file operations</a>, but at the moment transfers can be done directly on login node (dardel.pdc.kth.se).


## Data transfer using RClone
Rclone is a command-line program that can be used to transfer files across a wide range of protocols. This can be useful when you you are unable to use specialised submission tools or Aspera, for example when transfering files in bulk to <a href="https://www.scilifelab.se/data/repository/" target="_blank">SciLifeLab Data Repository</a> over the FTPS protocol.

The following example describes how to upload files to SciLifeLab Data Repository (or any other FigShare repository):

1. Find/create your username and password for FTP uploads to Figshare
1. To configure your <a href="https://rclone.org/ftp/" target="_blank">FTP connection parameters for rclone</a> your command will look something like this (`rclone lfs :ftp:data` will list the content of your data uploads folder on FigShare):
   ```
   rclone lsf :ftp:data --ftp-host=ftps.figshare.com --ftp-user=$user --ftp-pass=$(rclone obscure $pass) --ftp-port=21 --ftp-explicit-tls
   ```
1. Use `rclone copy path/to/localfile :ftp:data/new-data-item-title-folder` to upload (use the same configuration flags as above)

<a class="link-teal" href="https://rclone.org/docs/" target="_blank"><b>Learn more about RClone <i class="bi bi-box-arrow-up-right"></i></b></a>

<a class="link-teal" href="https://help.figshare.com/article/upload-large-datasets-and-bulk-upload-using-the-ftp-uploader-desktop-uploader-or-api" target="_blank"><b>Learn more about FTP uploads to FigShare <i class="bi bi-box-arrow-up-right"></i></b></a>

## About checksums
File checksums are used to validate that a file remains intact, with no loss, for example after a data transfer. Often when you submit data to a repository, you are required to add the checksums for your data files, so that the repository can verify that the files are intact. Typically the data producer will calculate checksums for the files, and make these part of the delivery. Most, if not all, operating systems include built-in, command line, tools to calculate checksums. If you want, or need, to calculate them yourself, follow these steps:

1. Open a terminal (command prompt) window and change to the directory where the files are located, e.g. `cd my_data/raw/`.
1. Modify and execute the command `md5sum * > checksums-md5.txt` to match your file names and required output name. 

The command will calculate the checksums for all files in current directory and list them in a file named `checksums-md5.txt`. Note that in macOS the calculator is called `md5` instead of `md5sum`.


## Resources
Please find below resources concerning data transfer in form of training, guidance and/or tools.

{{< resources-per-page-topics >}}
