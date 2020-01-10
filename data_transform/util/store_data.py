def store_dataframe(df, file_type, file_path):
    with open(file_path, 'wb') as file:
        if(file_type == 'csv'):
            data_to_write = df.to_csv()

        file.write(data_to_write.encode())
