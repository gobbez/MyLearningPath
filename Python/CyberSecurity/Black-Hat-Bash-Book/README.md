# Black Hat Bash - Book
**Black Hat Bash** is a great book, written by D. Farhi and N. Aleks, about penetration testing with Bash and Kali Linux. A guide that follows you from basic to advanced topics.

![alt text](book.jpg "Black Hat Bash")


### Table of Contents
- [Chapter 1. The Bash Shell](#chapter-1-the-bash-shell)
- [Chapter 2. Flux control and text elaboration](#chapter-2-flux-control-and-text-elaboration)
- [Chapter 3. Creation of hacking laboratory](#chapter-3-creation-of-hacking-laboratory)
- [Chapter 4. Recognition](#chapter-4-recognition)
- [Chapter 5. Vulnerability Scanner and Fuzzing](#chapter-5-vulnerability-scanner-and-fuzzing)
- [Chapter 6. Acquire a Web Shell](#chapter-6-acquire-a-web-shell)
- [Chapter 7. Reverse Shell](#chapter-7-reverse-shell)
- [Chapter 8. Local Information Gathering](#chapter-8-local-informations-gathering)
- [Chapter 9. Escalation Of Privileges](#chapter-9-escalation-of-privileges)
- [Chapter 10. Persistency](#chapter-10-persistency)
- [Chapter 11. Network Survery and Lateral Movements](#chapter-11-network-survey-and-lateral-movements)
- [Chapter 12. Defenses Elusion and Exfiltration](#chapter-12-defenses-elusion-and-exfiltration)


## Step-By-Step Learning

### Chapter 1. The Bash Shell

This first chapter starts with an introduction of the Bash Shell with its common methods. 
<br>
The book teaches how to create scripts with various functions (like receive input or writing in the files).
<br>
At the end of the chapter there is a simple exercise.
<br>
You can find some exercises in 

[Files/Chapter1](files/chapter1)

<br>

### Chapter 2. Flux control and text elaboration

This chapter explains different type of loops (while, until, for) and conditions.
<br>
Using operators and conditions to create efficient loops and save results to files or modify them.
<br>
One exercise provided some IPs to filter, extract and modify.
<br>
As always, there are lots of Bash exercises to do, that you can find in:

[Files/Chapter2](files/chapter2/)

<br>

### Chapter 3. Creation of hacking laboratory

Here the books shows us how to instal **Docker**, **Kali Linux** and a fictional network with 8 machine (4 public and 4 private).
<br>
We will use these machines for our training in the following chapters.
<br>
The book lets us install different tools that aren't already available in Kali Linux. 
<br>
Here's a list of tools installed:
<li>Dirsearch</li>
<li>Gitjacker</li>
<li>LinEnum</li>
<li>LinuxExploitSuggester2</li>
<li>Nuclei</li>
<li>Pwncat</li>
<li>RustScan</li>
<li>unix-privesc-check</li>
<li>WhatWeb</li>

<br>

### Chapter 4. Recognition

This chapter lets us create some interesting script to extract information of our target network, such as:
<li>ip info</li>
<li>ping hosts</li>
<li>watchdog script</li>
<li>os info</li>
<li>server info</li>
<br>
There are plenty of exercises to do, where every script is found here:

[Files/Chapter4](files/chapter4/)

<br>

### Chapter 5. Vulnerability Scanner and Fuzzing

In this super interesting chapter we continued to explore our test-network and the book guided us to create scripts for our sessions.
<br>
We used different tools to discover vulnerabilities and extracting some informations, urls and even downloading files.
<br>
The tools that we have used are:
<li>Nikto: A web server scanner</li>
<li>Nmap: Network Mapper — the Swiss army knife of network scanning.</li>
<li>Nuclie: A fast, customizable vulnerability scanner powered by YAML templates.</li>
<li>Wfuzz: A web fuzzer.</li>
<li>Wget: A command-line tool to download files from the web.</li>

<br>
You can find the scripts here:

[Files/Chapter5](files/chapter5/)

<br>

### Chapter 6. Acquire a Web Shell

In this chapter we see different techniques and tools to try to install a web shell in our target.
<br>
We used the BurpSuite tool to add another app.py file to overwrite the current one in order to make us create and use a web shell.
<br>
Then, we managed to execute some bash code directly into our target-server.

<br>
You can find some scripts here:

[Files/Chapter6](files/chapter6/)

<br>

### Chapter 7. Reverse Shell

This chapter shows some common methods to enable reverse-shell, meaning to connect the target to our machine so that we can use it back (reverse shell).
<br>
In the chapter there is also an exercise to brute force a ssh (on our test server) and we managed to find the right combination of credentials.

<br>
Some scripts here:

[Files/Chapter7](files/chapter7)

<br>

### Chapter 8. Local Informations Gathering

This chapter showed many arguments on local settings, commands, planned scripts and so on.

<br>

[Files/Chapter8](files/chapter8)


<br>

### Chapter 9. Escalation Of Privileges

In this chapter we have learned what is privileges escalation, how to change autorizations in the settings, search files by autorizations.
<br>
We have created a script for brute-force a password and to exploit sudo configurations.
<br>
The book explained GTFOBins, its functions and how to create a search method with it.

<br>

[Files/Chapter9](files/chapter9)

<br>

### Chapter 10. Persistency

This chapter explains how to keep persistency in the network in order to mantain access and control.
<br>
It showed different ways to mantain access and their risks and we programmed a script to create a fake sudo that can give us passwords and control.

<br>

[Files/Chapter10](files/chapter10)

<br>

### Chapter 11. Network Survey and Lateral Movements

In this chapter we have seen different methods to gain access to other machines using a machine where we had access.
<br>
We have also seen some scripts and tools to gain access of databases.

<br>

[Files/Chapter11](files/chapter11)

<br>

### Chapter 12. Defenses Elusion and Exfiltration

In this last chapter we have seen some common tools and methods to find and block suspicious activities. 
<br>
We have seen some methods to try to mask or render invisible our attacking methods. 

<br>

[Files/Chapter12](files/chapter12)