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
  if(data[i,1]=="30-39"){
    data[i,1]=0
  }
  if(data[i,1]=="40-49"){
    data[i,1]=1
  }
  if(data[i,1]=="50-59"){
    data[i,1]=2
  }
  if(data[i,1]=="60-69"){
    data[i,1]=3
  }
  if(data[i,1]=="70-79"){
    data[i,1]=4
  }
  if(data[i,3]=="0-4"){
    data[i,3]=0
  }
  if(data[i,3]=="5-9"){
    data[i,3]=1
  }
  if(data[i,3]=="10-14"){
    data[i,3]=2
  }
  if(data[i,3]=="15-19"){
    data[i,3]=3
  }
  if(data[i,3]=="20-24"){
    data[i,3]=4
  }
  if(data[i,3]=="25-29"){
    data[i,3]=5
  }
  if(data[i,3]=="30-34"){
    data[i,3]=6
  }
  if(data[i,3]=="35-39"){
    data[i,3]=7
  }
  if(data[i,3]=="40-44"){
    data[i,3]=8
  }
  if(data[i,3]=="45-49"){
    data[i,3]=9
  }
  if(data[i,3]=="50-54"){
    data[i,3]=10
  }
  if(data[i,4]=="0-2"){
    data[i,4]=1
  }
  if(data[i,4]=="3-5"){
    data[i,4]=2
  }
  if(data[i,4]=="6-8"){
    data[i,4]=3
  }
  if(data[i,4]=="9-11"){
    data[i,4]=4
  }
  if(data[i,4]=="12-14"){
    data[i,4]=5
  }
  if(data[i,4]=="15-17"){
    data[i,4]=6
  }
}

#Disproportionate number of cases showing right-breast quadrants affected by cancer, so it was deleted
data<-data[,-8]

write.table(data, file="Data.csv", sep=",", row.names=FALSE)
