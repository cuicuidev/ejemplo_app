import streamlit as st
import seaborn as sns

def main():
    DATABASE_URL = st.secrets["DATABASE_URL"]

    df = sns.load_dataset("iris")
    st.dataframe(df)
    st.write(DATABASE_URL)

if __name__ == "__main__":
    main()