# Hypotheek_aflossing
Berekend effect extra aflossing van de annuïteitenhypotheek bij structurele en of incidentele extra betalingen bij een gelijkblijvend maandbedrag tot dat de hypotheek is afgelost. 

* Start maand extra structurele aflossing kan worden ingesteld (1 als het bij de eerste maand moet plaatsvinden).
* Bedrag van extra structurele aflossing.
* N incidentele aflossingen kunenen worden ingesteld.
* Maanden wanneer de incidentele aflossingen plaats vinden.
* Bedragen van de incidentele aflossingen.

Export voorbeeld:
Berekening van een annuïteitenhypotheek met structurele en incidentele extra aflossingen

Standaard maandlast (annuïteit): 1432.25

Aflossingstabel:
Maand | Betaling ZONDER |    Rente ZONDER | Aflossing ZONDER | C. Rente ZONDER | Restschuld ZONDER |    Betaling MET |       Rente MET |   Aflossing MET |    C. Rente MET |  Restschuld MET
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    1 |         1432.25 |         1000.00 |          432.25 |         1000.00 |       299567.75 |         1432.25 |         1000.00 |          432.25 |         1000.00 |       299567.75
    2 |         1432.25 |          998.56 |          433.69 |         1998.56 |       299134.07 |         1432.25 |          998.56 |          433.69 |         1998.56 |       299134.07
    3 |         1432.25 |          997.11 |          435.13 |         2995.67 |       298698.94 |         1432.25 |          997.11 |          435.13 |         2995.67 |       298698.94
    4 |         1432.25 |          995.66 |          436.58 |         3991.34 |       298262.35 |         1432.25 |          995.66 |          436.58 |         3991.34 |       298262.35
    5 |         1432.25 |          994.21 |          438.04 |         4985.54 |       297824.31 |         1432.25 |          994.21 |          438.04 |         4985.54 |       297824.31
    6 |         1432.25 |          992.75 |          439.50 |         5978.29 |       297384.82 |         1432.25 |          992.75 |          439.50 |         5978.29 |       297384.82
    7 |         1432.25 |          991.28 |          440.96 |         6969.57 |       296943.85 |         1432.25 |          991.28 |          440.96 |         6969.57 |       296943.85
    8 |         1432.25 |          989.81 |          442.43 |         7959.39 |       296501.42 |         1432.25 |          989.81 |          442.43 |         7959.39 |       296501.42
    9 |         1432.25 |          988.34 |          443.91 |         8947.73 |       296057.51 |         1432.25 |          988.34 |          443.91 |         8947.73 |       296057.51
   10 |         1432.25 |          986.86 |          445.39 |         9934.58 |       295612.12 |         1432.25 |          986.86 |          445.39 |         9934.58 |       295612.12
   11 |         1432.25 |          985.37 |          446.87 |        10919.96 |       295165.25 |         1432.25 |          985.37 |          446.87 |        10919.96 |       295165.25
   12 |         1432.25 |          983.88 |          448.36 |        11903.84 |       294716.89 |         1532.25 |          983.88 |          548.36 |        11903.84 |       294616.89
   13 |         1432.25 |          982.39 |          449.86 |        12886.23 |       294267.03 |         1532.25 |          982.06 |          550.19 |        12885.90 |       294066.70
   14 |         1432.25 |          980.89 |          451.36 |        13867.12 |       293815.68 |         1532.25 |          980.22 |          552.02 |        13866.12 |       293514.68
   15 |         1432.25 |          979.39 |          452.86 |        14846.51 |       293362.82 |         1532.25 |          978.38 |          553.86 |        14844.50 |       292960.81
   16 |         1432.25 |          977.88 |          454.37 |        15824.38 |       292908.45 |         1532.25 |          976.54 |          555.71 |        15821.04 |       292405.10
   17 |         1432.25 |          976.36 |          455.88 |        16800.74 |       292452.56 |         1532.25 |          974.68 |          557.56 |        16795.72 |       291847.54
  357 |         1432.25 |           18.94 |         1413.31 |       215580.03 |         4268.25 |            0.00 |            0.00 |            0.00 |       170480.95 |            0.00
  358 |         1432.25 |           14.23 |         1418.02 |       215594.26 |         2850.23 |            0.00 |            0.00 |            0.00 |       170480.95 |            0.00
  359 |         1432.25 |            9.50 |         1422.75 |       215603.76 |         1427.49 |            0.00 |            0.00 |            0.00 |       170480.95 |            0.00
  360 |         1432.25 |            4.76 |         1427.49 |       215608.52 |            0.00 |            0.00 |            0.00 |            0.00 |       170480.95 |            0.00
  ...
  
--- Eindoverzicht ---
--- Besparing in looptijd ---
Looptijd hypotheek zonder extra aflossingen: 360 maanden (30.0 jaar)
Looptijd hypotheek met extra aflossingen: 300 maanden (25.0 jaar)
Aantal maanden eerder klaar met aflossen: 60 maanden (5.0 jaar)

--- Financiële besparing
Totaal betaald zonder extra aflossing (rente + aflossing): € 515608.52
Totaal betaald met extra aflossing(en) (rente + aflossing): € 470480.95

Totaal betaalde rente zonder extra aflossing(en): € 215608.52
Totaal betaalde rente met extra aflossing(en): € 170480.95
Totale besparing aan rente door extra af te lossen: € 45127.57

Totaal aan structurele aflossing: € 28900.00 (€ 100.00 per maand vanaf maand 12 gedurende 289 maanden)
Totaal aan incidentele aflossingen: € 12500.00 (€ 5000.00 in maand 24, € 7500.00 in maand 48)
Totaal aan sneeuwbaleffect aflossingen: € 36602.43 
Totaal extra aflossing (inclusief sneeuwbaleffect): € 78002.43

  ![image](https://github.com/user-attachments/assets/76d14340-6992-4969-b868-9b106ee3440a)
