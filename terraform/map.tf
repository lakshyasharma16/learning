output "userage" {

  value = try("age of ${var.user} is ${lookup(var.userage, var.user)}")
#systax = try("age of ${variable} is ${lookup(variable_map, variable_map_key)}")
}

variable "userage" {
  type = map(any)
  default = {
    lakshya = 30
    kanu    = 20
	maa= 40
	papa=50
  }
}

#this variable is used to set the value for [output "userage"]
variable "user" {
  type    = string
  default = "lakshya"
}