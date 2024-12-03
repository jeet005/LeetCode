import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    
    data = {"student_id": [], "age": []}
    for id, age in student_data:
        data['student_id'].append(id)
        data['age'].append(age)
        
    result = pd.DataFrame(data)
    print(result)
    return result