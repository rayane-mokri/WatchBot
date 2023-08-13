//terraform init
//terraform fmt
//terraform validate
//terraform apply -auto-approve -var-file=../envs/secrets.tfvars

provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "bot" {
  ami             = var.ami_id
  instance_type   = var.instance_type
  key_name        = var.key
  vpc_security_group_ids = [var.security_group]
  tags = {
    Name = var.instance_name
  }
}

output "instance_ip" {
  value = aws_instance.bot.public_ip
}

