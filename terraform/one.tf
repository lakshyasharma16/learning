output "name" {
  value = "Hello,${var.user} your age is ${var.age} and mobile number's ${var.mobile_index}th digit is ${var.mobile[var.mobile_index]}, are you married? : ${var.married}"
}

#variable user{}



#count = var.user == "lakshya" ? 0 : 1
#
#
#output "count" {
#  value = count
#}