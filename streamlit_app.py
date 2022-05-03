import streamlit as st
import snowflake.connector

# Credentials need to connect to Snowflake! Add these to your Streamlit secrets
PASSWORD = st.secrets["PASSWORD"]
WAREHOUSE = st.secrets["WAREHOUSE"]
USER = st.secrets["USER"]
ACCOUNT = st.secrets["ACCOUNT"]

# Let's write some queries to run in Snowflake!
query_1 = " "
query_2 = " "
query_3 = " "

initiate_snowflake_connection = st.button("Initiate Snowflake Connection")

# Before running any queries, we need to set up our connection to Snowflake
if initiate_snowflake_connection:
  conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT
  )
  
cur = conn.cursor() # Cursor object allows you to execute DDL/DML statements & queries
cur.execute(query_1) # Execute your first query!
results_query_1 = cur.fetchall() # Use .fetchall() to grab all results of your query
num_results_query_1 = cur.rowcount # Use .rowcount to count number of results

st.heading("Here are the results of my first query: ")
st.write(results_query_1) # Print your first query's result with st.write


# first_name = st.text_input("Customer's first name", placeholder="John")
# last_name = st.text_input("Customer's last name", placeholder="Smith")
# search_for_cust = st.button("Search for existing customer")
# add_new_cust = st.button("Add new customer")

#     if num_results == 0:
#         st.info('0️⃣ No such customer exists in the database.')
#     elif num_results == 1:      
#         for first, last in results:
#             search_results += f"{first} {last}."
#         full_results = "✅ One customer exists in the database with the same first and last name.\n Here is the customer: " + search_results
#         st.success(full_results)
#     else:
#         search_results = ""
#         for first, last in results:
#             ind += 1
#             if num_results == ind:
#                 search_results += f"and {first} {last}."
#             else:
#                 search_results += f"{first} {last}, "
#         cust_exists_message = "✅ " + str(num_results) + " customers exist in the database with the same first and last names.\n Here they are: "
#         full_results = cust_exists_message + search_results
#         st.success(full_results)

# if add_new_cust:
#     conn = snowflake.connector.connect(
#         user=USER,
#         password=PASSWORD,
#         account=ACCOUNT,
#     )
    
#     cur = conn.cursor()
#     cur.execute("INSERT INTO CUSTOMER_LOYALTY_PROGRAM.PUBLIC.CUSTOMERS VALUES (%s, %s)", (first_name, last_name))
    
#     if cur.rowcount > 0:
#         st.success("🥳 Customer was successfully added to the database.")
#     else:
#         st.error("😬 Whoops! We couldn't add your customer. Try again or check the logs.")
