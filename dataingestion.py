import pandas as pd
import streamlit as st
import streamlit.server.server as streamlit_server
from az_blob_query import * #upload_blob,read_data_from_blob
# providing raw url to download csv from github
# brands = 'brandname_encoding.csv'
connection_string = "DefaultEndpointsProtocol=https;AccountName=microservicesstoreafrdev;AccountKey=1sZeV2d35MKBGM4wneLOt+cQH0mXcFJgvd19BnjcQk1vzh12xgg9loLzgIZSLcHjerlOEIQlc/L/1i1vCGR5vA==;EndpointSuffix=core.windows.net"


connection_string = "DefaultEndpointsProtocol=https;AccountName=microservicesstoreafrdev;AccountKey=1sZeV2d35MKBGM4wneLOt+cQH0mXcFJgvd19BnjcQk1vzh12xgg9loLzgIZSLcHjerlOEIQlc/L/1i1vCGR5vA==;EndpointSuffix=core.windows.net"
#os.getenv('_connection_string')

# @st.cache
def readdata():
    # Read data
    try:
#         branddf = read_data_from_blob(blob_name='brandname_encoding.csv',connection_string=connection_string)
#         df = read_data_from_blob(blob_name='allrecordsohe.csv',connection_string=connection_string)
#         df2 = read_data_from_blob(blob_name='allrecords.csv',connection_string=connection_string)
        df = pd.read_csv('allrecordsohe.csv', low_memory=False)
        df2 = pd.read_csv('allrecords.csv', low_memory=False)
        branddf = pd.read_csv('brandname_encoding.csv', low_memory=False)
    except BaseException:
        print('Blob download failed')
    # df = pd.read_csv('allrecordsohe.csv', low_memory=False)
    # df2 = pd.read_csv('allrecords.csv', low_memory=False)
#     branddf = pd.read_csv(brands, low_memory=False)

    # Check for empty data
    df.isnull().sum()
    df2.isnull().sum()

    # Remove NaN
    nr_samples_before = df.shape[0]
    df = df.fillna(0)
    print('Removed %s samples' % (nr_samples_before - df.shape[0]))
    nr_samples_before = df2.shape[0]
    df2 = df2.fillna(0)
    print('Removed %s samples' % (nr_samples_before - df2.shape[0]))

    # Drop irrelevant variables
#     df.drop(['TD_ID', 'KRUX_ID', 'TAP_IT_ID', 'GOOGLE_CLIENT_ID'], axis=1, inplace=True)
#     df2.drop(['TD_ID', 'KRUX_ID', 'TAP_IT_ID', 'GOOGLE_CLIENT_ID'], axis=1, inplace=True)

    # df = df.reset_index()
    # df2 = df2.reset_index()

    return df, df2, branddf

    ### End


