[![testing](https://github.com/sophiemanuel/wwstatviz/actions/workflows/tests.yml/badge.svg)](https://github.com/sophiemanuel/wwstatviz/actions)

# wwstatviz - World Wide Statistics Visualizer

This repository contains two python packages:

- wwstatviz: provides a high-level API that simplifies the visualization of
  statistics about countries on a world map or in different types of plots.
- wwstatviz-webapp: provides a user friendly interface making use of wwstatviz
  API for visualizing world wide statistics in a browser. It is destined to
  regular (non-developer) end-users.

This package is still WIP.

## Installation

To install the API from the git repository directly:

```
pip install "git+https://github.com/sophiemanuel/wwstatviz.git#egg=wwstatviz&subdirectory=wwstatviz"
```

To install the web application:

```
pip install "git+https://github.com/sophiemanuel/wwstatviz.git#egg=wwstatviz-webapp&subdirectory=wwstatviz-webapp"
```

The web application is still in early stage active development, so the 
installation may fail.

## API Usage

wwstatviz logic is as follows:

First, we define data in a CSV file having the following specific format:

|    | feature\_1   | feature\_2   | ... | feature\_N   |
|----|:------------:|:------------:|-----|:------------:|
| JP |     3.11     |      930     | ... |      241     |
| NO |     3.11     |     1230     | ... |      123     |
| AT |     3.11     |     1930     | ... |      197     |
| .. |              |              | ... |              |
| CO |     5.36     |     1820     | ... |       93     |

The rows of the CSV data file must be indexed by the 
[ISO country codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) 
(Alpha-2 or Alpha-3 codes). The data file should contain at least one feature
column that hold the values to be visualized in the map or in the plot. The
feature columns must hold numerical values.

Second, we declare a visualizer object and provide as argument the path to the
data file described above:

```python
from wwstatviz import Visualizer
vis = Visualizer('/path/to/data.csv')
```

Third, we use the visualizer to generate plots:

```python
# generates a choropleth map visualizing the values of feature_1 for all countries
fig = vis.choropleth(feature = 'feature_1', countries = 'all') 

# to save generated figure
fig.save('/path/to/figure.ext')

# bar plot in which:
# the x-axis contains the set of countries given in the argument "countries"
# the y-axis contains the bars of the features given in the argument "features"
vis.histogram(features = ['feature_1', 'feature_3'], countries = ['FR', 'US'])
```

For more information about plotting, you can refer to the 
[API documentation](wwstatviz/doc/build/html/index.html).

## Web Application Usage

1. To run the web application, type in a terminal:

```
$ wwstatviz --port 7890
Application is run in http://0.0.0.0:7890
```

2. Then, in the web browser, open http://0.0.0.0:7890.
3. Upload a CSV file containing the data (in the same format described above).
4. Select the features to visualize in the appropriate menu.
4. In the left menu, select the type of visualization to plot (you can filter
   by country).
5. The web application provides buttons to download the plot in PDF or PNG
   formats for later use.

## Task affectation

For the time being, the work is organized as follows :

* Data preprocessing and loading : Seydou
* Interactive choropleth map (design, features,...) : Anas, Ravahere
* Histogram/KDE and sortable datatable Sophie using the package `pandas`
* Heatmap : Anas, Ravahere
* Lineplot : Anas
* Animation : Seydou, Sophie
* Unit Testing by the team
* Documentation will be written by the team
* Beamer for the oral presentation will be done by the team
* Web app : Depending on the project's evolution & deadlines, the package is 
  expected to have a dedicated web app that will be implemented by the team 
  members. We will use flask as a development framework.

## Authors

- Sophie Manuel [sophie.manuel@etu.umontpellier.fr](mailto:sophie.manuel@etu.umontpellier.fr)
- Ravahere Paint-Koui [ravahere.paint-koui@etu.umontpellier.fr](mailto:ravahere.paint-koui@etu.umontpellier.fr)
- Seydou Sane [seydou.sane@etu.umontpellier.fr](mailto:seydou.sane@etu.umontpellier.fr)
- Anas Zakroum [anas.zakroum@etu.umontpellier.fr](mailto:anas.zakroum@etu.umontpellier.fr)

*(sorted by last name)*

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
