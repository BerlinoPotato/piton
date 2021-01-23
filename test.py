import numpy
import inspect
import confluent_kafka

src = inspect.getsource(numpy)

#print(src)




source_DF = inspect.getsource(confluent_kafka)
print(type(source_DF))

source_file_DF = inspect.getsourcefile(confluent_kafka)

print(source_file_DF)