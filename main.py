import streamlit as st
import hashlib
import pandas as pd
import datetime as dt
import app

def main():
    st.title('Draft to List Lite')
    manual = '''
    使い方は<a href="https://marked-jaborosa-40b.notion.site/Draft-to-List-Lite-f5f3e4872df14b2e83c3ca8bf2fb2b32">こちら</a>
    '''
    st.write(manual, unsafe_allow_html = True)
    pw = st.text_input('Enter password / パスワードを入力',type = 'password')

    if hashlib.sha224(pw.encode()).hexdigest() == st.secrets["PW_HASH"]:
        uploaded_file = st.file_uploader('Upload the draft as csv file / CSVファイルをアップロード','csv')
    
        if uploaded_file is not None:

            encoding = st.sidebar.selectbox('Encoding / 文字コード',('utf-8','shift-jis','cp932'))

            _df = pd.read_csv(uploaded_file,encoding=encoding)

            df = app.get_studentData(_df)

            columns = ['Student_Name','Day','Time','Room','Teacher','Level','Grade']
            df = df.reset_index()
            df = df.loc[:,columns]
            
            df_csv = df.to_csv()

            now = dt.datetime.now()
            file_name = 'StudentList_' + now.strftime('%Y%m%d%H%M%S') + '.csv'
            st.download_button('Download the list as ' + file_name, df_csv,file_name,'csv')

            st.dataframe(df)

if __name__ == '__main__':
    main()
