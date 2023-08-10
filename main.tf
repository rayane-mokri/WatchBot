provider "aws" {
  region = var.aws_region
}


resource "aws_instance" "bot" {
  ami = var.ami_id
  instance_type = var.instance_type
  key_name = var.key

  tags = {
    Name = var.instance_name
  }

  provisioner "local-exec" {
    command = "sleep 30" # Wait for instance to fully initialize
  }
}

output "instance_ip" {
  value = aws_instance.bot.public_ip
}

//terraform init
//terraform fmt
//terraform validate
//terraform apply -var-file=envs/secrets.tfvars

