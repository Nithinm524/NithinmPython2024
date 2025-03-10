# -*- coding: utf-8 -*-
"""coviddatavisuaalization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KHsCbWEbK0AdJNFO27owv3xPA7SQKJOV

Data Visualization: Dynamic COVID-19 Graph
"""

import matplotlib.pyplot as plt
import requests

def get_covid_data(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["cases"], data["deaths"], data["recovered"]
    else:
        print("Error fetching data. Please check the country name.")
        return None

def visualize_data(country):
    data = get_covid_data(country)
    if data:
        labels = ["Cases", "Deaths", "Recovered"]
        plt.pie(data, labels=labels, autopct="%1.1f%%", colors=["orange", "red", "green"])
        plt.title(f"COVID-19 Statistics for {country.capitalize()}")
        plt.show()

country = input("Enter the country name: ")
visualize_data(country)