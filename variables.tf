variable "aws_region" {
  description = "AWS region for the EC2 instance"
  type        = string
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
}

variable "instance_name" {
  description = "Name tag for the EC2 instance"
  type        = string
}

variable "instance_type" {
  default = "Instance type"
  type    = string
}

variable "key" {
  default = "Key name"
  type = string
}