import pandas as pd
import numpy as np 
import streamlit as st 


def load_data():
    return pd.read_csv(r'D:\OneDrive\Pessoal\2. Data Science\Comunidade_DS\repos\repos\Git\projeto\data\processed\bikes_completed.csv')

def main():
    df = load_data()
    st.dataframe(df)
    
if __name__ == '__main__':
    main()