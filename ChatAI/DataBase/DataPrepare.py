import os
import string
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Token =  {}

def find_DB(word):
    word2 = word
    return 1
def Add_DB(word):
    word2 = word
    return 1
def sep(input_file, output_file):
    # ������ ����������� �����
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # �������� ������ ����� ��� �����, ���������� ������ �������
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    Without = '\n'.join(non_empty_lines)
    return Without
def MD(Without):
    # ������ ���������� ����� � ����� ���� ��� ���������� ��������� �����
    Type = "req"
    arr = [""]
   
    for lin in Without:
        analyse = lin.translate(str.maketrans('', '', string.punctuation))
        analyse = analyse.lower()
        analyse = analyse.split()
        if analyse[0] == "�������":
            Type = "ret"
            
        for word in analyse:
            if find_DB(word):
                arr.append(find_DB(word))
            else:
                arr.append(Add_DB(word))
    return Type, arr