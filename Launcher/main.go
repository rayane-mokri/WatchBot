package main

import (
	"fmt"
	"os"
	"os/exec"
)

func TerraformLaunch(workenv string, args ...string) {
	cmd := exec.Command("cmd", append([]string{"/c", "terraform"}, args...)...)
	cmd.Stdout = os.Stdout
	cmd.Dir = workenv

	if err := cmd.Run(); err != nil {
		fmt.Println("could not run command: ", err)
	}
}

func main() {
	workenv := "../TF_AWS/"
	TerraformLaunch(workenv, "init")
	TerraformLaunch(workenv, "validate")
	TerraformLaunch(workenv, "apply", "-auto-approve", "-var-file=../envs/secrets.tfvars")
	TerraformLaunch(workenv, "output", "-json", "instance_ip", ">>", "../Launcher/testing.json")
}
