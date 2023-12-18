---
comments: true
---

# Welcome to Sqooler

This is a library that cloud access of cold atom experiments that are running with [labscript](https://docs.labscriptsuite.org/en/latest/)through the `qiskit-cold-atom` and the `qlued` interface:

- `qiskit-cold-atom` allows the enduser to write the circuit definitions on its laptop and send them to the server in form of a nice *json* file.
- `qlued` handles the user management and stores the received *json* file in an appropiate queue.
- `labscript-qc` acts as the backend that performs the calculations from the queue and sends back the result into the storage.

To enable this work-flow, the labscript sequences have to written according to  a few rules on how to parse the json files etc. This is what we have started to standardize and simplify as much as possible. In the following we documented each module its purpose and look forward to your contributions.

## Integrating with labscript

- Make sure that you have running installation of [labscript suite](https://github.com/labscript-suite).
- To install `labscript-qc` please clone the repository into the `userlib/pythonlib` folder of your labscript suite installation. 
- Install the `labscript-qc-example` into your labscriptlib. We typically give it the name `mot` for explantory purposes.

It is now time to configure the `labscript-qc` package. Some of the settings can be currently found in the `.env` file, some in the `settings.py` file and some in the `config.py` of the template itself. A more consistent configuration will be implemented in the future.

- Copy the `.env.example` file to `.env` and edit it to your needs.
- Update the `settings.py` file to your needs. We have tried to highlight the most important lines.

Most likely you will stumble across the question of the fitting storage. We need to enable the storage of the settings, which we manage with [python-decouple](https://pypi.org/project/python-decouple/). To do so, create a `.env` file in the root directory. 
```
project
│   README.md
│   maintainer.py
|   .env
|   ...    
│
└───.github
│   │   ...
|
└───utils
│   │   ...
|
│   ...
```

An example content of this file would be:

``` python
# setting for MongoDB
MONGODB_USERNAME = <YOUR-USERNAME>
MONGODB_PASSWORD = <YOUR-PASSWORD>
MONGODB_DATABASE_URL = <YOUR-URL>

# settings for the Dropbox, if you use it as a storage
APP_KEY=<YOUR-APP-KEY>
APP_SECRET=<YOUR-APP-SECRED>
REFRESH_TOKEN=<YOUR-REFRESH-TOKEN>
```

Then, to configure the storage make sure which one you use as we provide different options. For example, if you use the MongoDB storage you have to set the `MONGODB_USERNAME`, `MONGODB_PASSWORD` and `MONGODB_DATABASE_URL`.

If you use the Dropbox storage, add the `APP_KEY`, `APP_SECRET` and `REFRESH_TOKEN` to the `.env` file.

To run the system you should run the `maintainer` with `python maintainer.py`.

!!! note
    
    This step also uploads the configuration of the backends onto the storage. So it is crucial for any kind of tests that involve `qlued`.

## Our other projects
* [``qlued``](https://github.com/alqor-ug/qlued) - API code that manages users etc for this project.
* [``sqooler``](https://github.com/alqor-ug/sqooler) - Simulator backends.

## Related projects

* [``qiskit-cold-atom``](https://github.com/qiskit-community/qiskit-cold-atom) - QisKit examples