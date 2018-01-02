## Analyse
```
Combining data from three sources to one pickle + one xlsx file.

Ocean optics HR2000 -> SpectraSuite -> CSV -> spectrum_parse.{a,b,c} ↴
LeCroy WaveAce 224 -> EasyScope 	-> CSV -> scope_parse.{a,b,c,d}  ↴
Manual written log 					-> XLSX -> calc_run.py			-|-> data.pkl & data.xlsx
```

## Visualize
Read pickle and make various plots.