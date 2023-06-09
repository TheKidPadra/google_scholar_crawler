# google-scholar-crawler

<p align="center"><img width="auto" src="https://github.com/TheKidPadra/google_scholar_crawler/blob/main/Assets/Google_crawl_faster_FI.png" /></p>

This is the web crawler I have been developing to extract [Google Scholar](https://scholar.google.com/) articles for my bachelor's thesis. The purpose of this crawler is to gather data that will be utilized in my NLP model, allowing me to extract a context vector. This context vector will then be employed in my machine learning model for further analysis and processing.

>１. Record the title, year and URL ['title', 'year', 'url'] of the Paper on Google Search Page in CSV file format.
>
>２. Download links with tags (e.g. [PDF], [HTML]) from Google Search Page as PDF files

## Get Started

>This software application is designed for Mac and runs on Python 3.9.13. It utilizes various libraries, including requests, BeautifulSoup, and pdfkit. To ensure smooth installation, it is recommended to use pip for the installation process.
>Prior to installing pdfkit, it is necessary to download wkhtmltopdf. Please ensure that you have obtained the appropriate version of wkhtmltopdf from the provided link before proceeding with the installation.

Initially, please clone this repository.

```
$ git clone https://github.com/TheKidPadra/google_scholar_crawler.git
```

## Instruction

### 1. Go to [Google Scholar Search](https://scholar.google.com/)

Please input the desired keywords into the designated field. Next, navigate to the first page of the Search Results and proceed to copy the URL of that specific page.

![](https://github.com/TheKidPadra/google_scholar_crawler/blob/main/Assets/GS.png)

### 2. Enter google_crawler.py

Put the copied URL into start_url, start_url = "url"

![](https://github.com/TheKidPadra/google_scholar_crawler/blob/main/Assets/google_crawler_py(v2).png)

### 3. p_key: puts the keyword you want to find, n_key: puts the keyword you don't want to find

In the Search Page, if the title and content of each cell contain the word p_key, Crawler will tend to crawl this Paper

In Search Page, if the title and content of each cell contain the word n_key, Crawler will tend to ignore this paper.

![](https://github.com/TheKidPadra/google_scholar_crawler/blob/main/Assets/google_crawler_py.png)

In the above picture, because I want to find emotion detection related articles, not signal nor voice related articles, so I put the word related to emotion identificayion in p_key,and put the word related to voice/signal in n_key.

### 4. set page = number, you can set the number of pages to crawl Google Search Page

![](https://github.com/TheKidPadra/google_scholar_crawler/blob/main/Assets/google_crawler_py(v3).png)

Set too many pages will induce Google's robot check

### 5. start executing the program

Run google_crawler.py in Terminal

```
$ python3 google_crawler.py
```

The data captured ('title', 'year', 'url',...) will be in the result.pickle

Then, run csvNdownload.py in Terminal

```
$ python3 csvNdownload.py
```

Convert data to CSV file and store in CSV folder

Download links with Tag (PDF, HTML) to PDF files and store them in PDF, HTML folders respectively.

## Google Robot Check

Google's Search Page incorporates anti-crawler detection mechanisms, and excessive downloading or rapid web page access can raise suspicions of automated robot activity, potentially leading to IP address bans.

The easiest way to use a VPN is to use a VPN to change your IP address immediately when you are thought to be a robot.

Now there are many free VPNs on the Internet that can be downloaded

If a message appears while running Crawler

```
__findPages - Can not find the pages link in the start URL!!
__findPages - 1.Google robot check might ban you from crawling!!
__findPages - 2.You might not crawl the page of google scholar

```

In the event that you encounter a message like above during the crawler execution that indicates the presence of this issue, employing a VPN and switching IP addresses is an advisable solution. Alternatively, you can consider defining an IP pool or implementing a DHCP server to facilitate dynamic IP changes during the crawling process, thereby mitigating the risk of IP blocks.
