#!/usr/bin/env python3
import os
import pandas as pd
from pprint import pprint
import sys

def describe_my_folder(path_folder):
    def describe_my_file(file_path):
        print("<<<<<<<<<<<<<<<<<<< ", file_path , ">>>>>>>>>>>>>>>>>>>")
        df = pd.read_csv(file_path, encoding='latin-1')
        def unique_for_cols(df):
            print("Details on distinct values of each column.\n")
            for col in df.columns:
                uniques = df[col].unique()
                nb_uniques = len(uniques)
                if nb_uniques <= 20:
                    print("The column ", col, " have ", nb_uniques, " distinct values.\n")
                    print("Distinct values are : ", uniques)
                    print("=============================================================")
                else:
                    print("The column ", col, " have ", nb_uniques, " distinct values.\n")
                    print("=============================================================")

        print("Shape dataframe is : ", df.shape, "\n")
        print("The columns of ", file_path, " dataframe are :")
        pprint(list(df.columns))
        unique_for_cols(df)
    for filename in [file for file in os.listdir(path_folder) if "csv" in file]:
        describe_my_file(path_folder + "/" + filename)


describe_my_folder(sys.argv[1])

