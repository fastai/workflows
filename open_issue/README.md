# Open A GitHub Issue

> Open an issue, but optionally skip if an existing issue with the same title already exists.

## Documentation

```yaml
inputs:
  repo:
    description: "The owner/repo that you want to open an issue in.  For example 'fastai/fastai'"
    required: true
    default: ${{ github.repository }}
  title:
    description: 'Issue Title'
    required: true
  body:
    description: 'Issue Body'
    required: true
  token:
    description: 'GitHub Token'
    required: true
  skip_if_exists_flag:
    description: 'Setting this to any value will result in not an opening a new issue if there is an existing issue with the same title.'
    required: false
outputs:
  bool_new_issue_created: 
    description: "Returns 'True' or 'False' depending on if new issue was created.  Can only be 'False' if input skip_if_exists_flag is specified."
  related_issue_num: 
    description: "Returns issue number of issue that was created.  If a new issue is not created because of the skip_if_exists_flag, the issue number of corresponding existing issue is returned."
  related_issue_url: 
    description: "Same as related_issue_num except returns the URL for the issue instead of the issue number."
```

Full specification can be found [here](https://github.com/fastai/workflows/blob/master/open_issue/action.yml)


## Suggested Usage

```yaml
name: open issue
on: [workflow_dispatch]

jobs:
  open_issue:
    runs-on: ubuntu-latest
    name: test-open-issue
    steps:
    - uses: actions/setup-python@v2
    - uses: fastai/workflows/open_issue@master
      id: open_issue
      with:
        repo: ${{ github.repository }}
        title: "Test Open Issue"
        body: "Test Body"
        token: ${{ secrets.GITHUB_TOKEN }}
        skip_if_exists_flag: "Yes" # omit this input completely if you do not want to trigger this flag
    - name: see outputs
      run: |
        echo bool_new_issue_created ${{ steps.open_issue.outputs.bool_new_issue_created }} 
        echo related_issue_num ${{ steps.open_issue.outputs.related_issue_num }}
        echo related_issue_url ${{ steps.open_issue.outputs.related_issue_url }} 
```
