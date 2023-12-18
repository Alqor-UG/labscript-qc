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

## Contributing

See [the contributing guide](docs/contributing.md) for detailed instructions on how to get started with a contribution to our project. We accept different **types of contributions**, most of them don't require you to write a single line of code.

On the [labscript-qc](https://alqor-ug.github.io/labscript-qc/) site, you can click the make a contribution button at the top of the page to open a pull request for quick fixes like typos, updates, or link fixes.

For more complex contributions, you can [open an issue](https://github.com/alqor-ug/labscript-qc/issues) to describe the changes you'd like to see.

If you're looking for a way to contribute, you can scan through our [existing issues](https://github.com/alqor-ug/labscript-qc/issues) for something to work on. 

### Join us in discussions

We use GitHub Discussions to talk about all sorts of topics related to documentation and this site. For example: if you'd like help troubleshooting a PR, have a great new idea, or want to share something amazing you've learned in our docs, join us in the [discussions](https://github.com/alqor-ug/labscript-qc/discussions).

## License

Any code within this repo is licenced under the [Apache 2](LICENSE) licence.


The labscript-qc documentation in the docs folders are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).


## Thanks :purple_heart:

Thanks for all your contributions and efforts towards improving labscript-qc. We thank you for being part of our :sparkles: community :sparkles:!

## Other projects

Other related partner projects are:

- [qiskit-cold-atom](https://github.com/qiskit-community/qiskit-cold-atom) - qiskit connection to cold atoms
- [qlued](https://github.com/Alqor-UG/qlued) - User and circuit management for atom circuits
- [sqooler](https://github.com/Alqor-UG/sqooler) - The simulator equivalent of `labscript-qc`