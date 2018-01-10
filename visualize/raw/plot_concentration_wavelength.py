import matplotlib.pyplot as plt

from analyze.spectrum_parse.a_spectrasuite_parser import parse_file

data = parse_file('G:/Prive/MIJN-Documenten/TU/62-Stage/20180110/run5-4/spect/')

fig, ax = plt.subplots()
for d in data[1]:
    ax.plot(data[0], d)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Plot of spectrum analyzer')
ax.grid(True)
plt.legend()
plt.show()
