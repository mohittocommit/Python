import csv

csvfile = open("dummy_csv.csv", "w")
writer = csv.writer(csvfile)
writer.writerow(["SN","Name","Contribution",1,"Linus Torvalds","Linux Kernels"])

csvfile.close()
