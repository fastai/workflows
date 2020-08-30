# conda-env

This is a GitHub Action that lets you use conda in your environment. If you're using miniconda3 and the base environment, you've got nothing to change. Otherwise, set these additional parameters as needed:

- `conda_env` (default - base): Environment to activate
- `conda_env` (default - miniconda3): Name of your base conda folder (normally `miniconda3` or `anaconda3`)
- `conda_prefix` (default - derived from `$HOME`, `conda_name`, and `conda_env`): Full path to conda folder (leave empty if you use `conda_env` or `conda_name`)
