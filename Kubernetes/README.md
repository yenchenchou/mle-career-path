# Kubernetes Note

## Workload Resource

### Deployment

```Yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  # A Deployment named nginx-deployment
  name: nginx-deployment
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
