from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def clean_data(data):
    # Python code for cleaning and preprocessing the dataset
    # Drop rows with missing values

    # Convert 'Ram' and 'Weight' columns to numeric values
    data['Ram'] = data['Ram'].str.replace('GB', '').astype(int)

    data['Weight'] = data['Weight'].str.replace('kg', '').astype(float)


    # Extract screen resolution width and height
    data[['Width', 'Height']] = data['ScreenResolution'].str.extract(r'(\d+)x(\d+)').astype(int)


    # Extract CPU brand and model
    data['CpuBrand'] = data['Cpu'].str.split().str[0]
    # Extract GPU brand
    data['GpuBrand'] = data['Gpu'].str.split().str[0]

    # Convert 'Memory' column into separate SSD and HDD columns
    data['SSD'] = data['Memory'].str.extract(r'(\d+)GB SSD', expand=False).fillna(0).astype(int)
    data['HDD'] = data['Memory'].str.extract(r'(\d+)GB HDD', expand=False).fillna(0).astype(int)

    # Drop unnecessary columns
    data = data.drop(columns=['ScreenResolution', 'Cpu', 'Gpu', 'Memory'])
    # Apply one-hot encoding to categorical features
    categorical_columns = ['Company', 'TypeName', 'OpSys', 'CpuBrand', 'GpuBrand']
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    encoded = encoder.fit_transform(data[categorical_columns])
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(categorical_columns), index=data.index)
    data = pd.concat([data.drop(columns=categorical_columns), encoded_df], axis=1)
    
    # Exclude 'Price' column from scaling
    columns_to_scale = [col for col in data.columns if col != 'Price']
    # Apply MinMaxScaler to the selected columns
    scaler = MinMaxScaler()
    data[columns_to_scale] = scaler.fit_transform(data[columns_to_scale])

    data_prepared = data.copy()
        
    return data_prepared

print("Everything is fine here!")


# from sklearn.preprocessing import OneHotEncoder
# from sklearn.preprocessing import MinMaxScaler
# import pandas as pd

# def clean_data(data):
#     # Convert columns to string before using .str methods
#     data['Ram'] = data['Ram'].astype(str).str.replace('GB', '', regex=False).astype(int)
#     data['Weight'] = data['Weight'].astype(str).str.replace('kg', '', regex=False).astype(float)
#     data['ScreenResolution'] = data['ScreenResolution'].astype(str)
#     data['Cpu'] = data['Cpu'].astype(str)
#     data['Gpu'] = data['Gpu'].astype(str)
#     data['Memory'] = data['Memory'].astype(str)

#     # Extract screen resolution width and height
#     data[['Width', 'Height']] = data['ScreenResolution'].str.extract(r'(\d+)x(\d+)').astype(int)

#     # Extract CPU brand and model
#     data['CpuBrand'] = data['Cpu'].str.split().str[0]
#     # Extract GPU brand
#     data['GpuBrand'] = data['Gpu'].str.split().str[0]

#     # Convert 'Memory' column into separate SSD and HDD columns
#     data['SSD'] = data['Memory'].str.extract(r'(\d+)GB SSD', expand=False).fillna(0).astype(int)
#     data['HDD'] = data['Memory'].str.extract(r'(\d+)GB HDD', expand=False).fillna(0).astype(int)

#     # Drop unnecessary columns
#     data = data.drop(columns=['ScreenResolution', 'Cpu', 'Gpu', 'Memory'])
#     # Apply one-hot encoding to categorical features
#     categorical_columns = ['Company', 'TypeName', 'OpSys', 'CpuBrand', 'GpuBrand']
#     encoder = OneHotEncoder(sparse_output=False, drop='first')
#     encoded = encoder.fit_transform(data[categorical_columns])
#     encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(categorical_columns), index=data.index)
#     data = pd.concat([data.drop(columns=categorical_columns), encoded_df], axis=1)
    
#     # Exclude 'Price' column from scaling
#     columns_to_scale = [col for col in data.columns if col != 'Price']
#     # Apply MinMaxScaler to the selected columns
#     scaler = MinMaxScaler()
#     data[columns_to_scale] = scaler.fit_transform(data[columns_to_scale])

#     data_prepared = data.copy()
        
#     return data_prepared

# print("Everything is fine")