output "user_age" {

  value = try("age of ${var.user_name} is ${lookup(var.user_age, var.user_name)}")
#systax = try("age of ${variable} is ${lookup(variable_map, variable_map_key)}")
}

variable "user_age" {
  type = map(any)
  default = {
    lakshya = 40
    kanu    = 20
	maa= 40
	papa=50
  }
}

#this variable is used to set the value for [output "user_age"]
variable "user_name" {
  type    = string
  default = "papa"
}