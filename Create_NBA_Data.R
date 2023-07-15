library(data.table)

nba22 <- fread('data/NBA/PlayerPerMinute21_22.csv')
nba23 <- fread('data/NBA/PlayerTotals22_23.csv')


nba22 <- nba22[`Player-additional`!='']
nba23 <- nba23[`Player-additional`!='']

shared_players <- intersect(nba22$Player, nba23$Player)
shared_cols <- intersect(names(nba22), names(nba23))

nba22 <- nba22[Player %in% shared_players]
nba23 <- nba23[Player %in% shared_players]


nba22[,Year:=2022]
nba23[,Year:=2023]

nba_long <- rbind(nba22[,..shared_cols], nba23[,..shared_cols])

setnames(nba23, 'PTS', 'TotalPts22_23')

nba <- merge(nba23[,.(Player, Tm, TotalPts22_23)],
             nba22, by=c('Player', 'Tm'))



fwrite(nba, 'data/NBA/NBA_Player_Data.csv')
fwrite(nba_long, 'data/NBA/NBA_Player_Data_Long.csv')
