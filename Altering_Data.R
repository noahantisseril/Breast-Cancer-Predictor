install.packages("jsonlite", repos="https://cran.rstudio.com/")
library("jsonlite")

json_file <- 'https://datahub.io/machine-learning/breast-cancer/datapackage.json'
json_data <- fromJSON(paste(readLines(json_file), collapse=""))

# get list of all resources:
print(json_data$resources$name)

# print all tabular data(if exists any)
for(i in 1:length(json_data$resources$datahub$type)){
  if(json_data$resources$datahub$type[i]=='derived/csv'){
    path_to_file = json_data$resources$path[i]
    data <- read.csv(url(path_to_file))
    print(data)
  }
}

for(i in 1:286){
  if(data[i,6]==3){
    data[i,6]="Malignant"
  }
  if(data[i,6]==2){
    data[i,6]="Benign"
  }
  if(data[i,6]==1){
    data[i,6]="Normal"
  }
  if(data[i,5]!='yes' && data[i,5]!='no'){
    data<-data[-i,]
  }
}
write.table(data, file="Data.csv", sep="\t", row.names=FALSE)
