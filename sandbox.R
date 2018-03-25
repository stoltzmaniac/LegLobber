library(circlize)
library(tidyverse)
library(ggalluvial)
library(ggpubr)


data = read_csv('all_data.csv')

head(data)

df = data %>%
  filter(fiscalYear==2015) %>%
  mutate(lobbyist = paste(lobbyistLastName, lobbyistFirstName, sep='-'),
         #client = paste(clientLastName, clientFirstName, sep='-'),
         client = clientName,
         income = as.numeric(gsub('\\$','',incomeAmount))) %>%
  group_by(lobbyist, clientBusinessDescription) %>%
  summarise(income = sum(income), n = n()) %>%
  mutate(donationSize = if_else(income>100000, 'Large', 'Small')) %>%
  select(lobbyist, clientBusinessDescription, n, donationSize, income) %>%
  arrange(-income)

ggplot(as.data.frame(df[1:30,]), 
       aes(weight = n, axis1=lobbyist, axis2=clientBusinessDescription)) + 
  geom_alluvium(aes(fill=donationSize), width=1/12) + 
  geom_stratum(width=1/12, fill='black', color='grey') + 
  geom_label(stat = "stratum", label.strata = TRUE) +
  scale_x_continuous(breaks=1:2, labels=c('Lobbyist', 'Business Description')) + 
  scale_fill_brewer(type='qual', palette='Set1') + 
  ggtitle('great')


df = data %>%
  filter(fiscalYear==2015) %>%
  mutate(lobbyist = paste(lobbyistLastName, lobbyistFirstName, sep='-'),
         #client = paste(clientLastName, clientFirstName, sep='-'),
         client = clientName,
         income = as.numeric(gsub('\\$','',incomeAmount))) %>%
  group_by(lobbyist, clientBusinessDescription) %>%
  summarise(income = sum(income), n = n()) %>%
  mutate(donationSize = if_else(income>100000, 'Large', 'Small'), avgDonation = income/n) %>%
  select(lobbyist, clientBusinessDescription, n, donationSize, income, avgDonation) %>%
  arrange(-avgDonation)

ggplot(as.data.frame(df[1:30,]), 
       aes(weight = n, axis1=lobbyist, axis2=clientBusinessDescription)) + 
  geom_alluvium(aes(fill=donationSize), width=1/12) + 
  geom_stratum(width=1/12, fill='black', color='grey') + 
  geom_label(stat = "stratum", label.strata = TRUE) +
  scale_x_continuous(breaks=1:2, labels=c('Lobbyist', 'Business Description')) + 
  scale_fill_brewer(type='qual', palette='Set1') + 
  ggtitle('great')



df = data %>%
  filter(fiscalYear==2015) %>%
  mutate(lobbyist = paste(lobbyistLastName, lobbyistFirstName, sep='-'),
         #client = paste(clientLastName, clientFirstName, sep='-'),
         client = clientName,
         income = as.numeric(gsub('\\$','',incomeAmount))) %>%
  group_by(lobbyist) %>%
  summarise(income = sum(income), n = n()) %>%
  mutate(donationSize = if_else(income>100000, 'Large', 'Small'), avgDonation = income/n) %>%
  select(lobbyist, n, donationSize, income, avgDonation)

p1 = ggplot(df %>% arrange(-avgDonation) %>% top_n(10), aes(x=reorder(lobbyist,avgDonation))) + 
  geom_bar(aes(y=avgDonation),stat='identity') + coord_flip()

p2 = ggplot(df %>% arrange(-income) %>% top_n(10), aes(x=reorder(lobbyist,income))) + 
  geom_bar(aes(y=income),stat='identity') + coord_flip()

p3 = ggplot(df %>% arrange(-n) %>% top_n(10), aes(x=reorder(lobbyist,n))) + 
  geom_bar(aes(y=n),stat='identity') + coord_flip()

ggarrange(p1,p2,p3, ncol=3)




df = data %>%
  filter(fiscalYear==2015) %>%
  mutate(lobbyist = paste(lobbyistLastName, lobbyistFirstName, sep='-'),
         #client = paste(clientLastName, clientFirstName, sep='-'),
         client = clientName,
         income = as.numeric(gsub('\\$','',incomeAmount))) %>%
  group_by(clientBusinessDescription) %>%
  summarise(income = sum(income), n = n()) %>%
  mutate(donationSize = if_else(income>100000, 'Large', 'Small'), avgDonation = income/n) %>%
  select(clientBusinessDescription, n, donationSize, income, avgDonation) %>%
  drop_na()

p1 = ggplot(df %>% arrange(-avgDonation) %>% top_n(10), aes(x=reorder(clientBusinessDescription,avgDonation))) + 
  geom_bar(aes(y=avgDonation),stat='identity') + coord_flip()

p2 = ggplot(df %>% arrange(-income) %>% top_n(10), aes(x=reorder(clientBusinessDescription,income))) + 
  geom_bar(aes(y=income),stat='identity') + coord_flip()

p3 = ggplot(df %>% arrange(-n) %>% top_n(10), aes(x=reorder(clientBusinessDescription,n))) + 
  geom_bar(aes(y=n),stat='identity') + coord_flip()

ggarrange(p1,p2,p3, ncol=3)
