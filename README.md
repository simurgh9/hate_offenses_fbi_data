<p align="center">
  <img
    width="1024px"
    src="./media/explore0.png"
    alt="Federal Bureau of Investigation (FBI) crime data for hate crimes."
  />
</p>
<h1 align="center">
  Federal Bureau of Investigation (FBI) Hate Crime Data Clustered by
  Groups of People
</h1>

The original data was downloaded on 2024 November 9th as [individual
files](nibrs_files) from the Federal Bureau of Investigation's (FBI) National
Incident-Based Reporting System (NIBRS).

It is publicly available at the following URLs,

- https://www.fbi.gov/how-we-can-help-you/more-fbi-services-and-information/ucr/hate-crime
- https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/hate-crime

The first link points to the second one and is titled "FBI CRIME DATA
EXPLORER." It appears to be an app that allows you to filter, view and
download the crime-data under different constrains.

# Processing

The original comma separated value (CSV) files from NIBRS were then
aggregated into one file using the following Python script,

- [aggregate.py](aggregate.py)

The aggregated CSV file is given bellow,

- [hate_offenses_fbi_data.csv](hate_offenses_fbi_data.csv)

Other than the standard Python 3, I have used the famous Python
libraries [NumPy](https://numpy.org/) and [Matplotlib](https://matplotlib.org/) for fast numerical
computations and plots.

# Description

Given bellow are the data headers in the aggregated data.

> Date, All, American Indian Or Alaska Native, Arab, Asian, Atheism
> Agnosticism, Bisexual, Black, Buddhist, Catholic, Church Of Jesus
> Christ, Eastern Orthodox Christian, Female, Gay, Gender Non
> Conforming, Hetrosexual, Hindu, Hispanic, Jehovahs Witness, Jewish,
> Lesbian, Male, Mental Disability, Muslim, Native Hawaiian Other
> Pacific Islander, Other Religion, Physical Disability, Protestant,
> Sikh, Transgender, White

The first column lists the dates (YYYY-MM) on which the offenses in
each respective row occurred. The rest of the columns are the _counts_
of the hate offences committed against the corresponding groups of
people on any given date.  E. g., the row corresponding to the date
`2009-01` and column corresponding to the group `Asian` intersect at
the cell with count `13`, i. e., there were 13 hate offences committed
in January of 2009 against Asians in the United States.

Note that all these columns are directly downloaded from NIBRS and not
computed based on other columns. I. e., if a certain row is not
totalling to its corresponding "All" cell then the reason may be
searched for in the documentation available on the FBI websites
provided above.

# Missing Values

The original files from NIBRS were missing data points for certain
dates. These are notated as [not a number](https://en.wikipedia.org/wiki/NaN) _NaN_ values in the
aggregated file.

Even though the aggregate CSV file's date column has dates from
2024-01 to 2024-11. The corresponding rows are all NaNs likely due to
that data not being available at the time of download.

# Code

You can perform your own analysis by reading the data as done in
[read_data.py](read_data.py),

```python
import numpy as np

source = 'https://cde.ucr.cjis.gov/'
source += 'LATEST/webapp/#/pages/explorer/crime/hate-crime'
data = np.loadtxt('hate_offenses_fbi_data.csv', delimiter=',', dtype=object)
header, data = data[0][1:], data[1:]
dates = data[:, 0].astype(np.datetime64)
offenses = data[:, 1:].astype(np.float64)
years = np.array([date.item().year for date in dates[::12]])
```

# Figures

I have generated some basic figures via [explore.py](explore.py) and
[bigplot.py](bigplot.py) that can be found in the [media](media) directory. They
are also drawn bellow,

![Hate crimes frequency by group.](media/bigplot.png 'Hate crimes frequency by group.')
![Hate crimes frequency against American Indian Or Alaska Native.](media/explore1.png 'Hate crimes frequency against American Indian Or Alaska Native.')
![Hate crimes frequency against Arab.](media/explore2.png 'Hate crimes frequency against Arab.')
![Hate crimes frequency against Asian.](media/explore3.png 'Hate crimes frequency against Asian.')
![Hate crimes frequency against Atheism Agnosticism.](media/explore4.png 'Hate crimes frequency against Atheism Agnosticism.')
![Hate crimes frequency against Bisexual.](media/explore5.png 'Hate crimes frequency against Bisexual.')
![Hate crimes frequency against Black.](media/explore6.png 'Hate crimes frequency against Black.')
![Hate crimes frequency against Buddhist.](media/explore7.png 'Hate crimes frequency against Buddhist.')
![Hate crimes frequency against Catholic.](media/explore8.png 'Hate crimes frequency against Catholic.')
![Hate crimes frequency against Church Of Jesus Christ.](media/explore9.png 'Hate crimes frequency against Church Of Jesus Christ.')
![Hate crimes frequency against Eastern Orthodox Christian.](media/explore10.png 'Hate crimes frequency against Eastern Orthodox Christian.')
![Hate crimes frequency against Female.](media/explore11.png 'Hate crimes frequency against Female.')
![Hate crimes frequency against Gay.](media/explore12.png 'Hate crimes frequency against Gay.')
![Hate crimes frequency against Gender Non Conforming.](media/explore13.png 'Hate crimes frequency against Gender Non Conforming.')
![Hate crimes frequency against Hetrosexual.](media/explore14.png 'Hate crimes frequency against Hetrosexual.')
![Hate crimes frequency against Hindu.](media/explore15.png 'Hate crimes frequency against Hindu.')
![Hate crimes frequency against Hispanic.](media/explore16.png 'Hate crimes frequency against Hispanic.')
![Hate crimes frequency against Jehovahs Witness.](media/explore17.png 'Hate crimes frequency against Jehovahs Witness.')
![Hate crimes frequency against Jewish.](media/explore18.png 'Hate crimes frequency against Jewish.')
![Hate crimes frequency against Lesbian.](media/explore19.png 'Hate crimes frequency against Lesbian.')
![Hate crimes frequency against Male.](media/explore20.png 'Hate crimes frequency against Male.')
![Hate crimes frequency against Mental Disability.](media/explore21.png 'Hate crimes frequency against Mental Disability.')
![Hate crimes frequency against Muslim.](media/explore22.png 'Hate crimes frequency against Muslim.')
![Hate crimes frequency against Native Hawaiian Other Pacific Islander.](media/explore23.png 'Hate crimes frequency against Native Hawaiian Other Pacific Islander.')
![Hate crimes frequency against Other Religion.](media/explore24.png 'Hate crimes frequency against Other Religion.')
![Hate crimes frequency against Physical Disability.](media/explore25.png 'Hate crimes frequency against Physical Disability.')
![Hate crimes frequency against Protestant.](media/explore26.png 'Hate crimes frequency against Protestant.')
![Hate crimes frequency against Sikh.](media/explore27.png 'Hate crimes frequency against Sikh.')
![Hate crimes frequency against Transgender.](media/explore28.png 'Hate crimes frequency against Transgender.')
![Hate crimes frequency against White.](media/explore29.png 'Hate crimes frequency against White.')

# License

Scripts or "programs" in this repository plot and aggregate the hate
crimes (per group of people) data from 2009 to 2024 acquired from the
Federal Bureau of Investigation's (FBI) National Incident-Based
Reporting System (NIBRS).

Copyright (C) 2024 Ahmad Tashfeen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the [GNU General Public License](COPYING)
along with this program. If not, see <https://www.gnu.org/licenses/>.
