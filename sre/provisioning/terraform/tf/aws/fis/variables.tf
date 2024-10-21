variable "aws_region" {
  description = "The AWS region to use"
  type        = string
  default     = "us-east-1"
}

variable "fis_role_arn" {
  description = "The ARN of the IAM role to be used by FIS"
  type        = string
  default     = "arn:aws:iam::000000000000:role/my-role"
}

variable "fis_k8s_service_account" {
  description = "Service Account"
  type        = string
  default     = "myserviceaccount"
}

variable "eks_cluster_name" {
  description = "The name of the EKS cluster"
  type        = string
  default     = "henry-sandbox"
}

variable "k8s_namespace" {
  description = "The Kubernetes namespace where the target pod resides"
  type        = string
  default     = "default"
}

variable "k8s_deployment" {
  description = "The name of the Kubernetes deployment containing the pod to stress"
  type        = string
  default     = "nginx-deployment"
}

variable "k8s_container" {
  description = "The name of the container inside the pod to stress"
  type        = string
  default     = "nginx-container"
}

variable "experiment_duration" {
  description = "The duration of the CPU stress action (ISO 8601 duration format)"
  type        = string
  default     = "PT5M"
}

variable "experiment_stress_percent" {
  description = "The percentage of CPU to stress on the target pod"
  type        = string
  default     = "70"
}

variable "experiment_number_of_workers" {
  description = "The number of workers (threads) to simulate CPU stress"
  type        = number
  default     = 1
}

variable "log_group" {
  description = "The ARN of the CloudWatch log group to store logs"
  type        = string
  default     = "arn:aws:logs:us-east-1:000000000000:log-group:/aws/eks/henry-sandbox/cluster:*"
}
