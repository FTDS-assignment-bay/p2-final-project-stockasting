import streamlit as st


st.set_page_config(
    page_title = "Dashboard",
    page_icon="📈",
    layout="wide"
)



def run():
    st.title("Stockastic")
    st.subheader("Welcome to our machine learning model tool!")

    st.markdown(
        """  

        This app allows you to analyze **financial data** and explore prediction outcomes to make  
        **data-driven decisions**  

        """
    )

    st.image("stock.jpg", use_column_width=True)



if __name__ == "__main__":
    run()