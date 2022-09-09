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
#Removing empty data points
for(i in 1:286){
  if(data[i,5]!='yes' && data[i,5]!='no'){
    data<-data[-i,]
  }
}
#Changing Strings to numbers
for(i in 1:284){
  if(data[i,2]=="premeno"){
    data[i,2]=0
  }
  if(data[i,2]=="ge40"){
    data[i,2]=1
  }
  if(data[i,2]=="lt40"){
    data[i,2]=2
  }
  if(data[i,5]=="yes"){
    data[i,5]=0
  }
  if(data[i,5]=="no"){
    data[i,5]=1
  }
  if(data[i,7]=="right"){
    data[i,7]=0
  }
  if(data[i,7]=="left"){
    data[i,7]=1
  }
  if(data[i,9]=="yes"){
    data[i,9]=0
  }
  if(data[i,9]=="no"){
    data[i,9]=1
  }
  if(data[i,10]=="recurrence-events"){
    data[i,10]=0
  }
  if(data[i,10]=="no-recurrence-events"){
    data[i,10]=1
  }
}
write.table(data, file="Data.csv", sep=",", row.names=FALSE)
