install.packages("devtools")
devtools::install_github("JaseZiv/worldfootballR")
library(worldfootballR)
install.packages("dplyr")
library(dplyr)
install.packages("tidyr")
library(tidyr)

Messi <- understat_player_shots(player_url = "https://understat.com/player/2097")

View(Messi)
