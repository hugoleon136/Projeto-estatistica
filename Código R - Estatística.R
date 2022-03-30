library(ggplot2)

setwd('C:\\Users\\HUGO CASTRO\\Desktop\\2021.1\\Estatística\\Projeto full')

df = read.csv("pesquisa.txt", header = T)
prop.table(table(df$SEXO))
prop.table(table(df$AUTODECLARAÇÃO.ÉTNICO.RACIAL))
prop.table(table(df$ESCOLARIDADE))
prop.table(table(df$MORADIA))
prop.table(table(df$ESTADO.CIVIL))
summary(df$ALTURA)
summary(df$PESO)
summary(df$IDADE)
summary(df$Nº.DE.FILHOS)
summary(df$RENDA)
var(df$ALTURA)
var(df$PESO)
var(df$IDADE)
var(df$Nº.DE.FILHOS)
var(df$RENDA)
sd(df$ALTURA)
sd(df$PESO)
sd(df$IDADE)
sd(df$Nº.DE.FILHOS)
sd(df$RENDA)
barplot(table(df$SEXO), col=c("blue","red"),
        ylim=c(0,25),
        space=0, width=c(.1,.1),
        main="Sexo",
        xlab="Gênero", ylab="Quantidade de funcionários")
text(locator(n=2),c("7","13"))
barplot(table(df$AUTODECLARAÇÃO.ÉTNICO.RACIAL), col=c("blue","red","green","yellow"),
        ylim=c(0,25),
        space=0, width=c(.1,.1),
        main="Autodeclaração étnico-racial",
        xlab=" ", ylab="Quantidade de funcionários")
text(locator(n=4),c("10%","40%","30%","20%"))
pie(table(df$ESCOLARIDADE), main="Escolaridade", labels=c("20%","20%","35%","25%"),col=c("Blue","red","green","yellow"))
legend("topright",fill=c("blue","red","green","yellow"),legend=c("Nível fundamental","Nível médio","Nível superior","Pós-graduação"))
pie(table(df$MORADIA), main="Moradia", labels=c("35%","30%","35%"), col=c("Blue","red","green"))
legend("topright",fill=c("blue","green","red"),legend=c("Alugada","Própria","Outros"))
barplot(table(df$ESTADO.CIVIL), col=c("blue","red","yellow"), 
        ylim=c(0,25), 
        space=.0, width=c(.2,.2), 
        main="Estado civil", 
        xlab=" ", ylab="Número de funcionários") 
text(locator(n=3),c("40%","35%","25"))
legend("topright",fill=c("blue","red","yellow"),legend=c("Casado(a)","Solteiro(a)","Outros"))
boxplot(df$ALTURA, col="blue", main="Altura", ylab="Classes", border="red")
hist(df$ALTURA, main="Altura", col=c(7,4),
     xlab="Variação de altura", ylab="Frequência")
boxplot(df$PESO, col="blue", main="Peso", ylab="Classes", border="red")
hist(df$IDADE, main="Idade", col=c(7,4),
     xlab="Variação de idade", ylab="Frequência")
barplot(table(df$Nº.DE.FILHOS), col=c("blue","red"), 
        ylim=c(0,25), 
        space=.8, width=c(.2,.2), 
        main="Número de filhos", 
        xlab="Quantidade de filhos", ylab="Número de funcionários") 
text(locator(n=5),c("5","5","5","4","1"))
boxplot(df$RENDA, col="blue", main="Renda", ylab="Classes", border="red")
library(ggplot2)
library(esquisse)
library(ggplot2)
ggplot(pesquisa) +
 aes(x = Nº.DE.FILHOS, y = RENDA) +
 geom_point(shape = "circle", size = 2.45, colour = "#EF562D") +
 labs(x = "Número de filhos", y = "Renda", title = "Gráfico de dispersão (Renda X Número de filhos)") +
 theme_gray() +
 theme(plot.title = element_text(size = 14L, face = "bold", hjust = 0.5), axis.title.y = element_text(face = "bold"), 
 axis.title.x = element_text(face = "bold"))

