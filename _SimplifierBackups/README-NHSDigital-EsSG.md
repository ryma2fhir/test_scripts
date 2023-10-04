# Simplifier Project Source Control

A simple repo that can be forked and configured to download, unpack, commit, create a PR and merge the current state of a Simplifier project.  

## Prequsites

A valid Simplifier account.

## Enable actions

The action is disabled in this repo, so must be enabled.  Additionally, when forking a repo, even if an action is enabled in the original repo, it may be necessary to enable actions to run as they are by default set to disabled on fork.  See the github docs on [forking settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#controlling-changes-from-forks-to-workflows-in-public-repositories) in regards to actions, and [enabling/disabling](https://docs.github.com/en/actions/managing-workflow-runs/disabling-and-enabling-a-workflow) workflows for more details.

## Schedule to run

The action is set to run hourly by default in the [action file](.github/workflows/backup.yml#L6).  

Further info on using a [scheduled cron job](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule) in an action.

## Respository secrets required

Docs on [creating secrets for a respository](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository).

### Secrets to add:

* REPO_TOKEN  
  * A GitHub token that has privileges to create branches, commit to branches, use workflows and create PR's.  
  * See GitHub docs on [using PAT tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
* COMITTER  
  * User to commit as.  
* SIMPLIFIER_USER  
  * Simplifier user that has access to project.  
* SIMPLIFIER_PWD  
  * Password for Simplifier user.

## Respository variables required

Docs on [creating variables for a respository](https://docs.github.com/en/actions/learn-github-actions/variables#creating-configuration-variables-for-a-repository).

### Variables to add:

* COMITTER_NAME
  * Name of user to commit as.
* SIMPLIFIER_ADDRESS
  * Address of project - e.g. `https://api.simplifier.net/<project>/zip`
  * See Firely docs on project zip using the [Simplifier API](https://docs.fire.ly/projects/Simplifier/features/api.html#project-zip-api)

## Configure branches to delete automatically

The action will create and merge a PR into main.  To automatically delete the head branch when the PR is merged, see [GitHub docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-the-automatic-deletion-of-branches) 

Updated at: Tue Sep 26 19:11:34 UTC 2023
