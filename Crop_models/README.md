# Crop simulation models and sensitivity analysis
> Seminar, Introduction to Digital Agro.

[![License](https://img.shields.io/github/license/EDSEL-skoltech/multi_objective_irrigation)](https://github.com/EDSEL-skoltech/multi_objective_irrigation/blob/main/LICENSE)
[![issues](https://img.shields.io/github/issues/EDSEL-skoltech/multi_objective_irrigation)](https://github.com/EDSEL-skoltech/multi_objective_irrigation/issues)
[![Rg](https://img.shields.io/badge/ResearchGate-Follow-green)](https://www.researchgate.net/project/Digital-Agro)




## Presentation

Crop models - [pdf](https://drive.google.com/file/d/1ao2In-YExZ3Jcu7GyjihcBBPjN8SoGh9/view?usp=sharing)

## Google Colab 

Open `Seminar_Crop_Model.ipynb` in Google Colab!

<a href="https://colab.research.google.com/github/EDSEL-skoltech/Intro_to_Digital_Agriculture/blob/main/Crop_models/Seminar_Crop_Model.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>


Open `Seminar_Sensitivity_analysis.ipynb` in Google Colab!

<a href="https://colab.research.google.com/github/EDSEL-skoltech/Intro_to_Digital_Agriculture/blob/main/Crop_models/Seminar_Sensitivity_analysis.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Dependencies 

PCSE/WOFOST - Python Crop Simulator Environment

https://pcse.readthedocs.io/en/stable/

SAlib - Sensitivity Analysis Library in Python

https://salib.readthedocs.io/en/latest/


## Installation

Clone this repository and create new `conda env` on your local machine

`git clone https://github.com/EDSEL-skoltech/Intro_to_Digital_Agriculture`

Create new env with `pcse` package for crop models WOFOST

`cd Crop_models`

`conda env create -f py3_pcse.yml`

`conda activate py3_pcse`


## Meta

Mikhail Gasanov – Mikhail.Gasanov@skoltech.ru

## License

Distributed under the MIT license. See ``LICENSE`` for more information.



## Homework
 

> In our lab work, we will use the crop simulation model WOFOST. Documentation for package and model: https://pcse.readthedocs.io/. Your task will be to conduct any crop growth simulations for several years for the Moscow region or any other. It will also be necessary to conduct a sensitivity analysis and optimize the irrigation strategy. For sensitivity analysis, we will use the SALib package. For optimization, we will use Nevergrad package.
 
All the necessary data is available in the GitHub repository and in Google Colabs.
 
 
### Part 1 – Crop Yield Prediction (PCSE/WOFOST) - 4 points

Assess the yield of one of the crops for the Moscow region over several years (potatoes, sugar beets or others)
* Crop - [List of crops](https://github.com/ajwdewit/WOFOST_crop_parameters)
* Weather - NASAdataprovider in [PCSE](https://pcse.readthedocs.io/en/stable/code.html?highlight=NASA#pcse.db.NASAPowerWeatherDataProvider)

Generate plots for biomass growth, crop yield and seasonal weather for one year\
Plot weather dynamics (`T min`, `ET0` or others)

Agromanagement for Moscow Potato crop and NPK fertilization
```
"name": "Potato", 
"latitude": 54.85,
"longitude": 38.85, 
"crop_start": "2019-04-20", 
"crop_end": "2019-09-15", 
"crop_name": "potato", 
"npk_events": ["2019-06-22"], 
"npk": [[90,10,90]]
```

#### Available crops

```
from pcse.fileinput import YAMLCropDataProvider
cropd = YAMLCropDataProvider()
cropd.print_crops_varieties()
```
 
### Part 2 – Sensitivity Analysis (SALib) - 4 points
1) Perform sensitivity analysis of one of the model blocks (crop, soil, agromanagement *) with SALib. You can choose one of the methods that you consider necessary (Sobol, FAST, ...). Generate samples – In report provide the size of the resulting matrix and the sample size (N). Conduct parameter sensitivity analysis  - In report provide S1 and ST indices.  
List of available crop parameters: 
df=pd.read_excel("./data/ScalarParametersOfWofost-Potential.xlsx")
display(df)
2) Generate plots (Hist, etc.)
*3) Speed-up sensitivity analysis with multiprocessing
*4) Estimate the required number of simulations to obtain reliable values of the sensitivity indices. Try to estimate the sample size at the confidence interval of the sensitivity indices.

### Part 3 – Optimization (Nevergrad) - 2 points 
 
The task is to compare several optimizers from the Nevergrad package with the Random Search method. To do this, you can use the visualizations provided in the notebook. It is also necessary to determine the required size of the budget.



## Contributing

1. Fork it (<https://github.com/EDSEL-skoltech/Intro_to_Digital_Agriculturefork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

