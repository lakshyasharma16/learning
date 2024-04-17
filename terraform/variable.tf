variable "user" {
  type    = string
  default = "laksh"
}

variable "age" {
  type    = number
  default = 30
}

variable "mobile" {
  type    = list(number)
  default = [9, 8, 9, 7, 1, 8, 6, 7, 2, 3]
}
variable "mobile_index" {
  type    = number
  default = 9
}


variable "married" {
  type    = bool
  default = false
}


#use this command for plan
#terraform plan -out abc.out
#terraform apply "abc.out"
