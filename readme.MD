
# Scraping coronovirus data from worldometer

Scrapy spider code to extract covid-19 coronavirus outbreak.

**Usage:**

To crawl and download the table into a csv file, use the following command:

`scrapy crawl coronavirus -o corona.csv`

**Other:**

To generate the basic spider, use the following command

`scrapy genspider coronavirus "www.worldometers.info/coronavirus"
`

Troubleshooting the xpath and setup

`scrapy shell "www.worldometers.info/coronavirus"`
