import pandas as pd
obj={1:"one",2:"Two",3:"Three",4:"Four"}
obj2=pd.Series(obj)
print(obj2)
# Converting back to Dictionary
new_object=obj2.to_dict()
print(new_object)