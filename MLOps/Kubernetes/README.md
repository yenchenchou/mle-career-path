# Kubernetes Note

## Overview

---

### [Kubernetes Architecture](https://doc.clickup.com/p/h/81y26-21/b5244c4b291d9ea)

### Kubernetes Components

![k8simage](https://d33wubrfki0l68.cloudfront.net/2475489eaf20163ec0f54ddc1d92aa8d4c87c96b/e7c81/images/docs/components-of-kubernetes.svg)

### Kubernetes Objects

def: persistent entities in the Kubernetes system. Kubernetes uses these entities to represent the state of your cluster. Usually we use `.yaml` to contorl the objects, which including:

- What containerized applications are running (and on which nodes)
- The resources available to those applications
- The policies around how those applications behave, such as restart policies, upgrades, and fault-tolerance

#### Reauire Fields in each objects / taml files

- `apiVersion` - Which version of the Kubernetes API you're using to create this object
- `kind` - What kind of object you want to create
- `metadata` - Data that helps uniquely identify the object, including a name string, UID, and optional namespace
- `spec` - What state you desire for the object

#### namespace

- Kubernetes supports multiple virtual clusters backed by the same physical cluster. These virtual clusters are called namespaces.
- Most Kubernetes resources (e.g. pods, services, replication controllers, and others) are in some namespaces. However namespace resources are not themselves in a namespace. And low-level resources, such as nodes and persistentVolumes, are not in any namespace.

#### Labels and Selectors

Labels are key/value paiar that identify attributes of objects that are meaningful and relevant to users. Unlike names and UIDs, labels do not provide uniqueness. Via a label selector, the client/user can identify a set of objects. Labels is a **identifying** metadata that will actually point to objects.

#### [Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)

You can use Kubernetes annotations to attach arbitrary non-identifying metadata to objects. Labels can be used to select objects and to find collections of objects that satisfy certain conditions. In contrast, annotations are not used to identify and select objects.

Here are some examples of information that could be recorded in annotations:

- Fields managed by a declarative configuration layer. Attaching these fields as annotations distinguishes them from default values set by clients or servers, and from auto-generated fields and fields set by auto-sizing or auto-scaling systems.

- Build, release, or image information like timestamps, release IDs, git branch, PR numbers, image hashes, and registry address.

- Pointers to logging, monitoring, analytics, or audit repositories.

- Client library or tool information that can be used for debugging purposes: for example, name, version, and build information.

- User or tool/system provenance information, such as URLs of related objects from other ecosystem components.

- Lightweight rollout tool metadata: for example, config or checkpoints.

- Phone or pager numbers of persons responsible, or directory entries that specify where that information can be found, such as a team web site.

- Directives from the end-user to the implementations to modify behavior or engage non-standard features.

## Cluster Architecture

## Workload Resource

### [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

```Yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  # A Deployment named nginx-deployment
  name: nginx-deployment
  # select a label called app: ngnix that is defined in the pod template
  labels:
    app: nginx
spec:
  replicas: 3
  # .spec.selector field defines how the Deployment finds which Pods to manage. In this case, you select the pod by a label (app: ngnix)
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    # The Pod template's specification
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2  # runs the nginx Docker Hub image at version 1.14.2.
        ports:
        - containerPort: 80
```

### Service Account

A service account provides an identity for processes that run in a Pod. [see more](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  serviceAccountName: build-robot  # the service account is set by you or your admin, default to 'default'
  automountServiceAccountToken: false
  ...
```

## Labels and Annotations

**Labels are for Kubernetes, while annotations are for humans.**

1. Labels: key/value pairs that are attached to objects and to **identify** a set of objects/resources. Thet are related to K8S.
2. Annotations: For “non-identifying information” i.e., metadata that Kubernetes does not care about.

## Additional info for Pods

### Pod Topology Spread Constraints

You can use topology spread constraints to control how Pods are spread across your cluster among failure-domains such as regions, zones, nodes, and other user-defined topology domains. This can help to achieve high availability as well as efficient resource utilization. [see more](https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/). [see topologyKey](https://kubernetes.io/docs/reference/labels-annotations-taints/)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  topologySpreadConstraints:
    - maxSkew: <integer>
      topologyKey: <string>  # [see](https://kubernetes.io/docs/reference/labels-annotations-taints/)
      whenUnsatisfiable: <string>
      labelSelector: <object>
```

### Define Environment Variables for a Container

When you create a Pod, you can set environment variables for the containers that run in the Pod. To set environment variables, include the env or envFrom field in the configuration file. [See more](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: envar-demo
  labels:
    purpose: demonstrate-envars
spec:
  containers:
  - name: envar-demo-container
    image: gcr.io/google-samples/node-hello:1.0
    env:
    - name: DEMO_GREETING
      value: "Hello from the environment"
    - name: DEMO_FAREWELL
      value: "Such a sweet sorrow"
```

### Define a Command and Arguments for a Container

[see more](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: command-demo
  labels:
    purpose: demonstrate-command
spec:
  containers:
  - name: command-demo-container
    image: debian
    command: ["printenv"]
    args: ["HOSTNAME", "KUBERNETES_PORT"]
  restartPolicy: OnFailure
```

### Configure Liveness, Readiness and Startup Probes

This is to configure liveness, readiness and startup probes for containers.

The kubelet uses liveness probes to know when to restart a container. For example, liveness probes could catch a deadlock; The kubelet uses readiness probes to know when a container is ready to start accepting traffic; The kubelet uses startup probes to know when a container application has started. If such a probe is configured, it disables liveness and readiness checks until it succeeds. [See more](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)

To Protect slow starting containers with startup probes, you set both livenessProbe and startupProbe. Once the startup probe has succeeded once, the liveness probe takes over to provide a fast response to container deadlocks.

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: liveness
  name: liveness-exec
spec:
  containers:
  - name: liveness
    image: k8s.gcr.io/busybox
    args:
    - /bin/sh
    - -c
    - touch /tmp/healthy; sleep 30; rm -rf /tmp/healthy; sleep 600
    livenessProbe:
      exec:
        command:
        - cat
        - /tmp/healthy
      initialDelaySeconds: 5
      # perform a liveness probe every 5 seconds.
      periodSeconds: 5
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: liveness
  name: liveness-http
spec:
  containers:
  - name: liveness
    image: k8s.gcr.io/liveness
    args:
    - /server
    livenessProbe:
    # To perform a probe, the kubelet sends an HTTP GET request to the server that is running in the container and listening on port 8080.
      httpGet:
        path: /healthz
        port: 8080
        httpHeaders:
        - name: Custom-Header
          value: Awesome
      initialDelaySeconds: 3
      periodSeconds: 3
```

## Volumes

To use a volume, specify the volumes to provide for the Pod in `.spec.volumes` and declare where to mount those volumes into containers in `.spec.containers[*].volumeMounts`. [see more](https://kubernetes.io/docs/concepts/storage/volumes/)

## ConfigMaps

A ConfigMap is an API object used to store non-confidential data in key-value pairs. Pods can consume ConfigMaps as environment variables, command-line arguments, or as configuration files in a volume. [see more](https://kubernetes.io/docs/concepts/configuration/configmap/)
