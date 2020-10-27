# DBKS - a Databricks CLI

## Environment variables
- DBC_HOST
- DBC_TOKEN

## Cluster definition YAML example
```yaml
---
cluster-1:
    cluster_name: cluster-1
    spark_version: 6.6.x-scala2.11
    node_type_id: c4.2xlarge
    driver_node_type_id: i3.xlarge
    autoscale:
        min_workers: 1
        max_workers: 8
    ...

cluster-2:
    cluster_name: cluster-2
    ...
```
