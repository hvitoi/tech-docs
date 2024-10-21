output "fis_experiment_template_id" {
  description = "The ID of the created FIS experiment template"
  value       = aws_fis_experiment_template.cpu_stress.id
}
