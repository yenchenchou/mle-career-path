# Helm

Helm is a package manager for Kubernetes. You can think of Helm as a tool for you to get a prebuilt templates since you usually need mutliple Kubernetes obejct at a time.

## Purpose

---
Due to software development becomes more micro service oriented, which means people are building specific apps with different dependicies and setting in paralleled. To speed up the process, companies use Kubenetes to managed the projects and it turns out that there are too many Kubernetes need to managed.

Thus, Helm is the very tool to help you:

* Manage and deploy different Kubernets object in very little command.

* Centralized Management on the configuration so that you don't need to edit the same value across different Kubernets object.

* A popular place to deploy, diff, check history, monitoryour app.

## Important conponents in Helm

---

1. Chart: A collection of Kubernetes objects/files
2. Repository: A place where you save your chart
3. Release:An instance created by the chart. One chart can produce many release

## Process to deploy by Helm

---

1. Search for repository from various resource
2. Choose the repository that fit most to you
3. Run `helm install <chart>` or modify the `.yaml` files then run `helm install <chart>`
4. Done!

## Built-in Objects

---

* `Release`: This object describes the release itself. It has several objects inside of it:
  * `Release.Name`: The release name
  * `Release.Namespace`: The namespace to be released into (if the manifest doesn’t override)
  * `Release.IsUpgrade`: This is set to true if the current operation is an upgrade or rollback.
  * `Release.IsInstall`: This is set to true if the current operation is an install.
  * `Release.Revision`: The revision number for this release. On install, this is 1, and it is incremented with each upgrade and rollback.
  * `Release.Service`: The service that is rendering the present template. On Helm, this is always Helm.*

* Values: Values passed into the template from the values.yaml file and from user-supplied files. By default, Values is empty.

* [Additional Resource](https://helm.sh/docs/chart_template_guide/builtin_objects/)
