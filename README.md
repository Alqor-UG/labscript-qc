# labscript-qc
A collection of spooler code to make quantum circuits accessible for labscript.

We are proud to be currently sponsored by the *Unitary Fund*. It enables us to set up a good test environment and make it as straight-forward as possible to integrate cold atoms with circuits. This documentation will improve as the good goes beyond the initial piloting status. 

[![Unitary Fund](https://img.shields.io/badge/Supported%20By-UNITARY%20FUND-brightgreen.svg?style=for-the-badge)](https://unitary.fund) 

## Installation

- Make sure that you have running installation of [labscript suite](https://github.com/labscript-suite).
- To install `labscript-qc` please clone the repository into the `userlib/pythonlib` folder of your labscript suite installation. 
- Install the `labscript-qc-example` into your labscriptlib. We typically give it the name `mot` for explantory purposes.

It is now time to configure the `labscript-qc` package. Some of the settings can be currently found in the `.env` file, some in the `settings.py` file and some in the `config.py` of the template itself. A more consistent configuration will be implemented in the future.

- Copy the `.env.example` file to `.env` and edit it to your needs.
- Update the `settings.py` file to your needs. We have tried to highlight the most important lines.

## Other projects

More mature partner projects are:

- [qiskit-cold-atom](https://github.com/qiskit-community/qiskit-cold-atom) - qiskit connection to cold atoms
- [qlued](https://github.com/Alqor-UG/qlued) - User and circuit management for atom circuits
- [sqooler](https://github.com/Alqor-UG/sqooler) - The simulator equivalent of `labscript-qc`


## Read the document here:
* Click [here](http://labscript-qc.readthedocs.io/) for the latest formatted release of the document at readthedocs.io.
* Click [here](docs/user_guide.md) for the local version of the document in Markdown format.
