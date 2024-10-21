data "aws_caller_identity" "current" {}

resource "aws_fis_experiment_template" "cpu_stress" {
  description = "Simulate CPU stress on selected EKS pods"
  role_arn    = var.fis_role_arn

  target {
    name           = "my-target"
    resource_type  = "aws:eks:pod"
    selection_mode = "ALL"

    parameters = {
      clusterIdentifier   = "arn:aws:eks:${var.aws_region}:${data.aws_caller_identity.current.account_id}:cluster/${var.eks_cluster_name}"
      namespace           = var.k8s_namespace
      selectorType        = "deploymentName"
      selectorValue       = var.k8s_deployment
      targetContainerName = var.k8s_container
    }
  }

  action {
    name      = "my-action"
    action_id = "aws:eks:pod-cpu-stress"

    parameter {
      key   = "kubernetesServiceAccount"
      value = var.fis_k8s_service_account
    }

    parameter {
      key   = "duration"
      value = var.experiment_duration
    }

    parameter {
      key   = "percent"
      value = var.experiment_stress_percent
    }

    parameter {
      key   = "workers"
      value = var.experiment_number_of_workers
    }

    target {
      key   = "Pods"
      value = "my-target"
    }

  }

  stop_condition {
    source = "none"
  }

  log_configuration {
    cloudwatch_logs_configuration {
      log_group_arn = "arn:aws:logs:${var.aws_region}:${data.aws_caller_identity.current.account_id}:log-group:/aws/eks/${var.eks_cluster_name}/cluster:*"
    }
    log_schema_version = 2
  }

  experiment_options {
    account_targeting            = "single-account"
    empty_target_resolution_mode = "fail"
  }

  tags = {
    name = "cpu-stress-tag"
  }
}

