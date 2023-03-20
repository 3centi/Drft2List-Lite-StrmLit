import pandas as pd

def get_studentData_fromClassUnit(_df, leftUpCell_row, leftUpCell_column, day, roomCell_row = 1, studentNumber = 8,fillna_str = ''):
    df, _df_class = pd.DataFrame(), pd.DataFrame()
    _df_class['Student_Name'] = _df.iloc[leftUpCell_row + 2:leftUpCell_row + 2 + studentNumber,[leftUpCell_column]]
    _df_class['Day'] = day
    if type(_df.iloc[leftUpCell_row, leftUpCell_column]) == str:
        _df_class['Time'] = str(_df.iloc[leftUpCell_row, leftUpCell_column])[:4]
    else:
        _df_class['Time'] = _df.iloc[leftUpCell_row, leftUpCell_column]
    _df_class['Room'] = _df.iloc[roomCell_row, leftUpCell_column]
    _df_class['Teacher'] = _df.iloc[leftUpCell_row + 1, leftUpCell_column]
    _df_class['Level'] = _df.iloc[leftUpCell_row, leftUpCell_column + 1]
    _df_class['Grade'] = _df.iloc[leftUpCell_row + 2:leftUpCell_row + 2 + studentNumber,[leftUpCell_column + 1]]
    df = pd.concat([df,_df_class])
    df = df.dropna(subset = ['Student_Name'])
    df = df[df["Student_Name"] != " "]
    df = df[df["Student_Name"] != "　"]
    df = df.fillna({
        'Time' : fillna_str,
        'Room' : fillna_str,
        'Teacher' : fillna_str
    })
    return df

def get_studentData_from3ClassUnits(_df, leftUpCell_row, leftUpCell_column, day, roomCell_row = 1, studentNumber = 8, fillna_str = ''):
    df = pd.DataFrame()
    for i in range(3):
        _df_class = get_studentData_fromClassUnit(_df,leftUpCell_row, leftUpCell_column + 2*i , day, roomCell_row, studentNumber, fillna_str)
        df = pd.concat([df,_df_class])
    return df

def get_studentData_from12ClassUnits(_df, leftUpCell_row, leftUpCell_column, day, roomCell_row = 1, studentNumber = 8,fillna_str = ''):
    df = pd.DataFrame()
    for i in range(4):
        _df_class = get_studentData_from3ClassUnits(_df, leftUpCell_row + 11*i , leftUpCell_column, day, roomCell_row, studentNumber,fillna_str)
        df = pd.concat([df,_df_class])
    return df

def get_studentData_fromNormalElemAndKindyClasses(_df,fillna_str = ''):
    days = ['Tue','Wed','Thu','Fri','Sat']
    df = pd.DataFrame()
    for i,day in enumerate(days):
        _df_class = get_studentData_from12ClassUnits(_df, 3 ,6 + 9*i, days[i],fillna_str = fillna_str)
        df = pd.concat([df,_df_class])
    for j in range(2):
        _df_class = get_studentData_from3ClassUnits(_df, 3 + 11*j ,49,'Sat',fillna_str = fillna_str)
        df = pd.concat([df,_df_class])
    return df

def get_studentData_from4ClassUnits(_df, leftUpCell_row, leftUpCell_column, day, roomCell_row = 59, studentNumber = 12,fillna_str = ''):
    df = pd.DataFrame()
    for i in range(4):
        _df_class = get_studentData_fromClassUnit(_df, leftUpCell_row, leftUpCell_column + 2*i , day, roomCell_row, studentNumber, fillna_str)
        df = pd.concat([df,_df_class])
    return df

def get_studentData_fromNormalAcademyClasses(_df,fillna_str = ''):
    days = ['Tue','Wed','Thu','Fri','Sat']
    df = pd.DataFrame()
    for i,day in enumerate(days):
        _df_class = get_studentData_from4ClassUnits(_df, 61,6 + 9*i , day,fillna_str = fillna_str)
        df = pd.concat([df,_df_class])
    return df

def get_studentData_fromMondayClasses(_df,fillna_str = ''):
    df = pd.DataFrame()
    for i in range(4):
        _df_class = get_studentData_fromClassUnit(_df, 3 + 11*i ,3,'Mon',fillna_str = fillna_str)
        df = pd.concat([df,_df_class])

    _df_class = get_studentData_fromClassUnit(_df, 61, 3 ,'Mon' , 59, 12,fillna_str = fillna_str)
    df = pd.concat([df,_df_class])

    _df_class = get_studentData_fromClassUnit(_df, 50, 3, 'Mon', 48, 2,fillna_str = fillna_str)
    df = pd.concat([df,_df_class])

    _df_class = get_studentData_fromClassUnit(_df, 78, 3, 'Mon', 76, 2,fillna_str = fillna_str)
    df = pd.concat([df,_df_class])
    return df

def get_studentData_fromSundayClass(_df,fillna_str = ''):
    return get_studentData_fromClassUnit(_df, 3, 59, 'Sun',fillna_str = fillna_str)

def get_studentData_fromPrivateClass(_df,fillna_str = ''):
    df = pd.DataFrame()
    days = ['Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    for i in range(2):
        for j in range(4):
            for k in range(4): 
                _df_class = get_studentData_fromClassUnit(_df, 50 + 28*i , 6 + 2*k + 9*j, days[j], 48 + 28*i , 2,fillna_str = fillna_str)
                df = pd.concat([df,_df_class])
    
    for i in range(2):
        for j in range(2):
            for k in range(3):
                _df_class = get_studentData_fromClassUnit(_df, 50 + 28*i, 42 + 2*k + 7*j , 'Sat', 48 + 28*i , 2,fillna_str = fillna_str)
                df = pd.concat([df,_df_class])
    return df

def get_studentData(_df,fillna_str = ''):
    df = get_studentData_fromNormalElemAndKindyClasses(_df,fillna_str)
    _df_1 = get_studentData_fromNormalAcademyClasses(_df,fillna_str)
    _df_2 = get_studentData_fromPrivateClass(_df,fillna_str)
    _df_3 = get_studentData_fromMondayClasses(_df,fillna_str)
    _df_4 = get_studentData_fromSundayClass(_df,fillna_str)

    df = pd.concat([df, _df_1, _df_2, _df_3, _df_4])
    return df