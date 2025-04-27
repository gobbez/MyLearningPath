# Chapter 1 - Assessment Methodologies Information Gathering

The first chapter explains Passive and Active Information Gathering.

## Types of gathering information
<li>Passive Gathering: Access to public information, either with browser (user experience) or general tools</li>
<li>Active Gathering: Gain insights on informations without using publicly available tools or methods (for example using bruteforce)</li>

## Passive Gathering Methods & Tools

<li>"website url"/robots.txt: file that may show informations</li>
<li>Command: host "website url": gain ip and other info</li>
<li>Command: whois "website url or ip": gain informations</li>
<li>Command: whatweb "website url": get info about server, ip, etc</li>
<li>HttTrack: download the website to analyze it's source code</li>
<li>NetCraft: gain informations like emails, operating system, technologies..</li>

### DNS recon

<li>DNSRecon: tool used to gain informations like email server, technologies, ips..</li>
You can use it with dnsrecon -d "website url"
<li>DNSDumpster: web tool to analyze a website and gain insights.</li>

### Firewall recon

<li>Wafw00f: a tool (you can find it on GitHub) to gain insights about the firewall of a website.</li>

### Subdomain enumeration 

<li>Sublist3r: a passive-gathering tool that gains access to the subdomains of a website. It will find every publicly available domains using search engines (like Google, etc).</li>
sublister -d "website url" -e "search engine(s)"
<li>Google Dorks: some google commands to find informations of a specific target.</li>
You can limit the Google search by targeting a specific website or url.
<br><br>
This will search for everything that starts with your search, thus searching for subdomains too.
<br>
<li>site:"browser search"  (example: site:ine.com will search for every url that has ine.com, like ine.com/blog etc)</li>

<br>
You can add the inurl to search for a specific argument inside the url.
<br>
<li>site:ine.com inurl:admin (this will search for every url that starts with ine.com and contains admin)</li>

<br>
You can search everything that ends with the url.
<br>
<li>site:*.ine.com (this will search for every url that finishes with ine.com, like courses.ine.com)</li>

<br>
You can use the intitle to search for a title.
<br>
<li>site:*.ine.com intitle:admin</li>

<br>
You can search by file types as well using filetype.
<li>site:*.ine.com filetype:pdf</li>

<br>
You can finish your "google query" with another search without commands
<li>site:ine.com courses</li>

<br>
Some easy methods to try to find some vulnerabilities such as websites that have shown passwords by error.
<li>inurl:auth_user_file.txt</li> 
<li>inurl:password.txt</li>

<br>
You can find many available Passive Gathering Google Dorks here:
<li>Google Hacking Database (exploit-db.com)</li>

### Website timemachine

You can see how a website looked years ago with the WayBack Machine (web.archive.org)

<br>

### Email Harvesting

TheHarvester is a tool for email enumerating.
<br>
This tool has both Passive and Active Gathering methods to search for vulnerable emails.
<li>theHarvester -d "website url" -b "google, linkedin" (-b is to search for a particular website platform)</li>

<br>

### Leaked Password Databases

There are different websites that allows to check if a password has been leaked from different websites.
<br>
Some of them are:
<li>haveibeenpwned.com</li>

<br>

## Active Gathering Methods and Tools

### DNS Zone Transfer

DNS (Domain Name System) is a protocol to resolve website names to ip addresses.
<li>dnsenum is a tool for active gathering, enumerating subdomains, providers, servers, files, etc</li>
<li>dig is another tool for active gathering</li>
<li>fierce is another tool, that can also enable brute force to find subdomains</li>

### Host Discovery with Nmap

Nmap is a tool for port-scanning and active information gathering. 
<br>
You can use it to search for subdomains of a website.
<br>
(Alternatively you can use Netdiscover, that does the same but using an ARP method instead)
<br>
<li>sudo nmap -sn "ip address": this command will show every ip address linked to a particolar ip</li>

### Port Scanning with Nmap

After you have discovered some ips of an host you can perform a port scanning, with Nmap tool.
<br>
To summarize, you can do:
<li>nmap "ip address": to scan the open ports of that ip (NB: if it's a Windows ip, sometimes you can use the nmap -Pn command instead)</li>
<li>nmap -p "port(s)" "ip address": optional to scan only certain port(s)</li>
<li>nmap -sV "ip address": scan the ports and their service version running</li>
<li>nmap -O "ip address": scan the operating system too</li>
<li>nmap -sC "ip address": scan more informations of the ports</li>
<li>nmap -T"number from 0 to 4" "ip address": scan faster or slower</li>
You can finish the command with -oN or -oX to save the results in a file (example a text) or a xml file.

### Gobuster

You can find a list of available urls with Gobuster.
<li>gobuster dir -u "website url" -w /usr/share/wordlists/dirb/common.txt</li>


### LAB 1

In the first lab we had to explore a website and gather informations. There were 5 "flags" to capture.
