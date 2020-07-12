#%%
from bs4 import BeautifulSoup
import requests
import re
import sys
import os
import calendar
import time
import rules


def main(path):
    # obtain html from website to txt
    htmlfile = open(path, "r", encoding="utf-8")
    htmlhandle = htmlfile.read()
    soup = BeautifulSoup(htmlhandle, "lxml")
    tr_all = soup.find_all("tr")

    passOr = []
    year_of_stay = []
    is_local_uni = []
    is_local_poly = []
    is_diploma = []
    is_bachelor = []
    is_master = []
    is_phd = []
    is_malaysian = []
    is_couple = []
    with_child = []
    salary = []
    is_ep = []

    for tr_all in tr_all:
        numOfSya = 0
        numOfSyb = 0
        profileatt = ""
        resultatt = ""
        for word in str(tr_all):
            if numOfSya == 18:
                if word == "/":
                    result = str(resultatt[:-1])
                    content = str(profileatt[:-1]).replace(" ", "")
                    if result == "通过" or result == "失败":
                        if rules.get_year_of_stay(content) == None:
                            break
                        elif int(str(rules.get_year_of_stay(content))) > 0:
                            if (
                                rules.is_local_poly(content) == 0
                                and rules.is_diploma(content) == 0
                                and rules.is_bachelor(content) == 0
                                and rules.is_master(content) == 0
                                and rules.is_phd(content) == 0
                            ):
                                break
                            else:
                                year_of_stay.append(
                                    str(rules.get_year_of_stay(content))
                                )
                                is_local_uni.append(str(rules.is_local_uni(content)))
                                is_local_poly.append(str(rules.is_local_poly(content)))
                                is_malaysian.append(str(rules.is_malaysian(content)))
                                is_couple.append(str(rules.is_couple(content)))
                                with_child.append(str(rules.with_child(content)))
                                is_ep.append(str(rules.is_ep(content)))
                                if result == "通过":
                                    passOr.append("1")
                                if result == "失败":
                                    passOr.append("0")
                                if str(rules.is_phd(content)) == "1":
                                    is_diploma.append("0")
                                    is_bachelor.append("0")
                                    is_master.append("0")
                                    is_phd.append(str(rules.is_phd(content)))
                                if str(rules.is_master(content)) == "1":
                                    is_diploma.append("0")
                                    is_bachelor.append("0")
                                    is_master.append(str(rules.is_master(content)))
                                    is_phd.append("0")
                                if str(rules.is_bachelor(content)) == "1":
                                    is_diploma.append("0")
                                    is_bachelor.append(str(rules.is_bachelor(content)))
                                    is_master.append("0")
                                    is_phd.append("0")
                                if str(rules.is_diploma(content)) == "1":
                                    is_diploma.append(str(rules.is_diploma(content)))
                                    is_bachelor.append("0")
                                    is_master.append("0")
                                    is_phd.append("0")

            if numOfSya == 15 & numOfSyb == 15:
                profileatt += word
                # print(profileatt)
            if numOfSya == 17 & numOfSyb == 17:
                resultatt += word
                # print(resultatt)
            if word == ">":
                numOfSyb += 1
            if word == "<":
                numOfSya += 1

    # 写入CSV
    from pandas import DataFrame

    DataSet = list(
        zip(
            year_of_stay,
            is_local_uni,
            is_local_poly,
            is_diploma,
            is_bachelor,
            is_master,
            is_phd,
            is_malaysian,
            is_couple,
            with_child,
            is_ep,
            passOr,
        )
    )
    df = DataFrame(
        DataSet,
        columns=[
            "year_of_stay",
            "is_local_uni",
            "is_local_poly",
            "is_diploma",
            "is_bachelor",
            "is_master",
            "is_phd",
            "is_malaysian",
            "is_couple",
            "with_child",
            "is_ep",
            "passOr",
        ],
    )
    export_csv = df.to_csv(
        r"C:/Users/Administrator/Desktop/SG_PR/raw.csv",
        index=None,
        header=True,
        encoding="utf-8-sig",
    )
    print("-------Success-------")


path = "C:/Users/Administrator/Desktop/SG_PR/sample.html"
main(path)


# %%
