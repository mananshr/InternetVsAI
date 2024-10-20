import streamlit as st
import pandas as pd
import numpy as np

st.title("Internet usage analysis")
st.text("By Manan Sharma")

df = pd.read_csv("./data/number-of-internet-users-by-country.csv")

#  country_code_list = set(df['Code'])

# st.dataframe(df)

country_list = df.Entity

# country_code_list = country_code_list.drop_duplicates
country_list_unique = country_list.unique()
# st.write(country_code_list.unique())

df_world = df.loc[df['Entity']=='World']

st.header("Global Usage: Numbers")

col1, col2, col3 = st.columns(3)

global_users_in_first_year = df_world['Number of internet users (OWID based on WB & UN)'].values[0]
global_first_year = df_world['Year'].values[0]
global_first_year = global_first_year.item()
global_users_in_last_year = df_world['Number of internet users (OWID based on WB & UN)'].values[-1]
global_last_year = df_world['Year'].values[-1]
global_last_year = global_last_year.item()

col1.metric(label="Number of users, in c.e. {}".format(global_first_year), value=global_users_in_first_year)

change_in_users = np.subtract(global_users_in_last_year, global_users_in_first_year)
# change_in_users = change_in_users.item()
col2.metric(label="Number of users, in c.e. {}".format(global_last_year), value=global_users_in_last_year, delta=change_in_users.item())

percet_increment = change_in_users/global_users_in_first_year
percet_increment = percet_increment * 100
percet_increment = np.round(percet_increment, 2)

col3.metric(label="Growth %, {}-{}".format(global_first_year, global_last_year), value=percet_increment, delta="Percent")

selected_entity = st.selectbox("Compair it with:", country_list_unique, placeholder="Select a country or entity", index=None)

if(selected_entity != None):

    col1, col2, col3 = st.columns(3)

    df_entity = df.loc[df['Entity']==selected_entity]

    entity_users_in_first_year = df_entity['Number of internet users (OWID based on WB & UN)'].values[0]
    entity_first_year = df_entity['Year'].values[0]
    entity_first_year = entity_first_year.item()
    entity_users_in_last_year = df_entity['Number of internet users (OWID based on WB & UN)'].values[-1]
    entity_last_year = df_entity['Year'].values[-1]
    entity_last_year = entity_last_year.item()

    col1.metric(label="Number of users, in c.e. {}".format(entity_first_year), value=entity_users_in_first_year, delta=selected_entity, delta_color="off")
    
    change_in_users_from_entity = np.subtract(entity_users_in_last_year, entity_users_in_first_year)
    
    col2.metric(label="Number of users, in c.e. {}".format(entity_last_year), value=entity_users_in_last_year, delta=change_in_users_from_entity.item())

    if(entity_users_in_first_year == 0):
        percet_increment_in_entity = "∞"
    else:
        percet_increment_in_entity = change_in_users_from_entity/entity_users_in_first_year
        percet_increment_in_entity = percet_increment_in_entity * 100
        percet_increment_in_entity = np.round(percet_increment_in_entity, 2)

    col3.metric(label="Growth %, {}-{}".format(entity_first_year, entity_last_year), value=percet_increment_in_entity, delta="Percent")

if(selected_entity == None):
    st.area_chart(df_world, x="Year", y="Number of internet users (OWID based on WB & UN)", y_label="Number of internet users, globally")
else:
    df_merged = df_world.merge(df_entity, on="Year", how='outer')
    df_merged = df_merged.drop(columns=['Entity_x', 'Code_x', 'Entity_y', 'Code_y'])
    df_merged = df_merged.rename(columns={"Number of internet users (OWID based on WB & UN)_x": "World", "Number of internet users (OWID based on WB & UN)_y":selected_entity})
    chart = st.area_chart(df_merged, x="Year", y=["World", selected_entity], y_label="Number of internet users", color=["#FF0000", "#0000FF"])

st.header("Global Usage: Percentage")

df_percentage = pd.read_csv("./data/share-of-individuals-using-the-internet.csv")

df_percentage_world = df_percentage.loc[df_percentage['Entity']=='World']
df_percentage_world