import matplotlib.pyplot as plt

from analyze.spectrum_parse.a_spectrasuite_parser import parse_file

data = parse_file('G:/Prive/MIJN-Documenten/TU/62-Stage/20180131-compare/run1/spect/')
# data = parse_file('G:/Prive/MIJN-Documenten/TU/62-Stage/20180118-def2/run3-2/spect/')
data[1] = data[1][:]

fig, ax = plt.subplots()
for i, d in enumerate(data[1]):
    ax.plot(data[0], d, label=i)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Plot of spectrum analyzer')
ax.grid(True)
plt.legend()
plt.show()
