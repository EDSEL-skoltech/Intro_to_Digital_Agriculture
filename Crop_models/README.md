# Crop simulation models and sensitivity analysis
> Seminar, Introduction to Digital Agro.

[![License](https://img.shields.io/github/license/EDSEL-skoltech/multi_objective_irrigation)](https://github.com/EDSEL-skoltech/multi_objective_irrigation/blob/main/LICENSE)
[![issues](https://img.shields.io/github/issues/EDSEL-skoltech/multi_objective_irrigation)](https://github.com/EDSEL-skoltech/multi_objective_irrigation/issues)
[![Rg](https://img.shields.io/badge/ResearchGate-Follow-green)](https://www.researchgate.net/project/Digital-Agro)




<!-- ![graphical](plots_ICCS/Graphical_abstract.png) -->

## Google Colab 

Open `How_to_start.ipynb` in Google Colab!

<a href="https://colab.research.google.com/github/EDSEL-skoltech/multi_objective_irrigation/blob/main/How_to_start.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

To plot results of optimization open `Plots_for_ICCS.ipynb`

<a href="https://colab.research.google.com/github/EDSEL-skoltech/multi_objective_irrigation/blob/main/Plots_for_ICCS.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Dependencies 

PCSE/WOFOST - Python Crop Simulator Environment

https://pcse.readthedocs.io/en/stable/

SAlib - Sensitivity Analysis Library in Python

https://salib.readthedocs.io/en/latest/


## Installation

Clone this repository and create new `conda env` on your local machine

`git clone https://github.com/EDSEL-skoltech/multi_objective_irrigation.git`

Create new env with `pcse` package for crop models WOFOST

`conda env create -f py3_pcse.yml`

`conda activate py3_pcse`


## Meta

Mikhail Gasanov – Mikhail.Gasanov@skoltech.ru

## License

Distributed under the MIT license. See ``LICENSE`` for more information.


## TO-DO list

- [X] Weather loader from NASA-POWER
- [ ] Test how weather loader convert data to CSV
- [ ] Function to save optimal irrigation dates and volumes to txt file


## Contributing

1. Fork it (<https://github.com/EDSEL-skoltech/multi_objective_irrigation/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

