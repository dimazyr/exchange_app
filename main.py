import file_reader as fr
import processing as pr

filepathdata = "dataset/TRD2.csv"
data, exchange_classes=fr.read_file(filepathdata)
for i in range(1, len(exchange_classes)):
    print(pr.greatest_window(data, exchange_classes[i]), exchange_classes[i])
