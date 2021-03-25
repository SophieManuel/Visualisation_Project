# wwstatviz - World Wide Statistics Visualizer

This is a python package providing a high-level API that simplifies 
the visualization of statistics about countries on a world map or in different
types of plots.

This package is still WIP.

## Installation

```
pip install wwstatviz
```

## API Usage

wwstatviz logic is as follows:

First, we define data in a pandas dataframe having the following specific format:

|    | feature\_1   | feature\_2   | ... | feature\_N   |
|----|:------------:|:------------:|-----|:------------:|
| MA |     3.11     |      930     | ... |      241     |
| FR |     3.11     |     1230     | ... |      123     |
| PF |     3.11     |     1930     | ... |      197     |
| .. |              |              | ... |              |
| SN |     5.36     |     1820     | ... |       93     |

The rows of the data frame must be indexed by the 
[ISO country codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) 
(Alpha-2 or Alpha 3 code). The data frame should contain at least one feature
column that hold the values to be visualized in the map or in the plot. The
feature columns must hold numerical values.

Second, we declare a visualizer object and provide as argument the dataframe described above:

```python
from wwstatviz.visual import Visualizer
df = pd.read_csv('...')
vis = Vizualizer(data = df)
```

Third, we use the visualizer to generate plots:

```python
# generate a choropleth map visualizing the values of feature_1
vis.map(type = 'choropleth', feature = 'feature_1') 

# to generate scatter points map visualizing values of feature_3
vis.map(type = 'scatter', feature = 'feature_3')

# bar plot in which:
# the x-axis contains the set of countries given in the argument "countries"
# the y-axis contains the bars of the features given in the argument "features"
vis.bar(features = ['feature_1', 'feature_3'], countries = ['FR', 'US'])
```

For more information about possible plots, you can refer to the 
[API documentation](#).

## Authors

- Anas Zakroum [anas.zakroum@etu.umontpellier.fr](mailto:anas.zakroum@etu.umontpellier.fr)
- Sophie Manuel [sophie.manuel@etu.umontpellier.fr](mailto:sophie.manuel@etu.umontpellier.fr)
- Ravahere Paint-Koui [ravahere.paint-koui@etu.umontpellier.fr](mailto:ravahere.paint-koui@etu.umontpellier.fr)
- Seydou Sane [seydou.sane@etu.umontpellier.fr](mailto:seydou.sane@etu.umontpellier.fr)

## License

GNU General Public License v3

```
wwstatviz - World Wide Statistics Visualizer
Copyright (C) 2021 A. Zakroum, S. Manuel, R. Paint-Koui, S. Sane

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
