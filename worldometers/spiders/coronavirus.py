# -*- coding: utf-8 -*-
import scrapy

class CoronavirusSpider(scrapy.Spider):
    name = 'coronavirus'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/coronavirus/']

    def parse(self, response):
        countries = response.xpath("//table[@id = 'main_table_countries']/tbody/tr[not(contains(@class,'total_row'))]")
        for country in countries:
            row = country.xpath(".//td/text()").getall()
            N = len(row)
            i = 1
            country_name = row[0]
            if (row[0] == ' '):
                country_name = country.xpath(".//td/a/text()").get()
                if (country_name == None):
                    country_name = country.xpath(".//td/span/text()").get()
                i = 2
            total_cases = row[i]
            new_cases = row[i+1]
            total_deaths = row[i + 2]
            new_deaths = row[i + 3]
            total_recovered = row[i+4]
            active_cases = row[i+5]
            critical = row[i+6]
            #have to put the below condition because Diamond Pricess row was giving an issue
            if (i+7 < N):
                tot_per_mill = row[i+7]
            else:
                tot_per_mill =''
            yield{
                "country": country_name,
                "total_cases":total_cases,
                "new_cases":new_cases,
                "total_deaths":total_deaths,
                "new_deaths":new_deaths,
                "total_recovered":total_recovered,
                "active_cases":active_cases,
                "critical":critical,
                "tot_per_mill":tot_per_mill
            }
        total_row = response.xpath("//table[@id = 'main_table_countries']/tbody/tr[(contains(@class,'total_row'))]")