variable "client_id" {
    default = "ca103843-cede-4b94-888c-6f722b723813"
}
variable "client_secret" {
    default = "c8f52072-edbe-4824-9a40-8ce5bd085eef"
}

variable "agent_count" {
    default = 3
}

variable "ssh_public_key" {
    default = "~/.ssh/id_rsa.pub"
}

variable "dns_prefix" {
    default = "k8striniti"
}

variable cluster_name {
    default = "k8striniti"
}

variable resource_group_name {
    default = "azure-k8striniti"
}

variable location {
    default = "Central US"
}

#variable log_analytics_workspace_name = "testLogAnalytics"

# refer https://azure.microsoft.com/global-infrastructure/services/?products=monitor for log analytics available regions
variable log_analytics_workspace_location {
    default = "eastus"
}

# refer https://azure.microsoft.com/pricing/details/monitor/ for log analytics pricing 
variable log_analytics_workspace_sku {
    default = "PerGB2018"
}
