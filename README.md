<h1 align="center">Simple Python email scraper</h1>

<br>

<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <img src="https://img.shields.io/badge/python3-blue.svg" />
<a href="https://github.com/JRPerezJr/Simple-python-email-scraper/blob/main/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

<br>

> A Python information gathering tool.

## Demo
![email-scraper-app](https://user-images.githubusercontent.com/19915910/152496409-bb42a3ef-fadf-4ff3-abf3-c8f3a565766d.png)

## 📐 Prerequisites

- Git
- Python3
- Docker (To run as a container)

## 🛠 Install and Run Locally

Clone the project

```shell
  git clone https://github.com/JRPerezJr/Simple-python-email-scraper.git
```

Go to the project directory

```shell
  cd Simple-python-email-scraper
```

Install dependencies with pip if needed

```shell
pip install -r requirements.txt
```
Make the file executable with
```shell
chmod +x email_scraper.py
#or
sudo chmod +x email_scraper.py
```

## 👩‍💻 👨‍💻 Usage

Run with 
```shell
./email_scraper.py
#or
python3 email_scraper.py
```
Run anywhere with Docker
```shell
 docker run -it --rm --name email_scraper jperezdevinjp/python_email_scraper
```
<br>

> Then enter the domain name 
> Ex. `https://example.com`
> The program will search all the links for email addresses and print it out in the console.
> This program was tested on Kali Linux running Python 3.9.9


## 📓 Author

![Logo](https://user-images.githubusercontent.com/19915910/120965966-81203b00-c7a0-11eb-8ef4-a42c0642db4c.png)

- Github: [@JRPerezJr](https://github.com/JRPerezJr)
- LinkedIn: [@devjperez](https://linkedin.com/in/devjperez)

## 📝 License
This project is [MIT](https://github.com/JRPerezJr/Simple-python-email-scraper/blob/main/LICENSE) licensed.