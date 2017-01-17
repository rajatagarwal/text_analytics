library(wordcloud)
library(tm)
# Famous speech by Martin Luther King I Have a Dream 1963
wordcloud("I have a dream that one day in Alabama with its vicious racists with its governor having his lips dripping with the words of interposition and nullification one day right there in Alabama little black boys and black girls will be able to join hands with little white boys and white girls as sisters and brothers I have a dream today I have a dream that one day every valley shall be exalted and every hill and mountain shall be made low the rough places will be made plain and the crooked places will be made straight and the glory of lord shall be revealed and all flesh shall see it together.", colors=brewer.pal(6,"Dark2"), min.freq=3, max.words=Inf, random.order=TRUE, random.color = TRUE, rot.per=0.1, ordered.colors=FALSE, use.r.layout=TRUE, fixed.asp=TRUE)

# Get more info here
# Brewer: https://cran.r-project.org/web/packages/RColorBrewer/RColorBrewer.pdf 